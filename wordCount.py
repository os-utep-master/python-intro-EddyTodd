import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input file> <output file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

# make sure input files exist
if not os.path.exists(inputFname):
    print("input file %s doesn't exist! Exiting")
    exit()

# create dictionary
dic = {}

# read input file
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        words = re.split('\W', line.strip())  # remove line breaks and non alpha characters
        words = [x.lower() for x in words]  # to lower case
        for w in words:
            if w == '':  # ignore empty string
                continue
            elif w in dic:
                dic[w] += 1
            else:
                dic[w] = 1

# print to output file
with open(outputFname, 'w') as outputFile:
    for key, value in sorted(dic.items()):
        outputFile.write(key + ' ' + str(value) + '\n')
