import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium", css_file="./custom.css")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Heading 1**
    ## Heading 2
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop =10, step =1)
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.ui.text("hi "*slider.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    version 3
    """)
    return


if __name__ == "__main__":
    app.run()
