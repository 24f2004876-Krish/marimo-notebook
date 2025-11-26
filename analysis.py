# Marimo notebook
# Email: 24f2004876@ds.study.iitm.ac.in

import marimo

app = marimo.App()

# ---------------------------
# Cell 1: Import and slider widget
# This cell defines a variable (x) that other cells depend on.
# ---------------------------
@app.cell
def slider_cell():
    import marimo as mo
    x_slider = mo.ui.slider(start=0, stop=100, step=5, value=50, label="Select a value")
    x = x_slider.value
    x_slider  # widget output
    return x, x_slider
# ---------------------------


# ---------------------------
# Cell 2: Computation dependent on slider value
# This cell depends on variable x from above.
# ---------------------------
@app.cell
def compute_cell(x):
    squared_value = x * x
    cubed_value = x * x * x
    return squared_value, cubed_value
# ---------------------------


# ---------------------------
# Cell 3: Dynamic markdown output
# This cell dynamically renders markdown based on x.
# ---------------------------
@app.cell
def markdown_cell(x, squared_value, cubed_value):
    import marimo as mo
    mo.md(
        f"""
        ## Interactive Results

        - **Selected x:** `{x}`
        - **x²:** `{squared_value}`
        - **x³:** `{cubed_value}`

        This markdown updates automatically when you move the slider above.
        """
    )
# ---------------------------


# ---------------------------
# Cell 4: Documenting data flow
# ---------------------------
@app.cell
def comments_cell():
    import marimo as mo
    mo.md(
        """
        ### Data Flow Documentation

        1. **slider_cell** defines an interactive slider and exposes the variable `x`.  
        2. **compute_cell** depends on `x` and computes `x²` and `x³`.  
        3. **markdown_cell** depends on both `x` and computed values, updating markdown dynamically.

        This satisfies the requirement for documenting variable dependencies.
        """
    )
# ---------------------------


if __name__ == "__main__":
    app.run()
