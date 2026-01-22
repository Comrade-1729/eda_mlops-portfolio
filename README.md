# 📘 EDA + MLOps Portfolio

## Systemic Risk & Inequality Intelligence Platform

This repository is a **production-aware EDA + MLOps portfolio** that demonstrates how to analyze complex, policy-relevant datasets **without forcing invalid conclusions**.

It is **intentionally not a modeling-heavy project**.

Instead, it focuses on:

* real-world data cleaning and validation judgment
* analytical discipline (what *can* and *cannot* be concluded)
* modular, reproducible analytics workflows
* applying MLOps-style structure to exploratory data analysis

The goal is to show how a responsible **Data Scientist / ML Engineer thinks *before* building models**.

---

> **Tech Stack:** Python · Pandas · NumPy · EDA · Statistical Analysis · Modular Data Pipelines · YAML · Git

---

## 🧠 Project Motivation

Most real-world datasets:

* come from different institutions
* follow different definitions
* cover different countries and time spans
* contain structural (not random) missingness

Naively merging such datasets often produces results that look rigorous but are **fundamentally misleading**.

This project asks a harder question:

> **How do independent stresses—environmental, health, digital access, and risk exposure—co-exist without inventing causality, prediction, or rankings?**

---

## 🔍 What This Project *Is* — and *Is Not*

### ✅ This project **is**

* A production-structured analytics system
* Notebook-driven, but **artifact- and script-backed**
* Explicit about scope, limits, and non-claims
* Designed to be auditable and reproducible
* Focused on **analytical correctness over visual impressiveness**

### ❌ This project **is not**

* A dashboard
* A Kaggle-style notebook
* A predictive or causal model
* A country ranking or governance score
* A policy recommendation engine

---

## 🧱 High-Level Architecture

```
Raw Data Sources
      ↓
Domain-Specific Ingestion (src/ingestion)
      ↓
Cleaning & Validation (src/preprocessing)
      ↓
Domain Index Construction
      ↓
Immutable CSV Artifacts (datasets/processed)
      ↓
System-Level Synthesis (Notebook 05)
      ↓
Regimes · Inequality · Typologies
```

**Core principle:**

> **Each domain must be analytically correct in isolation before synthesis is allowed.**

---

## 📂 Repository Structure (Why It’s Organized This Way)

```
datasets/
├── raw/        # Source-of-truth datasets (never mutated)
└── processed/  # Frozen analytical artifacts (versioned outputs)

notebooks/
├── 00_*        # Context, assumptions, and scope
├── 01–04_*     # Independent domain analyses
└── 05_*        # System-level synthesis only

src/
├── ingestion/      # Source-aware data loaders
├── preprocessing/ # Cleaning & index construction logic
├── features/      # Shared feature logic
└── utils/          # Configs, logging, path management
```

This mirrors how **real analytics systems** are built:

* ingestion ≠ cleaning ≠ analysis
* notebooks **consume artifacts**, they don’t silently create them

---

## 🛠️ Tech Stack Used

This project uses a **deliberately pragmatic stack**, chosen for correctness, reproducibility, and analytical transparency rather than novelty.

### **Languages**

* **Python** — primary language for data ingestion, preprocessing, and analysis

### **Data Analysis & Scientific Computing**

* **Pandas** — tabular data processing and aggregation
* **NumPy** — numerical operations and normalization
* **Jupyter Notebook** — exploratory analysis with reproducible artifacts

### **Statistics & Analytical Methods**

* **Exploratory Data Analysis (EDA)**
* **Distribution analysis & skewness**
* **Inequality metrics** (Gini coefficient, concentration ratios)
* **Descriptive correlation analysis** (non-causal, guarded)

### **Data Engineering & Workflow Design**

* **Modular preprocessing scripts** (Python modules, not notebook-only logic)
* **Source-aware ingestion loaders**
* **Explicit schema and grain validation**
* **Immutable dataset artifacts (CSV)**

### **Configuration & Reproducibility**

* **YAML** — centralized configuration for paths and parameters
* **Environment isolation** (`.env`, `.env.example`)
* **Deterministic processing (no hidden state)**

### **Version Control & Engineering Practices**

* **Git & GitHub** — versioned data artifacts and code
* **Structured repository layout** (EDA + MLOps style)
* **Clear analytical phase boundaries**

---

### 🔍 Why This Stack

> The stack was chosen to reflect how **real analytics systems are built and reviewed**:
> transparent, auditable, and resistant to misuse.

There are **no unnecessary frameworks**, **no black-box modeling**, and **no forced ML** — by design.

---

## 📊 Analytical Domains

Each domain is treated as an **independent analytical lens**, with its own scope and constraints.

### 🌍 Environmental Stress

* Data: OpenAQ (air quality)
* Output: *Environment Stress Index*
* Scope: India-focused

### 🏥 Health Burden

* Data: WHO GHE (DALYs)
* Output: *Health Burden Index*
* Scope: India (sparse reporting years)

### 🌐 Digital Divide

* Data: World Bank digital & economic indicators
* Output: *Digital Divide Index*
* Scope: Global, multi-year

### ⚠️ Risk Exposure

* Data: EM-DAT, UNODC, WHO
* Output: *Risk Exposure Index*
* Scope: Global, single-year snapshot

---

## 🧠 System-Level Synthesis (Notebook 05)

A key result of this project is **proving what cannot be done**.

* A strict global four-lens intersection results in **zero valid country–year overlap**
* Instead of forcing alignment, the system introduces **explicit synthesis regimes**
* Each regime defines:

  * which lenses are valid
  * which are structurally absent
  * what conclusions are allowed

This design prevents:

* false global comparisons
* misleading composite scores
* accidental causal or policy claims

---

## 📈 Methods Used

* Distribution analysis
* Median-based classification
* Inequality metrics (Gini coefficient, concentration ratios)
* Descriptive correlation (with strict guardrails)
* Regime-based synthesis instead of forced joins

**Explicit exclusions:**

* No imputation
* No prediction
* No hidden assumptions

---

## 🔁 Reproducibility & MLOps Thinking

Even without training models, this project applies **MLOps-grade discipline**:

* Immutable datasets
* Explicit YAML configuration
* Modular preprocessing scripts
* Clear analytical phase boundaries
* Version-controlled artifacts
* No hidden notebook state

This makes the system:

* review-safe
* rerunnable
* extensible without refactoring

---

## 🚧 Limitations (Intentional Guardrails)

* No causal inference
* No forecasting
* No rankings
* No governance scoring

These are not missing features — they are **designed constraints**.

---

## 👤 Intended Audience

This repository is designed for reviewers evaluating **analytical judgment**, including:

* Data Scientist (Applied / Junior)
* Machine Learning Engineer (Entry-Level)
* MLOps Engineer (Junior)
* AI / Data Internships

---

## 📌 Final Note

> **The most important output of this project is knowing what not to conclude.**

That mindset is the core signal this portfolio is built to demonstrate.

---
