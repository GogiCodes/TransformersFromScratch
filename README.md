# 🗄️ Mistral-7B-Text2SQL

[![Model](https://img.shields.io/badge/Model-Mistral--7B--v0.1-blue)](https://huggingface.co/mistralai/Mistral-7B-v0.1)
[![Dataset](https://img.shields.io/badge/Dataset-Spider-green)](https://yale-nlp.github.io/spider/)
[![Quantization](https://img.shields.io/badge/Quantization-4--bit%20QLoRA-orange)](#)
[![Accuracy](https://img.shields.io/badge/Execution%20Accuracy-49%25%20(%2B15%25)-brightgreen)](#)

A high-performance Text-to-SQL generation pipeline built by fine-tuning **Mistral-7B** on the **Spider** benchmark using **QLoRA (4-bit quantization)** and Hugging Face's `SFTTrainer`. Featuring an automated schema formatting engine and an execution-verified SQLite evaluation pipeline, this model turns natural language queries into executable, schema-compliant SQL.

---

## ✨ Key Capabilities

* **Resource-Efficient Fine-Tuning:** Leveraged 4-bit QLoRA (NormalFloat4) and PEFT to fine-tune Mistral-7B on consumer-grade GPU hardware without sacrificing performance.
* **Automated Schema Engine:** Custom preprocessing pipeline that serializes complex SQLite database schemas (tables, columns, foreign keys) into clean, token-efficient prompt templates.
* **Execution-Verified Evaluation:** Validates generated SQL against a live SQLite engine using strict Execution Accuracy (EX) rather than fragile string-matching metrics.
* **Significant Accuracy Gains:** Boosted execution accuracy by **+15 percentage points** over the base model on unseen Spider test/dev schemas.

---

## 📊 Evaluation Results

Evaluated on a subset of the **Spider Development Set**:

| Model / Configuration | Fine-Tuning Method | Execution Accuracy (EX) |
| :--- | :--- | :---: |
| **Mistral-7B-Instruct (Baseline)** | Zero-Shot Prompting | **34.0%** |
| **Mistral-7B-Text2SQL (Ours)** | **4-bit QLoRA + SFTTrainer** | **49.0% (+15.0%)** |

> **Why Execution Accuracy Matters:** Standard string matching (exact match) fails when SQL queries use different aliases or join orders that yield identical results. Our pipeline executes predictions directly against SQLite databases to measure true execution correctness.

---

## 🏗️ Pipeline Architecture
