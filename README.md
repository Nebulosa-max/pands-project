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

# PROMPTS / AI Assistance Log

I used ChatGPT to help plan, debug, and polish documentation. Below are paraphrased summaries of the prompts I used (no verbatim copying, just descriptions):

1) **Repo setup & debugging**  
   Asked: why my `analysis.py` couldn’t find `analysis.py` / CSV; how to structure folders; how to commit/push step by step.

2) **Iris pipeline**  
   Asked: write a small script that loads Iris, generates `summary.txt`, saves histograms and scatter plots, and regenerates `data/iris.csv` from scikit-learn if missing.

3) **Notebook**  
   Asked: minimal notebook that loads `data/iris.csv`, prints shape/class counts/`describe()`, and draws simple histograms & scatter plots (saving to `images/`).

4) **README polishing**  
   Asked: organize the README so the examiner can run the project quickly; include references and an AI disclosure.

All analysis / coding decisions were understood and typed in by me; I verified and executed the code locally.

