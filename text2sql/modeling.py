from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LoRAConfig:
    r: int = 16
    alpha: int = 32
    dropout: float = 0.05


class Text2SQLModel:
    """Facade for the base Mistral checkpoint and its adapter weights."""

    def __init__(self, base_model_name: str, lora: LoRAConfig | None = None) -> None:
        self.base_model_name = base_model_name
        self.lora = lora or LoRAConfig()

    def describe(self) -> str:
        return (
            f"Base model: {self.base_model_name}; "
            f"LoRA r={self.lora.r}, alpha={self.lora.alpha}, dropout={self.lora.dropout}"
        )
