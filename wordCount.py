"""
wordCount.py - Script that counts the number of occurrences of word on a file

This script reads a file containing words, skips the values that are not words (or just letters)
It then prints the results on the console and creates and a file named "WordCountResults.txt" 
with all the gathered information.
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import time

# In[2]:


def open_file(path):
    """
    Open and read numeric data from a file. It also anlyze each value to confirm if it is a word
    if it is not, then it displays an error and skips it.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = []
        for line in file.readlines():
            stripped_data = line.strip()
            if stripped_data and stripped_data.isalpha():
                data.append(stripped_data)
            else:
                print(f"Warning: {stripped_data} is not a word and "
                      "will not be taken into account")
        return data


# In[3]:

def count_occurrences(words, target_word):
    """
    Counts the number of occurrences of a word in an array. It then
    deletes those words so that they are not taken into account the
    next time it rans.
    """
    count = 0
    i = 0

    while i < len(words):
        if target_word == words[i]:
            count += 1
            del words[i]
        else:
            i += 1

    return count

# In[4]:

def main():
    """
    Main function to execute when the script is run. It counts the individual occurrences
    of the words in the file, then it prints the results in the console and writes them in
    a file called "WordCountResults.txt".
    """
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    path = sys.argv[1]
    data = open_file(path)
    occurrences = {}
    while data:
        current_word = data[0]
        count = count_occurrences(data, current_word)
        occurrences[current_word] = count
        data = data[1:]
    print("Results:")
    for index, (word, count) in enumerate(occurrences.items(), start=1):
        print(f"{index} Word: {word}, Occurrences: {count}")
    time_elapsed = time.time() - start_time
    print(f"Time Elapsed:, {time_elapsed} seconds\n")
    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        # Redirect stdout to the file
        sys.stdout = result_file
        print("Results:")
        for index, (word, count) in enumerate(occurrences.items(), start=1):
            print(f"{index} Word: {word}, Occurrences: {count}")
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()

# In[5]:
