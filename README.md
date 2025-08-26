# ATU Programming & Scripting Project — Iris Dataset

This repository analyses Fisher’s Iris dataset using Python (script and Jupyter notebook).


## Repository Structure

analysis.py          # Main script: generates summary + plots
iris_analysis.ipynb  # Notebook: mini exploratory analysis with outputs
data/iris.csv        # Local copy of dataset (auto-generated if missing)
images/              # Auto-generated plots from analysis.py
summary.txt          # Auto-generated text summary
requirements.txt     # Dependencies
.gitignore           # Ignore system files / artefacts
PROMPTS.md           # AI assistance log (sessions & prompts)

---

## What the Code Does
- Loads the Iris dataset (`data/iris.csv`, or regenerates via scikit-learn if missing).  
- Writes a text summary to `summary.txt`.  
- Saves histograms and pairwise scatter plots into `images/`.  
- Provides an exploratory notebook (`iris_analysis.ipynb`) for visual inspection.  


## How to Run (script)

```bash
# 1) Clone
git clone https://github.com/USERNAME/pands-project.git
cd pands-project

# 2) Create environment (conda or venv — either is fine)
# conda:
conda create -n iris python=3.10 -y
conda activate iris
# or venv:
python3 -m venv .venv && source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run script
python3 analysis.py

---

## What the Code Does
- Loads the Iris dataset (`data/iris.csv`, or regenerates via scikit-learn if missing).  
- Writes a text summary to `summary.txt`.  
- Saves histograms and pairwise scatter plots into `images/`.  
- Provides an exploratory notebook (`iris_analysis.ipynb`) for visual inspection.  


## How to Run (script)

```bash
# 1) Clone
git clone https://github.com/USERNAME/pands-project.git
cd pands-project

# 2) Create environment (conda or venv — either is fine)
# conda:
conda create -n iris python=3.10 -y
conda activate iris
# or venv:
python3 -m venv .venv && source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run script
python3 analysis.py

---

## What the Code Does
- Loads the Iris dataset (`data/iris.csv`, or regenerates via scikit-learn if missing).  
- Writes a text summary to `summary.txt`.  
- Saves histograms and pairwise scatter plots into `images/`.  
- Provides an exploratory notebook (`iris_analysis.ipynb`) for visual inspection.  


## How to Run (script)

```bash
# 1) Clone
git clone https://github.com/USERNAME/pands-project.git
cd pands-project

# 2) Create environment (conda or venv — either is fine)
# conda:
conda create -n iris python=3.10 -y
conda activate iris
# or venv:
python3 -m venv .venv && source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run script
python3 analysis.py

Outputs will appear in:
	•	summary.txt
	•	images/*.png

⸻

How to Run (notebook)
	•	Open iris_analysis.ipynb in VS Code or Jupyter.
	•	Run all cells to see dataset shape, class counts, histograms, and scatter plots.

Tip:
If notebook is inside a subfolder, update image/data paths:
	•	../images/…
	•	../data/iris.csv

⸻

Dataset
	•	Source: UCI Machine Learning Repository — Iris
	•	Instances: 150 (3 classes × 50 each)
	•	Features: 4 numeric (sepal length/width, petal length/width)

⸻

Findings (brief)
	•	Each class has 50 rows (balanced).
	•	Petal measurements separate classes more clearly than sepal measurements.
	•	Histograms indicate different spreads/centres across classes.

⸻

Requirements

See requirements.txt.

⸻

References
	•	R. A. Fisher (1936). The use of multiple measurements in taxonomic problems.
	•	UCI ML Repository: Iris dataset (link above).
	•	scikit-learn: sklearn.datasets.load_iris used to regenerate CSV if missing.
	•	pandas / matplotlib for data handling and plots.

——-

AI Assistance (disclosure)

I used an AI assistant (ChatGPT) for planning, debugging, and wording the README.
Prompts & summaries are recorded in PROMPTS.md (non-verbatim, paraphrased).
All code and analysis were understood and typed by me.
