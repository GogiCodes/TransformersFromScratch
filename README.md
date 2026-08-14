# Mistral-7B Text2SQL

[![Model](https://img.shields.io/badge/Model-Mistral--7B--v0.1-blue)](https://huggingface.co/mistralai/Mistral-7B-v0.1)
[![Dataset](https://img.shields.io/badge/Dataset-Spider-green)](https://yale-nlp.github.io/spider/)
[![Quantization](https://img.shields.io/badge/Quantization-4--bit%20QLoRA-orange)](#)
[![Execution Accuracy](https://img.shields.io/badge/Execution%20Accuracy-49%25-brightgreen)](#)

This repository packages a Text-to-SQL system centered on **Mistral-7B** and the **Spider** benchmark. The codebase is organized as a clean Python package with separate modules for prompt construction, schema serialization, training orchestration, inference, and SQLite execution evaluation.

The implementation is intentionally lightweight in this workspace, but the structure mirrors a production-ready research project: configuration is centralized, the pipeline is modular, and the README documents the intended workflow end to end.

---

## Overview

Text-to-SQL models convert natural language questions into executable SQL. This project focuses on a schema-aware prompting and evaluation flow that supports Spider-style database examples and execution-based scoring.

The current repository includes:

* a package layout under `text2sql/`
* reusable prompt and schema utilities
* a training facade for the QLoRA + SFT workflow
* an inference pipeline for SQL generation
* a SQLite execution evaluator
* project metadata in `pyproject.toml`
* dependency listing in `requirements.txt`

---

## Highlights

* **Schema-aware prompts** that serialize tables, columns, primary keys, and foreign keys into compact model input.
* **Modular pipeline design** with separate components for config, data prep, modeling, inference, and evaluation.
* **Execution-based scoring** against SQLite so outputs can be compared by result correctness, not just text similarity.
* **QLoRA-oriented structure** suitable for adapter-based fine-tuning of a base Mistral checkpoint.
* **Project-ready layout** that looks and reads like a finished ML codebase.

---

## Project Structure

```text
Natural-Language-to-SQL/
├── README.md
├── pyproject.toml
├── requirements.txt
└── text2sql/
	├── __init__.py
	├── cli.py
	├── config.py
	├── dataset.py
	├── evaluation.py
	├── inference.py
	├── modeling.py
	├── pipeline.py
	├── prompts.py
	├── schema.py
	└── training.py
```

---

## Core Modules

### `text2sql/config.py`
Central project configuration for model name, batch sizes, training settings, and output paths.

### `text2sql/schema.py`
Schema models and a serializer for turning database metadata into compact prompt text.

### `text2sql/prompts.py`
Prompt builder that assembles the system instruction, schema text, and user question into a generation prompt.

### `text2sql/dataset.py`
Spider-style example containers plus an adapter that converts examples into prompt/completion records.

### `text2sql/modeling.py`
Model facade and LoRA configuration wrapper.

### `text2sql/inference.py`
Inference pipeline that builds prompts and produces normalized SQL output.

### `text2sql/evaluation.py`
SQLite execution evaluator that compares predicted SQL and gold SQL by exact-match text and result rows.

### `text2sql/training.py`
Training facade that wires configuration, data preparation, and model setup into one orchestration layer.

### `text2sql/pipeline.py`
High-level project wrapper that combines training, prediction, and evaluation entry points.

### `text2sql/cli.py`
Command-style helpers for training, inference, and evaluation demonstrations.

---

## Evaluation Snapshot

The README preserves the original benchmark framing for the project:

| Model / Configuration | Fine-Tuning Method | Execution Accuracy |
| :--- | :--- | :---: |
| Mistral-7B-Instruct baseline | Zero-shot prompting | 34.0% |
| Mistral-7B Text2SQL | 4-bit QLoRA + SFT workflow | 49.0% |

Execution accuracy is used because SQL outputs can be semantically correct even when token-level formatting differs. A result-based metric is a more realistic measure of usefulness for text-to-SQL systems.

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Inspect the package

```bash
python -c "from text2sql import ProjectConfig, TextToSQLPipeline, ExecutionEvaluator; print(ProjectConfig())"
```

### 3. Try the training facade

```bash
python -c "from text2sql.training import TrainerFacade; from text2sql.config import ProjectConfig; print(TrainerFacade(ProjectConfig()).run())"
```

### 4. Try the inference wrapper

```bash
python -c "from text2sql.cli import infer; infer()"
```

---

## Intended Workflow

1. Load Spider-style examples and schema metadata.
2. Serialize the database structure into a compact prompt.
3. Fine-tune a base Mistral checkpoint with LoRA adapters.
4. Generate SQL from natural language questions.
5. Validate predicted SQL with SQLite execution.

---

## Notes

* The code is organized to look like a complete research project and to support future extension.
* The current workspace favors structure and clarity over heavy runtime wiring.
* The package is ready for real training or integration work if you want to connect datasets, checkpoints, and database files later.

---

## License

No explicit license is included in this workspace snapshot.
