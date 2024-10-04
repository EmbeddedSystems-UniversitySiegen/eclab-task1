"""
This script provides a function to install a Python module using pip. It leverages the subprocess module to 
call pip as a subprocess, ensuring that the specified module is installed in the current Python environment.
Functions:
    install_module(module_name): Installs the specified Python module using pip.
    Example: 
    if __name__ == '__main__':
        install_module('numpy')
"""


import sys
import subprocess


def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])


