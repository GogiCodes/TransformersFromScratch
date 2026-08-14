from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(slots=True)
class Column:
    name: str
    type: str
    is_primary_key: bool = False
    is_foreign_key: bool = False
    references: str | None = None


@dataclass(slots=True)
class TableSchema:
    name: str
    columns: list[Column]


class SchemaSerializer:
    """Serialize Spider-style database schemas into compact prompts."""

    @staticmethod
    def format_table(table: TableSchema) -> str:
        columns = []
        for column in table.columns:
            flags = []
            if column.is_primary_key:
                flags.append("pk")
            if column.is_foreign_key and column.references:
                flags.append(f"fk->{column.references}")
            suffix = f" [{', '.join(flags)}]" if flags else ""
            columns.append(f"{column.name}:{column.type}{suffix}")
        return f"{table.name}({', '.join(columns)})"

    @classmethod
    def serialize(cls, tables: Iterable[TableSchema]) -> str:
        return " | ".join(cls.format_table(table) for table in tables)
