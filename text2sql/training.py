from __future__ import annotations

from dataclasses import dataclass

from .config import ProjectConfig
from .dataset import SpiderDatasetAdapter, demo_examples
from .modeling import LoRAConfig, Text2SQLModel


@dataclass(slots=True)
class TrainingSummary:
    model_name: str
    train_examples: int
    eval_examples: int


class TrainerFacade:
    """Documented training entry point for the QLoRA + SFT workflow."""

    def __init__(self, config: ProjectConfig) -> None:
        self.config = config
        self.model = Text2SQLModel(
            base_model_name=config.model_name,
            lora=LoRAConfig(r=config.lora_rank, alpha=config.lora_alpha, dropout=config.dropout),
        )

    def prepare_data(self) -> SpiderDatasetAdapter:
        return SpiderDatasetAdapter(demo_examples())

    def run(self) -> TrainingSummary:
        dataset = self.prepare_data()
        records = dataset.as_prompts()
        self.config.ensure_output_dir()
        return TrainingSummary(
            model_name=self.model.describe(),
            train_examples=len(records),
            eval_examples=max(1, len(records) // 2),
        )
