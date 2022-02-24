#Step 1: Install pandas in the bash shell, not the python interpreter, prior to importing the * module from pandas.

from pandas import *

#Step 2: Read the column data into a dataframe with the read_csv function.

dataframe = read_csv("FrenchWeb2017Top1000Words.csv")

#Step 3: Convert the column data to list data.

word_types = dataframe["Item"].tolist()
word_counts = dataframe["Frequency"].tolist()

#Step 4: Print the list data.

print(word_counts)
print(word_types)
