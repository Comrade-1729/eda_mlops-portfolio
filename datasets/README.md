# 📂 Datasets

This directory contains **all data used in the project**, organized to enforce
immutability, traceability, and analytical safety.

---

## 📁 Directory Structure

datasets/
├── raw/ # Original source data (never modified)
├── processed/ # Cleaned, indexed, frozen artifacts

---

## 🔒 Raw Data (`datasets/raw`)

- Represents the **source of truth**
- Files are ingested exactly as provided by data sources
- Never mutated or overwritten
- Used only via ingestion scripts

Subdirectories map directly to domains:

- `climate/` → OpenAQ air quality
- `health/` → WHO GHE DALYs
- `eco-digital/` → World Bank indicators
- `risk/` → EM-DAT, UNODC, WHO road safety

---

## ❄️ Processed Data (`datasets/processed`)

- Output of explicit preprocessing scripts
- Each file corresponds to a **defined analytical contract**
- Treated as immutable once generated
- Used by notebooks and synthesis logic

Examples:

- `environment_stress_index.csv`
- `health_burden_index.csv`
- `digital_divide_index.csv`
- `risk_exposure_index.csv`

---

## ⚠️ Important Rules

- Missing data is treated as **structural absence**, not noise
- No imputation is performed
- Processed datasets are not silently regenerated
- Any change requires explicit script execution

---

## 🎯 Why This Matters

Separating raw and processed data:

- prevents accidental data leakage
- enables auditability
- mirrors production analytics systems

This is a deliberate design choice, not overhead.
