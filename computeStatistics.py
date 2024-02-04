"""
computeStatistics.py - Script that computes descriptive statistics from numbers on a file

This script reads a file containing numeric data, skips the values that are not numbers and then 
computes descriptive statistics (mean, median, mode, standard deviation, and variance). It prints
the results on the console and creates and a file named StatisticsResults.txt with all the gathered
information.
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import time
import math


# In[2]:


def open_file(path):
    """
    Open and read numeric data from a file. It also anlyze each value to confirm if it is a number
    if it is not, then it displays an error and skips it.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = []
        for line in file.readlines():
            stripped_data = line.strip()
            if stripped_data:
                try:
                    float_number = float(stripped_data)
                    data.append(float_number)
                except ValueError:
                    print(f"Warning: {stripped_data} is not a number and "
                          "will not be taken into account")
        return data


# In[3]:


def compute_statistics(data):
    """
    Compute descriptive statistics of the gathered data. The statistics are mean, median, mode,
    standard deviation and variance.
    """
    if data is None:
        return None

    n = len(data)
    mean = sum(data) / n
    sort = sorted(data)
    if n % 2 != 0:
        median = sort[n // 2]
    else:
        middle_left = sort[(n - 1) // 2]
        middle_right = sort[(n + 1) // 2]
        median = (middle_left + middle_right) / 2
    counts = {item: data.count(item) for item in set(data)}
    max_count = max(counts.values())
    if max_count == 1:
        modes = "NA"
    else:
        modes = [item for item, count in counts.items() if count == max_count]

    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    return n, mean, median, modes, std_dev, variance


# In[4]:


def main():
    """
    Main function to execute when the script is run. It verifies that the arguments 
    are written in the desired format. Then it opens the file, extracts the data and 
    computes the descriptive statistics. The results are printed in the console and 
    written in a .txt file.
    """
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    path = sys.argv[1]
    data = open_file(path)
    stats = compute_statistics(data)
    time_elapsed = time.time() - start_time
    if stats is not None:
        print("Count:", stats[0])
        print("Mean:", stats[1])
        print("Median:", stats[2])
        print("Mode:", stats[3])
        print("Standard Deviation:", stats[4])
        print("Variance:", stats[5])
        print(f"Time Elapsed:, {time_elapsed} seconds\n")
        with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.write(f"Count: {stats[0]}\n")
            result_file.write(f"Mean: {stats[1]}\n")
            result_file.write(f"Median: {stats[2]}\n")
            result_file.write(f"Mode: {stats[3]}\n")
            result_file.write(f"Standard Deviation: {stats[4]}\n")
            result_file.write(f"Variance: {stats[5]}\n")
            result_file.write(f"Time Elapsed: {time_elapsed} seconds\n")

if __name__ == "__main__":
    main()

# In[5]:
