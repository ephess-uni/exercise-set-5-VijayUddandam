"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths.  Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"

# Process the input data using numpy

# Save the result to output_file
data = np.loadtxt(input_file, delimiter=',')

# Set any negative elements of the array to 0
data[data < 0] = 0

# Write the processed array to a file named outputs/ex_5_4-processed.csv using numpy.savetxt
np.savetxt(output_file, data, delimiter=',')

# Print a message indicating successful completion
print("Processing completed. Output saved to:", output_file)