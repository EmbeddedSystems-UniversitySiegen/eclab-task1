"""
Example of using the stream_plot decorator to stream a plot to the browser.
Use the plotting functions as shown in the example below to stream the plot to the browser.

"""


from plot_image import stream_plot
from matplotlib import pyplot as plt
import numpy as np


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


if __name__ == '__main__':
    # Simple plot
    simple_line_plot([1, 2, 3, 4], [1, 4, 2, 3])
    # Custom plot
    custom_plot()
