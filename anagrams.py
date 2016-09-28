#!/usr/bin/python

'''Python Program to find all the anagrams in a file on disk with one line per word. 

Example input:
python anagram.py <filename.txt>

Example output:
[emit, item, mite, time]
[merit, miter, mitre, remit, timer]

'''
import argparse
from argparse import RawTextHelpFormatter
import os
import os.path

def findAnagrams(inputFile):

    from collections import defaultdict
    sortedTuple = []
    result = defaultdict(set)

    if os.path.exists(inputFile):
       
        with open(inputFile, 'r') as fobj:
            #Strip the '\n' at the end of each line and store the words as a list
            words = [word.rstrip() for word in fobj.readlines()]
            
            #For each word in the above list, create a list of tuples as (X,Y) 
            #where X = word and Y = the word sorted alphabetically 
            for word in words:
                sortedTuple.append((word, "".join(sorted([char for char in word]))))
            
            #Sort the  list of tuples based on the second parameter i.e the alphabetically sorted word
            #All words that are anagrams would appear next to each other
            sortedTuple.sort(key=lambda x: x[1])
            
            for word, sortedWord in sortedTuple: 
                result[sortedWord].add(word)
            
            #Group the anagrams found and store them in a set ( to remove duplicate entries)
            print "Anagrams found:"
            for k, values in result.items():
                print "{0}".format(list(values))
            
    else:
        print "File not found"    


def main():
	
    parser = argparse.ArgumentParser(description='''Program to find anagrams in a file 
           
     Input: <Filename> 
     Output: List of anagrams found in the file ''', formatter_class=RawTextHelpFormatter)

    parser.add_argument('-f', '--file', type=str, help='Filename to search for anagrams', required=True )

    args = parser.parse_args()
    
    print findAnagrams(args.file)

if __name__ == "__main__":
   main()
