#Tess Porter
#April 5, 2018
#CS 172 Section 68

import math

from spellchecker import spellchecker

def get_file(question):
    print('Welcome to Text File Spellchecker.')
    valid = True
    while valid:
        try:
            filename = input(question)
            open(filename, 'r')
            valid = False
        except OSError:
            print ('Could not open file.')
            valid = True           
    return filename
                    
file = get_file('Enter the name of the file to read:\n')

f = open(file, 'r')
fail = 0
num_lines = 0
num_words = 0
sc = spellchecker('english_words.txt')

for line in f:
    num_lines += 1
    for word in line.split():
        num_words += 1
        if not spellchecker.check(sc, word):
            print('Possible spelling error on line', num_lines, ':', word)
            fail += 1

print(num_words - fail, 'words passed spell checker')
print(fail, 'word failed spell checker.')

percent = ((num_words - fail)/num_words) * 100
print('%.2f%% of the words passed.' %(percent))
            
        