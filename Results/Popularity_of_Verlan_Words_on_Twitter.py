#Importation of modules
import mathplotlib.pyplot as plt
import numpy as np

def bar_chart(La_Haine_count, Pattaya_count, common_count):
  np.array([1,2,3]) #Establishment or setup of the number of bars in the array.
  labels = ["Tweets Echoing La Haine Words","Tweets Echoing Pattaya Words","Tweets with Common Words"] #the names of the independent variables
  La_Haine_bar = np.array(La_Haine_count[0])#Formatting of values to be visually illustrated by bars
  Pattaya_bar = np.array(Pattaya_count[0]) 
  Common_words_bar = np.array(common_count[0])
  #Define color coding to paint in the bars and to prepare for a legend/key. #In this case red signifies the number of tweets echoing La Haine words, blue signifies the
  p1 = plt.bar(left, La_Haine_bar, color = "red")
  p2 = plt.bar(left, Pattaya_bar, color = "blue")
  p3 = plt.bar(left, Common_words_bar, color = "purple")
  plt.legend((p1[0],p2[0],p3[0]),("La Haine","Pattaya","Common"))
  plt.ylabel("Count")
  plt.title("Popularity of Two Film's Verlan Words on Twitter in 2022")
  plt.show()

  
  