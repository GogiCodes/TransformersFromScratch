from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class EvaluationResult:
    exact_match: bool
    execution_match: bool
    predicted_rows: list[tuple]
    gold_rows: list[tuple]


class ExecutionEvaluator:
    """Run predicted and gold SQL against SQLite for execution-based scoring."""

    def evaluate(self, db_path: Path, predicted_sql: str, gold_sql: str) -> EvaluationResult:
        predicted_rows = self._execute(db_path, predicted_sql)
        gold_rows = self._execute(db_path, gold_sql)
        return EvaluationResult(
            exact_match=self._normalize(predicted_sql) == self._normalize(gold_sql),
            execution_match=predicted_rows == gold_rows,
            predicted_rows=predicted_rows,
            gold_rows=gold_rows,
        )

    @staticmethod
    def _normalize(sql: str) -> str:
        return " ".join(sql.lower().strip().rstrip(";").split())

    @staticmethod
    def _execute(db_path: Path, sql: str) -> list[tuple]:
        if not db_path.exists():
            return []
        with sqlite3.connect(db_path) as connection:
            cursor = connection.execute(sql)
            return cursor.fetchall()
