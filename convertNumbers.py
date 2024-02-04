"""
convertNumbers.py - Script that converts decimal numbers into binary and hexadecimal style.

This script reads a file containing numeric data, skips the values that are not numbers and then 
converts those numbers to binary and hexadecimal base. It then prints the results on the console 
and creates and a file named ConvertionResults.txt with all the gathered information.
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import time

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
                    int_number = int(stripped_data)
                    data.append(int_number)
                except ValueError:
                    print(f"Warning: {stripped_data} is not a number and "
                          "will not be taken into account")
        return data


# In[3]:


def find_max_bit(data):
    """
    Find maximum number of bits that will be needed for conversions. 
    Use this maximum for all values.
    """
    max_abs = 0
    number_bits = 1
    for number in data:
        abs_value = abs(number)
        if abs_value > max_abs:
            max_abs = abs_value
    max_bit = 1
    while max_bit < max_abs + 1:
        max_bit *= 2
        number_bits = number_bits +1
    max_rem = number_bits % 4
    if max_rem == 0:
        return number_bits
    max_bits = number_bits + (4 - max_rem)
    return max_bits


# In[4]:

def decimal_binary(number, number_bits):
    """
    Converts a decimal number into binary. Uses 2's complement to
    handle negative numbers.
    """
    binary_number = ""
    if number < 0:
        sign = "1"
    else:
        sign = "0"
    number = abs(number)
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number //=2
    while len(binary_number) < number_bits:
        binary_number = '0' + binary_number
    if sign == "1":
        binary_number = "".join("1" if bit == "0" else "0" for bit in binary_number)
        carry = 1
        for i in range(len(binary_number) - 1, -1, -1):
            if carry == 1:
                if binary_number[i] == "0":
                    binary_number = binary_number[:i] + "1" + binary_number[i + 1:]
                    carry = 0
                else:
                    binary_number = binary_number[:i] + "0" + binary_number[i + 1:]
        if carry == 1:
            binary_number = "1" + binary_number
    return binary_number, sign

# In[5]:

def decimal_hexadecimal(binary_number, sign):
    """
    Converts a binary number into hexadecimal. When having a negative number
    it uses 10 digits.
    """
    bin_to_hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex_number = ''
    if binary_number == "0":
        return "0"
    for i in range(0, len(binary_number), 4):
        binary_set = binary_number[i:i+4]
        hex_digit = bin_to_hex_dict[binary_set]
        hex_number += hex_digit
    if sign == "1":
        while len(hex_number) < 10:
            hex_number = 'F' + hex_number
    return hex_number

# In[6]:

def main():
    """
    Main function to execute when the script is run. It converts a decimal to
    a binary number, then takes this result and converts it to a hexadecimal number
    it prints the results in the console and writes then on a file named
    "ConvertionResults"
    """
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    path = sys.argv[1]
    data = open_file(path)
    number_bits = find_max_bit(data)
    conversion_results = []
    for number in data:
        decimal = decimal_binary(number, number_bits)
        hexadecimal = decimal_hexadecimal(decimal[0], decimal[1])
        conversion_results.extend([(number, decimal[0], hexadecimal)])
    print("Results:")
    for index, (decimal, binary, hexadecimal) in enumerate(conversion_results, start=1):
        print(f"{index} Decimal: {decimal}, Binary: {binary}, Hexadecimal: {hexadecimal}")
    time_elapsed = time.time() - start_time
    print(f"Time Elapsed:, {time_elapsed} seconds\n")
    with open("ConvertionResults.txt", 'w', encoding='utf-8') as result_file:
        # Redirect stdout to the file
        sys.stdout = result_file
        print("Results:")
        for index, (decimal, binary, hexadecimal) in enumerate(conversion_results, start=1):
            print(f"{index} Decimal: {decimal}, Binary: {binary}, Hexadecimal: {hexadecimal}")
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()

# In[7]:
