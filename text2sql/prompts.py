from __future__ import annotations

from .schema import SchemaSerializer, TableSchema


class PromptBuilder:
    """Build instruction-style prompts for text-to-SQL generation."""

    system_prompt = (
        "You are a precise text-to-SQL assistant. Produce one executable SQL query "
        "that matches the database schema and answers the user's request."
    )

    @classmethod
    def build(cls, question: str, tables: list[TableSchema], evidence: str | None = None) -> str:
        schema_text = SchemaSerializer.serialize(tables)
        evidence_text = f"\nEvidence: {evidence}" if evidence else ""
        return (
            f"{cls.system_prompt}\n\n"
            f"Schema: {schema_text}{evidence_text}\n\n"
            f"Question: {question}\n"
            "SQL:"
        )
