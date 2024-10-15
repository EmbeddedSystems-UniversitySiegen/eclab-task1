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

## Plotting Utilities

The `plot_image.py` file contains functions for plotting images using Matplotlib. For usage examples, refer to the `example_plot.py` file, which demonstrates how to capture and stream plots as base64-encoded PNG images.

This utility includes:

`capture_plot`: Captures the current Matplotlib plot and encodes it as a base64 PNG image.
`plot_to_stdout`: Streams the base64-encoded image data to stdout in chunks.
`stream_plot`: A decorator that automatically captures and streams the plot data for any Matplotlib plotting function.

Below is an example demonstrating how to plot a simple linear function and a sine wave over a specified range. These utilities simplify the process of capturing and streaming Matplotlib plots, making them suitable for embedding in web applications or APIs.

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

## Testing

The `tests/test_task1.py` file contains a simple test case for the `solution.py` functions. The test case verifies the correctness of the function by comparing the output with the expected solution.
To run the tests, add the module to the Python path and execute the test file.

```BASH
export PYTHONPATH=$PYTHONPATH:"$PWD/src"
pytest
```

## References

- [Introduction to Python](https://www.w3schools.com/python/python_getstarted.asp)
- [Solving linear equations](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.solve.html)
- [Matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py)
