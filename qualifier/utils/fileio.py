# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for saving the CSV Files.

    # Define the output path
    csvpath = Path("qualifying_loans.csv")

    # Set to write CSV file in csvpath
    with open(csvpath, 'w', newline='') as csvfile:
        
        # Set up a writer tool to write a CSV file
        csvwriter = csv.writer(csvfile)

        # Write the CSV data   
        for row in qualifying_loans:
            csvwriter.writerow(row)