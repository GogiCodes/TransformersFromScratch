from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .prompts import PromptBuilder
from .schema import Column, TableSchema


@dataclass(slots=True)
class Text2SQLExample:
    question: str
    sql: str
    tables: list[TableSchema]
    db_path: Path | None = None


class SpiderDatasetAdapter:
    """Lightweight adapter for Spider-style examples."""

    def __init__(self, examples: Iterable[Text2SQLExample]) -> None:
        self.examples = list(examples)

    def as_prompts(self) -> list[dict[str, str]]:
        records: list[dict[str, str]] = []
        for example in self.examples:
            records.append(
                {
                    "prompt": PromptBuilder.build(example.question, example.tables),
                    "completion": example.sql,
                }
            )
        return records


def demo_examples() -> list[Text2SQLExample]:
    return [
        Text2SQLExample(
            question="List the names of all students.",
            sql="SELECT name FROM students;",
            tables=[TableSchema(name="students", columns=[Column(name="id", type="INTEGER", is_primary_key=True), Column(name="name", type="TEXT")])],
        )
    ]
