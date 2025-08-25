# ATU Programming & Scripting Project — Iris Dataset

This repository analyses Fisher’s Iris dataset in Python.  
It contains:
- a Python script: `analysis.py`
- a generated summary text file: `summary.txt`
- image outputs in `images/`
- the dataset saved locally as `data/iris.csv`

> The Iris data used here originates from the UCI Machine Learning Repository (Dataset ID 53).

---

## What the code does

`analysis.py`:
1. Retrieves the Iris data (via scikit-learn) and writes it to `data/iris.csv`.
2. Writes a textual summary to `summary.txt` (descriptive stats + class counts).
3. Saves histograms for each numeric feature to `images/`.
4. Saves scatter plots for every pair of numeric features to `images/`.

**Key libraries:** `pandas`, `matplotlib`, `seaborn`, `scikit-learn`.

---

## How to run

From the repository folder:

```bash
python3 analysis.py