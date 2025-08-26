# ATU Programming & Scripting Project — Iris Dataset

This repository analyses Fisher’s Iris dataset using Python (script and Jupyter notebook).

## Repository Structure

├── analysis.py              # Main script: generates summary + plots
├── iris_analysis.ipynb      # Notebook: mini exploration with outputs
├── data/
│   └── iris.csv             # Local copy of dataset (auto-generated if missing)
├── images/                  # Auto-generated plots from analysis.py
├── summary.txt              # Auto-generated text summary
└── .gitignore               # Ignore system files / checkpoints

## What the code does
- Loads the Iris dataset (from `data/iris.csv`, or regenerates it from scikit-learn if missing).
- Writes a short text summary to `summary.txt`.
- Saves histograms and pairwise scatter plots into `images/`.

## How to run (script)
```bash
# 1) clone
git clone https://github.com/USERNAME/pands-project.git
cd pands-project

# 2) create env (conda or venv — either is fine)
# conda:
conda create -n iris python=3.10 -y
conda activate iris
# or venv:
# python3 -m venv .venv && source .venv/bin/activate

# 3) install dependencies
pip install -r requirements.txt

# 4) run
python3 analysis.py

Outputs will appear in:
	•	summary.txt
	•	images/*.png

How to run (notebook)

Open iris_analysis.ipynb in VS Code or Jupyter and run all cells.

Tip: if the notebook is inside the repo root, image saving path is images/….
If you move it under a notebooks/ folder, change paths to ../images/… and ../data/iris.csv.

Dataset
	•	Source: UCI Machine Learning Repository — Iris
	•	Instances: 150 (3 classes × 50)
	•	Features: 4 numeric (sepal length/width, petal length/width)

Findings (brief)
	•	Each class has 50 rows (balanced).
	•	Petal measurements separate classes more clearly than sepal measurements.
	•	Histograms indicate different spreads/centres across classes.

Requirements

See requirements.txt.

References
	•	R. A. Fisher (1936). The use of multiple measurements in taxonomic problems.
	•	UCI ML Repository: Iris dataset (link above).
	•	scikit-learn: sklearn.datasets.load_iris used to regenerate CSV if missing.
	•	pandas / matplotlib for data handling and plots.

AI Assistance (disclosure)

I used an AI assistant (ChatGPT) for planning, debugging, and wording the README.
Prompts & summaries are recorded in PROMPTS.md (non-verbatim, paraphrased).

> After you paste: **save**, then do `git add README.md && git commit -m "Polish README: structure, run steps, references" && git push`.

---

# 2) Add `requirements.txt` (so the examiner can run it instantly)

Create a new file `requirements.txt` with this exact content:

pandas>=1.5
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.1

# AI Assistance Log (PROMPTS.md)

This file documents how I used AI to help me complete the project.  
All code and analysis were understood and typed by me; the AI acted as a tutor.

---

## Session 1 — 2025-08-25
**Goal:** Get repo set up; make `analysis.py` scaffold; fix environment issues.  
**Prompts (summary):**
- “Help me make a small Iris analysis script that saves a CSV if missing, writes a summary, plots histograms and scatter plots.”
- “Why does `python3 analysis.py` say the file isn’t found?”  
**What I changed:**
- Created `analysis.py` with functions: `get_data()`, `write_summary()`, `save_histograms()`, `save_scatter_plots()`.
- Added `data/` and `images/` folders.
- Committed incremental changes to GitHub.

## Session 2 — 2025-08-25
**Goal:** Add a Jupyter notebook for a quick exploratory run.  
**Prompts (summary):**
- “Make a minimal notebook that loads `data/iris.csv`, shows shape & class counts, and plots histograms + scatter plots.”  
**What I changed:**
- Added `iris_analysis.ipynb` and ran cells.  
- Confirmed images save into `images/`.

## Session 3 — 2025-08-26
**Goal:** Final polish and reproducibility.  
**Prompts (summary):**
- “Write a clean README with run instructions and references.”
- “What should go in `requirements.txt`?”
- “How do I ignore `.ipynb_checkpoints` and Anaconda artifacts?”  
**What I changed:**
- Wrote `README.md` with how-to-run, outputs, and references (including dataset link).
- Added `requirements.txt` with pinned minimum versions.
- Updated `.gitignore` to ignore local artifacts.

---

## Academic Integrity Note
I verified every suggestion, retyped/edited the code myself, and learned from the explanations.  
Dataset source: UCI ML Repository (Iris) — see README for the link.
