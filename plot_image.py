import base64
import io
import sys
import matplotlib.pyplot as plt


def capture_plot():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.clf()
    return image_base64


def plot_to_stdout(plot_data):
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
