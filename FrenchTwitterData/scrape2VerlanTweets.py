#This program garners tweets from Twitter that feature occurrences of Verlan words in common between the French films La Haine (1995) and Pattaya (2016). This list is titled common_Verlan_words. This will evaluate whether Pattaya served to refresh the La Haine-popularized Verlan words.

#Step 1: Preparation and setup of the query by text search

#Import of modules

import pandas
import os

#In order to implement the scrape2VerlanTweets.py, install pandas and the snscrape packages in the bash shell, not in the python interpreter. 

#Type into the bash shell:
#pip install pandas
#pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

#Define the variables that will format the search command. These become search parameters of the .format() function

#Establish search_string1 after processing by the nlp machine-learning model from spacy.

tweet_count = "1000"
start_date = "2022-02-27"
end_date = "2022-02-28"

#Note: béflan is not shared in common between Pattaya and La Haine. It is exclusively found in La Haine.

common_verlan_words_string = "béflan caillera meuf ouf chelou renoi vénère teuf pécho"


#-------Spawning a Spacy-Processed List of Words---------------------------------------

#Step 1: Install spaCy and pandas in the bash shell, not in the python interpreter.

#Type into the bash shell the following:
#pip install -U spacy

#Step 2: Import modules from the spacy and pandas libraries

import spacy
from spacy import displacy
from collections import Counter
#import pandas as pd

#Step 3: Download the nlp machine-learning model for French from spaCy into the python interpreter.

#Type into the bash shell the following:

#python -m spacy download fr_core_news_md

#Step 4: Load the nlp machine-learning model for French to the program, and save it to the variable name nlp.

nlp = spacy.load('fr_core_news_md')


#Step 5: Applying the nlp function to a string to word-tokenize it. 

document = nlp(common_verlan_words_string)

#Then ensure that the word-tokenized text outputtted of the nlp function is of the list data type.

document = list(document)

#Guarantee that every token of the word-tokenized list is a string.

for token in document:
  token = str(token)
  
#output: the list titled common_Verlan_words 
common_verlan_words = document

print(common_verlan_words)


#---------------------------------------------------------------------------------------

#Step 2: Conduct a for loop iterating through the words in a word list, and for each word in the word list, search for tweets that feature a pattern containing that word to create a json file.

#Initialize a counter at zero to later keep track of the current index of the word list.

count = 0

for word in common_verlan_words:
  #Reinforce that the tokens of the word-tokenized list outputted from spacy are strings.
  word = str(word)
  search_string1 = '\"'+word+'\"'
  #'\"' signals to python to interpret " as a string element rather than as a special character.
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'>common_verlan_words.json".format(tweet_count,start_date, search_string1, end_date, count))

  #Step 3: Construct a dataframe from the json file.
  common_verlan_words_dataframe = pandas.read_json("common_verlan_words.json",'{}–firstscrape.json'.format(count), lines = True)

  #Step 4: Optionally apply the .head() or .tail() method to the dataframe to display the first five entries or final five entries of the dataframe to the shell window.
  #common_verlan_words_dataframe.head()
  #common_verlan_words_dataframe.tail()

  #Step 5: Export the dataframe of tweets and other columns of metadata to a csv file – or a succession of csv files that each bundle or package together the tweets for a particular word, in this case – and print the number of utterances collected at each step.
  if len(common_verlan_words_dataframe) == 0:
    print("Tweet Count of ", search_string1, "in Pattaya_dataframe : 0")
  else:
    common_verlan_words_dataframe.to_csv('{}–firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id','lang'])
  print("Tweet Count of", search_string1, "in Pattaya_dataframe : ", str(len(common_verlan_words_dataframe)))
#Increment the counter prior to proceeding to the next search word.
  count+=1
  
  