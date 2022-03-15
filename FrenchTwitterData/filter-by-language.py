
#File path of the read csv: CSV-Pract-and-Final-Project-1 > FrenchTwitterData> diacritic-containing-verlan-words > 0–firstscrape.csv


#One Source of FileNotFoundError: 0–firstscrape.csv contains a dash, not a hypthen.

#Another Source of FileNotFoundError: the file path specification with the ~ and the repl name as the apex node malfunctioned, so I resorted to the  file path specification with /home/runner/.

import csv
from csv import DictReader

#Open the csv file in read mode
#with file-opening statement

with open('/home/runner/CSV-Pract-and-Final-Project-1/FrenchTwitterData/common-verlan-words/8–firstscrape.csv','r') as filename:
  reader = csv.DictReader(filename)
  #Data type: The DictReader object is an iterable of the csv.DictReader data type. It is not categorized as dict.
  unfiltered_tweets_count = 0
  filtered_tweets_count = 0
  list_of_French_utterances = []
  for row in reader:
  #Data structure: The DictReader object is an iterable whose elements are row-representing dictionaries wherein the keys are column headers and each values is a csv entry that belongs to both the specified column and the current row.
    #row_dictionary['column header'] outputs the csv value that belongs to both the current row and the referenced column. 
    row_dictionary = row
    if row['lang'] != "fr":
      unfiltered_tweets_count+=1
    elif row['lang'] == "fr":
      unfiltered_tweets_count+=1
      filtered_tweets_count+=1
      #Append the csv value of the current row belonging to the column of interest.
      list_of_French_utterances.append(row_dictionary['content'])
filename.close()

print(list_of_French_utterances)
print(f"The unfiltered tweet count amounts to {unfiltered_tweets_count}.")
print("The filtered tweet count amounts to",filtered_tweets_count,".")



#If time permits, count up the number of tweets.

#def filter-by-language(filename,):
#"""
#This function admits a read csv file, counts the number of tweets in #total, tallies up the number of French tweets, and outputs a processed csv file from which non-French tweets were #winnowed out.
#"""
