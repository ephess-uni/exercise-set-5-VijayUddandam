""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""

import numpy as np
import argparse  

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    # Create argument parser object
    parser = argparse.ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")

    parser.add_argument("infile", help="Input filename for the data file to be processed")
    parser.add_argument("outfile", help="Output filename to write the processed data")

    args = parser.parse_args()

    input_data = np.loadtxt(args.infile)

    data_mean = np.mean(input_data)
    data_std = np.std(input_data)

    processed_data = (input_data - data_mean) / data_std

    np.savetxt(args.outfile, processed_data)
