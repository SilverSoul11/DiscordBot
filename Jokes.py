#Needed libraries are requests, os (to open file), and beautiful soup 4. this
#function will get a joke from a specific website and return it as a string.
import requests
import os
import bs4

url = "http://www.textfiles.com/humor/JOKES/badday.txt"

dJoke = requests.get(url)

#checks for error, if there is no error execution will continue otherwise it
#will break, save dad joke to a file.

dJoke.raise_for_status()

saveFile = open('dadJoke.txt','wb')

for chunk in dJoke.iter_content(100000):

        saveFile.write(chunk)
        
saveFile.close()

#def getURLs(url):
    
#Jokes class for taking two jokes and printing them
#class dadJokeC:
 #   def __init__(index, typeJ):
  #      index = self.index()
   #     typeJ = self.typeJ()
        
#   def create(self,index)
