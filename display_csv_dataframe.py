
#Simplest strategy to display the csv dataframe to the screen.

#Rudimentary Procedure
import pandas as pd
df = pd.read_csv("vowel_and_syllable_counts.csv")
print(df)

#Procedure for Displaying a Subset of Columns
#Insert the usecols() optional argument
dataframe = pd.read_csv("vowel_and_syllable_counts.csv",usecols = [""])
print(dataframe)