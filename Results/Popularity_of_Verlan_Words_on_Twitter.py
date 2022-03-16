#Installation of libraries

#In order to import matplotlib, install the the matplot library in the bash shell, not in the python interpreter.

#Type into a commandline of the shell/terminal the following:
#(!)pip install matplotlib
#Include the exclamation mark ! only in Google Colab


#Importation of modules
import matplotlib.pyplot as plt; plt.rcdefaults() #The program malfunctions if you type matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

def bar_chart(La_Haine_count, Pattaya_count, common_count):
  objects = ("La Haine Words", "Pattaya Words", "Common Words") #Independent variables
  y_pos = np.arange(len(objects))
  average_frequency = [La_Haine_count, Pattaya_count, common_count] #Dependent variables

  plt.bar(y_pos, average_frequency, align = 'edge', alpha=0.25)
  plt.xticks(y_pos, objects)
  plt.ylabel('Average Tweet Count')
  plt.title("The Percolation of French Film's Verlan Words into Tweets")
  plt.show()
 
bar_chart(188,119,278)
  
  