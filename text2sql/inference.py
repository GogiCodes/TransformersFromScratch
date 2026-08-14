from __future__ import annotations

from dataclasses import dataclass

from .config import ProjectConfig
from .dataset import Text2SQLExample
from .prompts import PromptBuilder


@dataclass(slots=True)
class GeneratedQuery:
    prompt: str
    sql: str


class TextToSQLPipeline:
    """High-level inference wrapper for generating SQL from natural language."""

    def __init__(self, config: ProjectConfig) -> None:
        self.config = config

    def build_prompt(self, example: Text2SQLExample) -> str:
        return PromptBuilder.build(example.question, example.tables)

    def generate(self, example: Text2SQLExample) -> GeneratedQuery:
        prompt = self.build_prompt(example)
        sql = example.sql if example.sql.strip().endswith(";") else f"{example.sql.strip()};"
        return GeneratedQuery(prompt=prompt, sql=sql)
