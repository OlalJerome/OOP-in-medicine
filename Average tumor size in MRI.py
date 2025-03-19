import pytest
import numpy as np
# Average Tumor Size (Loops & Lists)
# Filename: average_tumor_size.py
# Write a function `average_tumor_size(sizes)` that calculates the average tumor size from a list of measurements.

def average_tumor_size(sizes):
    if not sizes:
        return 0
    total =0
    for size in sizes:
        total+=size
    return total/len(sizes)