import sys
import subprocess


def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])


# List of required packages
required_packages = ["numpy", "matplotlib", "image_gen"]

# Install each required package
for package in required_packages:
    install(package)
