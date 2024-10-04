"""
main.py
This script executes a series of tasks and optionally generates example plots. 
It imports task solutions from the 'solution' module and plotting functions 
from the 'example_plot' module. 
Functions:
- solution_task2(): Executes the solution for task 2.
- solution_task3(): Executes the solution for task 3.
- solution_task4(): Executes the solution for task 4.
"""


from solution import solution_task2, solution_task3, solution_task4
from example_plot import custom_plot, simple_line_plot

# Task 2
solution_task2()

# Task 3
solution_task3()

# Task 4
solution_task4()

# Plots examples - Uncomment to see example plots
# Simple plot
# simple_line_plot([1, 2, 3, 4], [1, 4, 2, 3])
# Custom plot
# custom_plot()
