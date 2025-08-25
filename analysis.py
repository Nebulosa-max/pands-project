print("analysis.py is running ✔")

# Tiny sanity test so we know Python can import libraries
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    print("Imported pandas and matplotlib ✔")
except Exception as e:
    print("Import error:", e)

# Keep the script obviously doing something
print("All good — you can build your Iris code here next.")
