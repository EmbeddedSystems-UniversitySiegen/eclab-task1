"""
This module provides utilities for capturing and streaming matplotlib plots
as base64-encoded PNG images. It includes functions to capture a plot, stream
the plot data to stdout, and a decorator to automate the capture and streaming
process for any matplotlib plotting function.
"""
import base64
import io
import sys
import matplotlib.pyplot as plt


def capture_plot():
    """
    Captures the current matplotlib plot as a base64-encoded PNG image.

    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.clf()
    return image_base64


def plot_to_stdout(plot_data):
    """
    Streams the given base64- plot data to stdout in chunks.
    """
    print("BEGIN_PLOT")
    for i in range(0, len(plot_data), 1000):  # Send in chunks
        chunk = plot_data[i:i+1000]
        print(chunk)
    print("END_PLOT")
    sys.stdout.flush()


def stream_plot(func):
    """
    A decorator that wraps matplotlib plotting functions to automatically
    capture and stream the plot.
    """
    def wrapper(*args, **kwargs):
        plt.figure()
        func(*args, **kwargs)
        plot_data = capture_plot()
        plot_to_stdout(plot_data)
    return wrapper
