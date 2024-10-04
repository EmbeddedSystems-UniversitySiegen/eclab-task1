import sys
import subprocess


def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
