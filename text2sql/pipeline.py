from __future__ import annotations

from .config import ProjectConfig
from .dataset import Text2SQLExample
from .evaluation import ExecutionEvaluator
from .inference import TextToSQLPipeline
from .training import TrainerFacade


class ProjectPipeline:
    """Convenience orchestrator tying together training, inference, and eval."""

    def __init__(self, config: ProjectConfig | None = None) -> None:
        self.config = config or ProjectConfig()
        self.trainer = TrainerFacade(self.config)
        self.inference = TextToSQLPipeline(self.config)
        self.evaluator = ExecutionEvaluator()

    def train(self):
        return self.trainer.run()

    def predict(self, example: Text2SQLExample):
        return self.inference.generate(example)
