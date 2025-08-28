# ATU Programming & Scripting Project — Iris Dataset

This repository analyses Fisher’s Iris dataset using Python (script + Jupyter notebook).  
It is designed to be easy to run and easy to mark: clear structure, reproducible outputs, and proper references.

---

## Repository Structure

- `analysis.py` → Main script: generates/validates data, summary, and plots  
- `iris_analysis.ipynb` → Notebook: mini exploration with outputs  
- `data/iris.csv` → Local copy of dataset (auto-generated if missing)  
- `images/` → Auto-generated plots (histograms + scatter plots)  
- `summary.txt` → Auto-generated text summary  
- `requirements.txt` → Python packages (for quick setup)  
- `PROMPTS.md` → AI assistance log (how ChatGPT was used as tutor)  
- `.gitignore` → Ignore system/tool artifacts  

---

## What the Code Does

- Loads the Iris dataset (`data/iris.csv`, or regenerates it from scikit-learn if missing).  
- Writes a short text summary to `summary.txt`.  
- Saves histograms and pairwise scatter plots into `images/`.  

---

## How to Run (script)

1. **Clone the repository**
   
```bash
   git clone https://github.com/USERNAME/pands-project.git
   cd pands-project

2.	Create & activate and environment
 
(conda or venv — either is fine)
 •	Conda example:

conda create -n iris python=3.10 -y
conda activate iris
 •	venv example:

python3 -m venv .venvsource .venv/bin/activate   
# Mac/Linux
.venv\Scripts\activate      # Windows

3.	Install dependencies

pip install -r requirements.txt

4.	Run the script

python3 analysis.py

Outputs will appear in:
	•	summary.txt
	•	images/*.png
	•	(Re)generated data/iris.csv if it didn’t exist

⸻

How to Run (notebook)

Open iris_analysis.ipynb in VS Code or Jupyter and run all cells.

If you move the notebook under a notebooks/ folder, update any relative paths to ../images/ and ../data/iris.csv.

⸻

Dataset
	•	Source: UCI Machine Learning Repository — Iris
	•	Instances: 150 (3 balanced classes × 50)
	•	Features: 4 numeric (sepal length/width, petal length/width)

⸻

Findings (brief)
	•	Each class has 50 rows (balanced).
	•	Petal measurements separate the classes more clearly than sepal measurements.
	•	Histograms indicate different spreads/centres across classes.

⸻

Requirements

See requirements.txt (minimum versions pinned for the marker):

pandas>=1.5
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.1

References
	•	R. A. Fisher (1936). The use of multiple measurements in taxonomic problems.
	•	UCI ML Repository: Iris dataset (link above).
	•	scikit-learn: sklearn.datasets.load_iris used to regenerate CSV if missing.
	•	pandas / matplotlib / seaborn for data handling and plots.

⸻

AI Assistance (disclosure)

I used an AI assistant (ChatGPT) as a tutor to plan, debug, and polish documentation.
All code was understood and typed by me. A concise log is recorded in PROMPTS.md.