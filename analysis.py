# analysis.py — ATU P&S Project (Iris)
# Sophia Gotch

from pathlib import Path
from itertools import combinations
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# -------------------------
# Folders
# -------------------------
ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
IMAGES_DIR = ROOT / "images"
DATA_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(exist_ok=True)

# -------------------------
# Load / create dataset
# -------------------------
def _write_from_sklearn() -> pd.DataFrame:
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()                     # columns like 'sepal length (cm)'
    # Tidy column names
    rename = {
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)":  "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)":  "petal_width",
        "target":            "class",
    }
    df.rename(columns=rename, inplace=True)
    # Map numeric class -> label
    df["class"] = df["class"].map(dict(enumerate(iris.target_names)))
    # Save with headers
    csv_path = DATA_DIR / "iris.csv"
    df.to_csv(csv_path, index=False)
    print(f"Regenerated iris.csv at {csv_path.relative_to(ROOT)}")
    return df

def get_data() -> pd.DataFrame:
    csv_path = DATA_DIR / "iris.csv"
    if not csv_path.exists():
        return _write_from_sklearn()
    try:
        df = pd.read_csv(csv_path)            # read headers from file
        # Basic validation: 5 columns we expect
        if list(df.columns) != ["sepal_length","sepal_width","petal_length","petal_width","class"]:
            raise ValueError("Unexpected CSV columns")
        return df
    except Exception:
        print("iris.csv was invalid → regenerating from sklearn")
        return _write_from_sklearn()

# -------------------------
# Summary
# -------------------------
def write_summary(df: pd.DataFrame) -> None:
    out = ROOT / "summary.txt"
    with open(out, "w") as f:
        f.write("Iris Dataset Summary\n")
        f.write("="*30 + "\n\n")
        f.write(str(df.describe()) + "\n\n")
        f.write("Class counts:\n")
        f.write(str(df["class"].value_counts()) + "\n")
    print(f"Saved {out.relative_to(ROOT)}")

# -------------------------
# Plots
# -------------------------
def save_histograms(df: pd.DataFrame) -> None:
    for col in ["sepal_length","sepal_width","petal_length","petal_width"]:
        plt.figure()
        plt.hist(df[col], bins=20)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("count")
        out = IMAGES_DIR / f"hist_{col}.png"
        plt.tight_layout()
        plt.savefig(out)
        plt.close()
        print(f"Saved {out.relative_to(ROOT)}")

def save_scatter_plots(df: pd.DataFrame) -> None:
    # simple colour map per class
    palette = {"setosa":"tab:blue", "versicolor":"tab:orange", "virginica":"tab:green"}
    features = ["sepal_length","sepal_width","petal_length","petal_width"]
    for x, y in combinations(features, 2):
        plt.figure()
        for cls, sub in df.groupby("class"):
            plt.scatter(sub[x], sub[y], s=20, label=cls, alpha=0.8, c=palette.get(cls))
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend()
        plt.title(f"{x} vs {y}")
        out = IMAGES_DIR / f"scatter_{x}_vs_{y}.png"
        plt.tight_layout()
        plt.savefig(out)
        plt.close()
        print(f"Saved {out.relative_to(ROOT)}")

# -------------------------
# Main
# -------------------------
def main():
    df = get_data()
    write_summary(df)
    save_histograms(df)
    save_scatter_plots(df)
    print("All outputs written ✅")

if __name__ == "__main__":
    main()