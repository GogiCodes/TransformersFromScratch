from __future__ import annotations

from pathlib import Path

from .config import ProjectConfig
from .dataset import Text2SQLExample, demo_examples
from .evaluation import ExecutionEvaluator
from .inference import TextToSQLPipeline
from .schema import Column, TableSchema
from .training import TrainerFacade


def train() -> None:
    summary = TrainerFacade(ProjectConfig()).run()
    print(summary)


def infer() -> None:
    pipeline = TextToSQLPipeline(ProjectConfig())
    example = demo_examples()[0]
    print(pipeline.generate(example).sql)


def evaluate() -> None:
    evaluator = ExecutionEvaluator()
    db_path = Path("data/demo.sqlite")
    example = Text2SQLExample(
        question="List the names of all students.",
        sql="SELECT name FROM students;",
        tables=[TableSchema(name="students", columns=[Column(name="id", type="INTEGER", is_primary_key=True), Column(name="name", type="TEXT")])],
        db_path=db_path,
    )
    result = evaluator.evaluate(db_path, "SELECT name FROM students;", example.sql)
    print(result)
