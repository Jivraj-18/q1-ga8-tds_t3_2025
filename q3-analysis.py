# /// script
# marimo-version: 0.4.0
# ///

import marimo

app = marimo.App()

# A comment including your email:
# Author: Data Scientist | Contact: 22f3002542@ds.study.iitm.ac.in

# ---------------------------------------------
# Cell 1: Load synthetic dataset
# This cell produces the dataset used by downstream cells.
# ---------------------------------------------
@app.cell
def _(np):
    # Create a synthetic dataset for demonstration
    x = np.linspace(0, 10, 100)
    y = 3 * x + 5 + np.random.normal(0, 2, size=len(x))
    return x, y

# ---------------------------------------------
# Cell 2: Slider widget controlling smoothing
# This value is consumed by later cells.
# ---------------------------------------------
@app.cell
def _(mo):
    smoothing = mo.ui.slider(start=1, stop=20, step=1, value=5, label="Smoothing Window")
    smoothing
    return smoothing

# ---------------------------------------------
# Cell 3: Compute rolling average (depends on x, y, smoothing)
# Data flow: uses dataset from Cell 1 + widget value from Cell 2
# ---------------------------------------------
@app.cell
def _(np, y, smoothing):
    # Simple rolling mean operation
    window = smoothing.value
    y_smooth = np.convolve(y, np.ones(window) / window, mode="same")
    return y_smooth

# ---------------------------------------------
# Cell 4: Plot original vs smoothed curve
# Dynamic update whenever smoothing slider moves.
# ---------------------------------------------
@app.cell
def _(mo, x, y, y_smooth):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, label="Original", alpha=0.4)
    ax.plot(x, y_smooth, label="Smoothed", linewidth=2)
    ax.set_title("Relationship between X and Y")
    ax.legend()

    mo.pyplot(fig)

# ---------------------------------------------
# Cell 5: Dynamic Markdown responding to slider
# Data flow: reflects window size chosen in Cell 2
# ---------------------------------------------
@app.cell
def _(mo, smoothing):
    window = smoothing.value
    mo.md(f"""
### Smoothing Summary  
You selected a **window size of `{window}`**, which affects how much the curve is smoothed.

- A larger window results in **more smoothing** and less noise.
- A smaller window preserves **finer details** but keeps more noise.

The notebook is fully reactive — changing the slider updates the chart and this explanation.
""")

# ---------------------------------------------
# Dependencies
# ---------------------------------------------
@app.cell
def _():
    import numpy as np
    return np

@app.cell
def _():
    import marimo as mo
    return mo

if __name__ == "__main__":
    app.run()
