#Section 1


#-----We are opting out of the obtainment of the Verlan Lists from Text Files---------------------

#La_Haine_verlan_words = []
#Pattaya_verlan_words = []

#Equality file-opening statements

#Open the file in read mode and under the Unicode as the encoding style specification.

#In specifying a file path, we do not need to ascend to the apex of the file tree because the script program that reads txt files  and the txt files are situated in the same local environment.

#file1 = open(r"La_Haine_verlan_words.txt","r",encoding = 'utf-8')

#string_1 = file1.read()

#La_Haine_verlan_words = string_1.split()

#file1.close()

#file2 = open(r"Pattaya_verlan_words.txt","r",encoding = 'utf-8')

#string_2 = file2.read()

#Pattaya_verlan_words = string_2.split()

#file2.close()

#-------End of Manipulation of Verlan Text Files------

#------onset_of_accented_words_assessement------------------------------------------

#accented_words = "Coéquipier après entrée"

#nlp-processed_accented_words = nlp(accented_words)
#nlp-processed_accented_words = list(nlp-processed_accented_words)

#for word in nlp-processed_accented_words:
#Conduct a for loop iterating over the accented words, and for each accented word, scour Twitter for tweets that feature an appearance of that accented word to create a json file.
  #search_string1 = '/"'+word+'/"'
#os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'>accented_word_tweets.json".format(tweet_count,start_date,search_string1,end_date))

# Read the json file into a dataframe
  #accented_words_dataframe = pandas.read_json("accented_words.json", lines = True)
  
#Optionally display the first five or last five entries of the dataframe by applying the .head() method or .tail() method, respectively

  
#CExport or transfer the newly scraped data to a dataframe.
  #accented_words_dataframe.to_csv('accented-words-tweets.csv', sep=',', index=False, columns=['date', 'content', 'id', 'url'])

#-------------conclusion_of_accented_words_assessment-----------


#-----Display the json file to assess how its lines can be word-tokenized by nlp.

#Reconnaissance info from the display: Each line in the json file is a dictionary wherein keys are column headers or labels indicative of type of metadata (e.g., "_type", "url", "date", "content")
  
#import json

#json_string = open('accented_word_tweets.json', 'r', encoding = 'utf-8')

#json_string = str(json_string)

#json_dict = json.loads(json_string)

#for tweet in sorted(json_dict, key=json_dict.get, reverse = False):
  #print(tweet,":", json_dict[tweet])

#json_string.loads() admits a json string and repurposes it json dictionary.

#file1.close()

#accented_word_contents = []

#Access the tweet from the entry of each json dictionary via the key "content." Specify unicode as the encoding style

#file2 = open('accent_word_tweets.txt','w',encoding = 'utf-8')

#.writelines(L) writes a list of newline character-separated strings to a file.

#file2.writelines(accented_word_contents)               

#file2.close()


#----------conclusion of attempt to read json strings to dictionaries------------