#Approach pursued: import a module from pandas

#Step 1: import a module from pandas after installing pandas in bash shell.

from pandas import *

#Step 2: read the data from the csv file

data = read_csv("vowel_and_syllable_counts.csv")

#Commas had to be removed from the strings in the csv in order to properly tokenize the data.

#Step 3: convert the column data to list data

wrd = []
vs = []
ss = []

try:
  wrd = data["word"].tolist()     #wrd abbreviates word
  vs = data["vowels"].tolist()      #vs denotes vowel sounds
  ss = data["syllables"].tolist()  #ss references syllables

except Exception as e:
  print('type is:', e)
else:
  print('No errors detected')
#Step 4: display the list data to the screen

print(f"Words: {wrd}")
print(f"Numbers of vowel sounds: {vs}")
print(f"Numbers of syllables:{ss}")
