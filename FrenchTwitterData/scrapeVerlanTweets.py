
#Section 1: In order to implement or wield the scrapeVerlanTweets.py to garner Tweets from Twitter, install pandas and the snscrape packages in the Repl.it 
#bash shell, not in the python interpreter. The shell defaults to bash mode until "python" is typed in a commandline.
#pip install pandas
#pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

import os
import pandas

#Query Twitter by text search
#Set the variables that will facilitate the formatting of the search command.

La_Haine_verlan_words = []
Pattaya_verlan_words = []
tweet_count = 1000
#We can augment the max number of tweets garnered later.
start_date = "2022-02-27"
end_date = "2022-02-28"

#Section 2: Iterate through a list of verlan words typical of La Haine and a list of verlan words characteristic of Pattaya, 
#and for each verlan word detected, prepare to integrate the tweet featuring the verlan word into the list allocated for storing Tweets that manifest verlan words 
#of particular movie.

Tweets_attesting_to_La_Haine_verlan_words = []                                                                                    
Tweets_attesting_to_Pattaya_verlan_words = []

for word in La_Haine_verlan_words:
  #Search for tweets that feature the word that aligns with the current value of our looping variable.
  search_string1 = '/"'+word+'/"'
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> Tweets_attesting_to_La_Haine_verlan_words.json".format(tweet_count,start_date, search_string1, end_date)
  #Construct a dataframe that organizes the metadata and contents of tweets that feature each Verlan word characteristic of La Haine.
  
            
#Section 3: Construct a dataframe from the .json file. The dataframe should be organized into a column carrying number tags indicative
#of metadata of the Tweets and a column carrying the content of the Tweets. We remain in the for loop.
  La_Haine_dataframe = pandas.read_json("Tweets_attesting_to_La_Haine_verlan_words.json", lines = True)
                                        
#Section 4: Apply the .head() method or .tail() method to display the first five entries of the dataframe or the final five entries of the dataframe, respectively.
  first_five_tweets_attesting_to_La_Haine_verlan_words = La_Haine_dataframe.head()
  final_five_tweets_attesting_to_La_Haine_verlan_words = La_Haine_dataframe.tail()
  print(first_five_tweets_attesting_to_La_Haine_verlan_words)
  print(final_five_tweets_attesting_to_La_Haine_verlan_words)


for word in Pattaya_verlan_words:
  #search for tweets that feature the word
   search_string2 = '\"'+word+'\"'
  #Construct a dataframe that oranizes the metadata and contents of tweets that feature each Verlan word typical of Pattaya.
   os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> Tweets_attesting_to_Pattaya_verlan_words.json".format(tweet_count,start_date,search_string2,end_date)
   
#Section 3: Construct a dataframe from the .json file. The dataframe should be organized into a column carrying number tags indicative
#of metadata of the Tweets and a column carrying the content of the Tweets. We remain in the for loop.
   Pattaya_dataframe = pandas.read_json("Tweets_attesting_to_Pattaya_verlan_words.json", lines = True)
             
#Section 4: Apply the .head() method or .tail() method to display the first five entries of the dataframe or the final five entries of the dataframe, respectively.
  first_five_tweets_attesting_to_Pattaya_verlan_words = Pattaya_dataframe.head()
  final_five_tweets_attesting_to_Pattaya_verlan_words= Pattaya_dataframe.tail()
  print(first_five_tweets_attesting_to_Pattaya_verlan_words)
  print(final_five_tweets_attesting_to_Pattaya_verlan_words)
             
#Section 5: Export or transfer the newly scraped Verlan data to a csv file, and print to the screen the number of utterances collected.
  #Tweets Attesting to La Haine Words
  if len(La_Haine_dataframe) == 0:
    print("Tweet Count of ", search_string1, " : 0")
  else:
    La_Haine_dataframe.to_csv('La-Haine-tweets.csv', sep=',', index=False, columns=['date', 'content', 'id', 'url'])
    print("Tweet Count of ", search_string1, " : ", str(len(search_string1)))
  #Tweets Attesting to Pattaya Words
  if len(Pattaya_dataframe) == 0:
    print("Tweet Count of ", search_string2, " : 0")
  else:
    Pattaya_dataframe.to_csv('Pattaya-tweets.csv', sep=',', index=False, columns=['date', 'content', 'id', 'url'])
    print("Tweet Count of ", search_string2, " : ", str(len(search_string2)))
