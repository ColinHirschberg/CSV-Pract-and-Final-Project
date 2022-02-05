#Approach Pursued: import csv module and implement the DictReader() to parse the data of the columns

import csv

filename = open('vowel_and_syllable_counts.csv','r')

file = csv.DictReader(filename)

words = []
numbers_of_vowels = []
numbers_of_syllables = []


for row in file:
  words.append(row["word"])
  numbers_of_vowels.append(row["vowels"])
  numbers_of_syllables.append(row["syllables"])

print(f'word:{words}')
print(f'number of vowels sounds:{numbers_of_vowels}')
print(f'number of syllables:{numbers_of_syllables}')