# Getting Started

```BASH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Installing Packages

- Install packages as per the requirements.txt file to run locally in your system. 
- To install modules or libraries for the tasks, use install_module.py file when running in the your team coding space https://eslab.es.eti.uni-siegen.de/codespace/eclab/ectask1.

```
Example:

    if __name__ == "__main__":
        install_module("numpy")
        install_module("matplotlib") 
```

## Plotting Graphs

- Use the functions in the plot_image.py file to plot images. Examples of plotting can be found in the example_plot.py file. This file provides utilities for capturing and streaming matplotlib plots as base64-encoded PNG images. It includes functions to capture a plot, stream the plot data to stdout, and a decorator to automate the capture and streaming process for any matplotlib plotting function.
The function capture_plot, captures the current matplotlib plot as a base64-encoded PNG image. The function plot_to_stdout streams the given base64-encoded plot data to stdout in chunks and the function stream_plot is a decorator that wraps matplotlib plotting functions to automatically capture and stream the plot. The below example shows plotting a simple linear plot and plotting non linear functions like sine wave between a particular range. 

```
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

- Introduction to python (https://www.w3schools.com/python/python_getstarted.asp)
- Solving linear equations (https://numpy.org/doc/1.25/reference/generated/numpy.linalg.solve.html)
- Matplotlib plotting (https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py)
- 3D plot (https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#sphx-glr-gallery-mplot3d-2dcollections3d-py)

