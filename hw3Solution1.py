#Alexander Starr
#22C:016:A01
#00567613

# Parses a line and extracts words from the line into a list. Any word that is
# extracted needs to be at least 4 letters long. Also, all extracted words are
# converted into all-lower-case before being inserted into the list.
def parse(s):
    listOfWords = [] # maintains the list of words in strings s
    currentWord = ""
    
    wordBeingProcessed = False
    
    i = 0 # serves as an index into the string s
    while i < len(s):
        # if the current character is a lower case letter
        if (s[i] >= "a" and s[i] <= "z"): 
            wordBeingProcessed = True
            currentWord = currentWord + s[i]
        # if the current character is an upper case character
        # do the same as above, except convert character into corresponding
        # lower case character using the ord() and chr() functions
        elif (s[i] >= "A" and s[i] <= "Z"):
            wordBeingProcessed = True
            currentWord = currentWord + chr(ord("a") + ord(s[i]) - ord("A"))
        # else if the current character is a non-letter
        # immediately following a word
        elif wordBeingProcessed:
            if len(currentWord) >= 4:
                listOfWords.append(currentWord)
            wordBeingProcessed = False
            currentWord = ""
        i = i + 1
            
    return listOfWords

# Searches for a word in wordList and returns the index of the first occurrence
# of word in wordList if found; otherwise returns -1.
def getIndex(wordList, word):
    index = 0
    while index < len(wordList):
        if wordList[index] == word:
            return index
        index = index + 1
    return -1

# Takes a filename as parameter and parses the file, extracts words from the file
# and constructs two lists: one containing the words in the file and the other
# containing corresponding word-frequencies.
# In addition it, tracks the total number of words used, and the number of
# repeated words.
def computeFrequencies(filename):
    f = open(filename, "r")
    line = f.readline()
    masterList = [] # for maintaining the list of words
    frequencies = [] # for maintaining frequencies of these words
    total_words = 0
    num_repeats = 0
    while line:
        wordsInLine = parse(line) # parse the current line to extract words
 
        index = 0
        while index < len(wordsInLine):
            # if word is already in masterList, increase its frequency
            loc = getIndex(masterList, wordsInLine[index])
            if loc >= 0:
                frequencies[loc] = frequencies[loc] + 1
            else: # this is the first occurrence of the word, so just append
                  # and set frequency to be 1
                masterList.append(wordsInLine[index])
                frequencies.append(1)
            index = index + 1
            total_words = total_words + 1
        line = f.readline()

    f.close()
    num_repeats = total_words - len(masterList)
    # The number of words which are repeats is simply the total number of words
    # minus the number of unique words (which is the same as len(masterList))
    percent_repeat = float(num_repeats) / total_words * 100
    print "Total number of words:", total_words
    #print "Number of repeats:", num_repeats # Debug statement
    print "Percent repeats:", percent_repeat
    return [masterList, frequencies]

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

# Finds and returns the index of the word with maximum frequency in 
# the range L[lowerBound..len(L)-1]
def maxIndex(L, lowerBound):
    maxElement = L[lowerBound]
    indexOfMax = lowerBound
    index = lowerBound + 1

    while index < len(L):
        if L[index] > maxElement:
            maxElement = L[index]
            indexOfMax = index
            
        index = index + 1

    return indexOfMax

# Uses a truncated version of selection sort to bring the most frequent
# k words to the front of the list. 
def mostFrequentWords(wordList, frequencyList, k):
    n = len(wordList)
    index = 0

    while index < k:
        # Finds the index of a most frequent word in the range [index..n-1]
        m = maxIndex(frequencyList, index)

        # Bring this most frequent word to the "front" by swapping wordList[m] and
        # wordList[index] and also corresponding frequencies
        swap(wordList,index, m)
        swap(frequencyList,index, m)

        index = index + 1

# Merges two word and frequency lists
def merge(wL1, f1, wL2, f2):
    index = 0
    # Walk through the words in wL2 
    while index < len(wL2):
        loc = getIndex(wL1, wL2[index])
        if loc == -1: # the word wL2[index] is not in wL1
            wL1.append(wL2[index])
            f1.append(f2[index])
        else: # the word wL2[index] is already in wL1
            f1[loc] = f1[loc] + f2[index]
        index = index + 1
        
    return [wL1, f1] # the merged lists
            
# Prints the words in wordList in positions 0, 1,..., upperBound-1
def printPrefix(wordList, upperBound):
    index = 0
    while index < upperBound:
        print wordList[index]
        index = index + 1

# main program
# The main program has been commented out for this problem

# First deal with War and Peace
#[wordList, frequencies] = computeFrequencies("war.txt")
#mostFrequentWords(wordList, frequencies, 20)
#print "Tolstoy"
#printPrefix(wordList, 20)

# And then with Jekyl, Hyde, and the treasure island
#[wordList1, frequencies1] = computeFrequencies("hyde.txt")
#[wordList2, frequencies2] = computeFrequencies("treasure.txt")
#[wordList, frequencies] = merge(wordList1, frequencies1, wordList2, frequencies2)
#mostFrequentWords(wordList, frequencies, 20)
#print "R.L.Stevenson"
#printPrefix(wordList, 20)