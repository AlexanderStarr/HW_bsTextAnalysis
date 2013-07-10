#Alexander Starr
#22C:016:A01
#00567613

from hw3Solution1 import parse
from binarySearch2 import binarySearch
import time

def computeFrequencies1(filename):
    # Takes a string called 'filename' and reads from a file of that name.
    # Returns a list 'L', consisting of two lists.
    # L[0] is the list of all distinct, lowercase words of length at least 4.
    # L[1] is the list of corresponding frequencies of these words.
    f = open(filename, "r")
    distinct_words = []
    occurrences = []
    line = f.readline()
    while line:
        # While 'line' is non-empty, the line is first parsed into a list.
        # Then each word in the list is checked against 'distinct_words'
        # If the word is not in 'distinct_words', then it is added and...
        # the number of occurrences for that word is set to 1.
        # Note that the index of each word is the same as the index of...
        # its corresponding number of occurrences.
        words_in_line = parse(line)
        #print words_in_line     #Debugging print statement.
        index = 0
        while index < len(words_in_line):
            word = words_in_line[index]
            if word not in distinct_words:
                distinct_words.append(word)
                occurrences.append(1)
                # If the word is not unique, then the index for that word...
                # is used to add 1 to the number of occurrences with the
                # corresponding index.
            else:
                word_index = distinct_words.index(word)
                occurrences[word_index] = occurrences[word_index] + 1
            index = index + 1
        line = f.readline()
    f.close()
    L = [distinct_words, occurrences]
    return L

def computeFrequencies2(filename):
    f = open(filename, "r")
    line = f.readline()
    masterList = [] # for maintaining the list of words
    frequencies = [] # for maintaining frequencies of these words
    while line:
        wordsInLine = parse(line) # parse the current line to extract words
        index = 0
        while index < len(wordsInLine):
            # if word is already in masterList, increase its frequency
            loc = binarySearch(masterList, wordsInLine[index])
            if loc >= len(masterList) or masterList[loc] != wordsInLine[index]: 
                # This is the first occurrence of the word, so insert the
                # word and a count of 1 at the proper locations.
                masterList.insert(loc, wordsInLine[index])
                frequencies.insert(loc, 1)
            else: 
                # If the element in masterList at the location returned from
                # binarySearch is the same as the element that was searched for
                # (wordsInLine[index]), then simply increment the corresponding
                # frequency at the given location.
                frequencies[loc] = frequencies[loc] + 1
            index = index + 1
        line = f.readline()

    f.close()
    return [masterList, frequencies]

# First we time and print the time of the first function
t1 = time.time()
computeFrequencies1("war.txt")
t2 = time.time()
print t2 - t1

# Next we time and print the time of the second function
t1 = time.time()
computeFrequencies2("war.txt")
t2 = time.time()
print t2 - t1