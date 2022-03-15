
#Section 1: Preparation and Setup of the query by text search -- In order to implement or wield the scrapeVerlanTweets.py to garner Tweets from Twitter, install pandas and the snscrape packages in the Repl.it 
#bash shell, not in the python interpreter. The shell defaults to bash mode until "python" is typed in a commandline.
#pip install pandas
#pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

import os
import pandas
#---------------------------
#Setup of the nlp machine-learning model from spaCy
#Installation of the spacy library:
#Type the following in the bash shell
#pip install -U spacy

#Import of modules from spacy and pandas
import spacy
from spacy import displacy
from collections import Counter
#import pandas as pd

#Download the nlp machine-learning model for the language of interest from spacy to the python interpreter.
#Type in the shell/terminal
#python -m spacy download fr_core_news_md


#Load the nlp machine-learning model to the program and store it in a variable nlp.
nlp = spacy.load('fr_core_news_md')
#no success with the nlp machine-learning model fr_core_news_lg

#--------------------------

#Tweets_attesting_to_La_Haine_verlan_words = []                                                                       
#Tweets_attesting_to_Pattaya_verlan_words = []

#Query Twitter by text search
#Define the variables that will medisate the formatting of the search command. Such variables serve as search parameters of the search command.

tweet_count = 1000
#We can adjust the max number of tweets garnered later.
start_date = "2022-02-27"
end_date = "2022-02-28"

#Section 2: Conduct a for loop iterating through all the words in a word list, and for each word, search for tweets that feature a pattern containing that word in order to create a json file. First, define the search parameters of the format function in the search command.



La_Haine_verlan_words_list_0 = ["rebeu", "Rebeu", "keufs", "Keufs", "keum", "Keum", "kiffer", "Kiffer", "oinj", "Oinj","reuch", "Reuch", "reus", "Reus", "zicmu", "Zicmu","ramer", "Ramer", "tune", "Tune", "thune", "Thune", "tchatcher","Tchatcher", "pote", "Pote", "frangin", "Frangin", "flamber","Flamber", "fripes", "Fripes", "taf", "Taf", "boulot", "Boulot", "bosser", "Bosser", "saoler", "Saoler","bled", "Bled", "bouquin", "Bouquin", "taule", "Taule", "flingue", "Flingue","buter","Buter"]



La_Haine_verlan_words_string_0 = "rebeu Rebeu keufs Keufs keum Keum kiffer Kiffer oinj Oinj reuch Reuch reus Reus zicmu Zicmu blème Blème galère Galère ramer Ramer tune Tune thune Thune tchatcher Tchatcher pote Pote frangin Frangin pétard Pétard flamber Flamber sapé Sapé branché Branché fripes Fripes taf Taf boulot Boulot bosser Bosser saoler Saoler bled Bled bouquin Bouquin taule Taule flingue Flingue buter Buter"

Pattaya_verlan_words_list_0 = ["ken", "Ken", "caille", "Caille", "tej","Tej", "teub", "Teub", "segros", "Segros", "relou", "Relou", "queurblo", "Querblo", "demer", "Demer", "teshor", "Teshor"]
                             
Pattaya_verlan_words_string_0 = "ken Ken kaïra Kaïra kénn Kénn caille Caille tej Tej teub Teub segros Segros relou Relou teubé Teubé queurblo Querblo demer Demer teshor Teshor"

#Trial-and-error history

#*Value error: unexpected character encountered when decoding array value (2)
#-- incurred when string of verlan words with diacritics was word-tokenized
#--same error incurred when a string without diacritic-bearing words was word-tokenized
#--same error incurred when inputting a list of verlan words with diacritics
#--The actual source of the error was the lack of the csv file name as a positional argument.
#-- We then reverted back to the sophisticated program that feeds the nlp processed Verlan lists to the scraper.


#*The search strings "rebeu" and "Rebeu" yield the results, each one extracting both the lower case-initial version and the upper case-initial version, so the "Rebeu", just as any other capitalized search, is superfluous. The capitalized versions of words were deleted. Also, the url column should be jettisoned from the csv since the scraper might garner Twitter urls, instead of actual tweets, that feature the search pattern. 

#--Reintroduce diacritic-containing words back into La_Haine_verlan_words_string and Pattaya_verlan_words_string.

#2022-02-27 23:36:27+00:00,"Je dois l’admettre, ce que propose le Barça c’est joli",1498079613263781888,https://twitter.com/Rebeu_07/status/1498079613263781888,fr

#

La_Haine_verlan_words_string = "rebeu keufs keum kiffer oinj reuch reus zicmu blème galère ramer tune thune tchatcher pote frangin pétard flamber sapé branché fripes taf boulot bosser saoler bled bouquin taule flingue buter"


Pattaya_verlan_words_string = "ken kaïra kénn caille tej teub segros relou teubé queurblo demer teshor"

#------Word Tokenization by the trained pipeline (i.e., the nlp machine-learning model)-------

La_Haine_verlan_words = nlp(La_Haine_verlan_words_string)
Pattaya_verlan_words = nlp(Pattaya_verlan_words_string)

#Guarantee that the outputs of nlp are word-tokenized lists.

La_Haine_verlan_words = list(La_Haine_verlan_words)
Pattaya_verlan_words = list(Pattaya_verlan_words)


#Ensure that the members, elements, or items of the word-tokenized lists are strings

for i in range(len(La_Haine_verlan_words)):
  La_Haine_verlan_words[i] = str(La_Haine_verlan_words[i])

#Remark: Lists are mutable, so list indices can be reassigned new values.
  
for j in range(len(Pattaya_verlan_words)):
  Pattaya_verlan_words[j] = str(Pattaya_verlan_words[j])
#-----------------------------------------------------------------------------------------------


count = 0

for word in La_Haine_verlan_words:
  #CKH: Search for tweets that feature the word that aligns with the current value of our looping variable.
  search_string1 = '\"'+word+'\"'
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'>Tweets_attesting_to_La_Haine_verlan_words.json".format(tweet_count,start_date, search_string1, end_date, count))
#CKH: Construct a dataframe that organizes the metadata and contents of tweets that feature each Verlan word characteristic of La Haine.
   
#Section 3: Construct a portion of the dataframe from the .json file. The dataframe should be organized into a column carrying numerical and alphabetic tags indicative
#of metadata of the Tweets and a column carrying the content of the Tweets. We remain in the for loop.
  La_Haine_dataframe = pandas.read_json("Tweets_attesting_to_La_Haine_verlan_words.json",'{}–firstscrape.json'.format(count), lines = True)
                                        
#Section 4: Apply the .head() method or .tail() method to display the first five entries of the dataframe or the final five entries of the dataframe, respectively.
  #first_five_tweets_attesting_to_La_Haine_verlan_words = La_Haine_dataframe.head()
  #final_five_tweets_attesting_to_La_Haine_verlan_words = La_Haine_dataframe.tail()
  #print(first_five_tweets_attesting_to_La_Haine_verlan_words)
  #print(final_five_tweets_attesting_to_La_Haine_verlan_words)

  #The issue was the lack of a positional argument of the read_json function. It needed a file name to read.
  
#Section 5: Export or transfer the newly scraped Verlan data to a csv file, and print to the screen the number of utterances collected at each step.
  #CKH: Tweets Attesting to La Haine Words
  if len(La_Haine_dataframe) == 0:
    print("Tweet Count of ", search_string1, "in La_Haine_dataframe : 0")
  else:
    La_Haine_dataframe.to_csv('{}–firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id','lang'])
  print("Tweet Count of ", search_string1, "in La_Haine_dataframe : ", str(len(La_Haine_dataframe)))
  count = count+1

count = 0

for word in Pattaya_verlan_words:
  #CKH: search for tweets that feature the word
  search_string2 = '\"'+word+'\"'
  #CKH: Construct a dataframe that oranizes the metadata and contents of tweets that feature each Verlan word typical of Pattaya.
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'>   Tweets_attesting_to_Pattaya_verlan_words.json".format(tweet_count,start_date,search_string2,end_date, count))
   
#Section 3: Construct a dataframe from the .json file. The dataframe should be organized into a column carrying number tags indicative
#of metadata of the Tweets and a column carrying the content of the Tweets. We remain in the for loop.
  Pattaya_dataframe = pandas.read_json("Tweets_attesting_to_Pattaya_verlan_words.json",'{}–firstscrape.json'.format(count), lines=True)
             
#Section 4: Apply the .head() method or .tail() method to display the first five entries of the dataframe or the final five entries of the dataframe, respectively.
  #first_five_tweets_attesting_to_Pattaya_verlan_words = Pattaya_dataframe.head()
  #final_five_tweets_attesting_to_Pattaya_verlan_words= Pattaya_dataframe.tail()
  #print(first_five_tweets_attesting_to_Pattaya_verlan_words)
  #print(final_five_tweets_attesting_to_Pattaya_verlan_words)
  
#Section 5: Export or transfer the newly scraped Verlan data to a csv file, and print to the screen the number of utterances collected at each step.
  
  if len(Pattaya_dataframe) == 0:
    print("Tweet Count of ", search_string2, "in Pattaya_dataframe : 0")
  else:
    Pattaya_dataframe.to_csv('{}–firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id','lang'])
  print("Tweet Count of", search_string2, "in Pattaya_dataframe : ", str(len(Pattaya_dataframe)))
  count = count + 1

  #*In the updated scrape tweets, are the if-else blocks nested in the for loop because the construction of the dataframe transpires one chunk at a time after each query for a word in a wordlist rather than having the dataframe be synthesized in one fell swoop?

#How can the file path and file name of the exported csv be specified in the updated  scrapeTweets.py?

#Add a positional argument before {}-firstscrape


#Is there an argument of the to_csv function in which the file name of the exported csv can be specified when also inserting the {}-firstscrape argument?

#a futile attempt: 
# La_Haine_dataframe.to_csv('Tweets_attesting_to_La_Haine_verlan_words.csv','{}–firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id', 'url','lang'])
# Pattaya_dataframe.to_csv('Tweets_attesting_to_Pattaya_verlan_words.csv','{}–firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id','lang'])

#How can the csv files outputted from a scrapeTweets program that constructs one portion of the dataframe for each word in the wordlist be collated into a single csv file?


