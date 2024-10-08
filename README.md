# Getting Started

```BASH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Installing Packages

- Install packages as per the requirements.txt file when running locally. 
- Use the `install_module.py` module to install an external module (if required) in [lab codespace](https://eslab.es.eti.uni-siegen.de/codespace/eclab/ectask1).

```Python
Example:

    if __name__ == "__main__":
        install_module("numpy")
        install_module("matplotlib") 
```

## Plotting Graphs

Use the functions in the plot_image.py file to plot images. 
Examples of plotting can be found in the example_plot.py file. The file provides utilities for capturing and streaming Matplotlib plots as base64-encoded PNG images. 
The file includes functions to capture a plot, stream the plot data to stdout, and a decorator to automate the capture and streaming process for any Matplotlib plotting function.

The function `capture_plot`, captures the current Matplotlib plot as a base64-encoded PNG image. The function `plot_to_stdout` streams the given base64-encoded plot data to stdout in chunks and the function `stream_plot` is a decorator that wraps Matplotlib plotting functions to capture and stream the plot automatically. The example below shows plotting a simple linear plot and nonlinear functions like sine wave for a given range. 

```Python
    @stream_plot
    def simple_line_plot(x, y):
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Simple Line Plot')


    @stream_plot
    def custom_plot():
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Sine Wave')
        plt.grid(True)


    # Simple plot
    simple_line_plot([1, 2, 3, 4], [1, 4, 2, 3])
    # Custom plot
    custom_plot()
```


## References

- [Introduction to Python](https://www.w3schools.com/python/python_getstarted.asp)
- [Solving linear equations](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.solve.html)
- [Matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py)

