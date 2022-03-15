#Three strategies for reading csv columns to lists include the implementation of pandas and the notion of dataframes, implementation of the Dict_Reader function of the csv module, and the implementation of the defaultdict function from a collection of the csv module.

#This file illustrates the strategy that utilizes the DictReader function.


import csv      
from csv import DictReader  #Some other sources may contend that the module name is in all caps like CSV, but this is erroneous.

# Open the csv file in read mode.

#It did not suffice to specify a csv filepath and csv file name in one argument of the open function, prefacing the file path by the tilde (~) and including the repl name as the apex node in the file path on repl.it

filename = open('/home/runner/CSV-Pract-and-Final-Project-1/vowel_and_syllable_counts.csv','r',encoding = 'utf-8')

#Original name of Repl.it:n CSV-Pract-and-Final-Project-1



#Read or translate the opened file into a DictReader object using the DictReader function.

reader = csv.DictReader(filename)

print(type(reader))

#Explore the data structure of the DictReader object.

#for row in reader:
  #print(row) #Output: A dictionary whose elements are representative of csv rows.

#Explore the data structure of the DictReader object & an attempt at converting columns to lists

#for row in reader:
  #print(row['word']) #Output: an array of only the column bearing the column header 'word'
  #print(row['word'],row['vowels'],row['syllables']) #Output: an array of all the columns
  #word_list = row['word']
 # word_list = list(word_list) Output: 'p' 'i' 't' 'h' 'y'

#word_list = []
#vowels_list = []
#syllables_list = []

#for row in reader:
  #row_dictionary = row
  #word_list.append(row_dictionary['word'])
  #vowels_list.append(row_dictionary['vowels'])
  #syllables_list.append(row_dictionary['syllables'])

#print(word_list)
#print(vowels_list)
#print(syllables_list)


#Read only the words whose corresponding values in the number of syllables column is not "?".These are the words whose syllabification is not controversial or contestable.

list_of_words_of_uncontested_syllable_count = []

for row in reader:
  row_dictionary = row
  if row_dictionary['syllables'] != "?": 
    list_of_words_of_uncontested_syllable_count.append(row_dictionary['word'])
  else:
    continue
  
print("Words of uncontested syllabification:", list_of_words_of_uncontested_syllable_count)






