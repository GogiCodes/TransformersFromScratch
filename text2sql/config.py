from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class ProjectConfig:
    """Shared project configuration for training and inference."""

    model_name: str = "mistralai/Mistral-7B-v0.1"
    dataset_name: str = "spider"
    output_dir: Path = field(default_factory=lambda: Path("artifacts") / "mistral-text2sql")
    max_source_length: int = 2048
    max_target_length: int = 256
    lora_rank: int = 16
    lora_alpha: int = 32
    dropout: float = 0.05
    learning_rate: float = 2e-4
    train_batch_size: int = 1
    eval_batch_size: int = 1
    gradient_accumulation_steps: int = 8
    num_train_epochs: int = 3
    seed: int = 42

    def ensure_output_dir(self) -> Path:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        return self.output_dir
