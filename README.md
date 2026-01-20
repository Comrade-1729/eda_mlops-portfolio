# MLOps / Portfolio Polish

## Objective

- Add logging for reproducibility and traceability
- Ensure project paths are **config-driven**
- Make the notebook **re-runnable end-to-end**
- Provide clear outputs for portfolio presentation
- Ensure all artifacts (plots, cleaned CSVs) are saved systematically

## Logging Setup

- Logging ensures **every key step is recorded**
- Useful for debugging, collaboration, and portfolio showcase

## Config-Driven Paths

- Config-driven paths make notebook **re-runnable on any machine**
- Easy to update paths globally instead of changing every cell

## Reproducibility: Random Seeds & Versions

- Seed ensures any stochastic operation (e.g., train-test splits) is reproducible
- Version logs help maintain **portfolio credibility**

## Saving Artifacts Automatically

- All key outputs (data + plots) are saved to structured folders
- Portfolio reviewers can **see raw data, plots, and results** immediately

## Notebook Re-Runnable Gaurantee

- ✅ All paths defined via PROJECT_ROOT
- ✅ Data ingestion via `load_data()`
- ✅ Cleaning via `clean_openaq()`
- ✅ Plots saved in `plots/climate` folder
- ✅ Logging records all important actions
- ✅ Random seeds set for reproducibility
