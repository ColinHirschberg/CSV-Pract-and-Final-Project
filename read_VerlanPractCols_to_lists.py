#Approach Pursued: Installed pandas prior to importing a module from pandas

#Step 1: Install pandas in the bash shell, not the Python interpreter, prior to importing * from pandas.

from pandas import *

#Step 2: Read the data from the csv file.

data_frame = read_csv("VerlanPract.csv")

print(data_frame)

#Step 3: Convert the column data to list data.

list_1 = []
list_2 = []

list_1 = data_frame['NumberTag'].tolist()
list_2 = data_frame['SearchHit'].tolist()

#Step 4: Print the list data.

print(f"Number tags: {list_1}")
print(f"Search hits: {list_2}")

