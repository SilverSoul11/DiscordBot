#Needed libraries are requests, os (to open file), and beautiful soup 4. this
#function will get a joke from a specific website and return it as a string.


url = "http://www.textfiles.com/humor/JOKES/badday.txt"

def Jokes(url):
	import requests
	import os
	import bs4
	
	dJoke = requests.get(url)

	#checks for error, if there is no error execution will continue otherwise it
	#will break, save dad joke to a file.

	dJoke.raise_for_status()

	saveFile = open('dadJoke.txt','wb')

	for chunk in dJoke.iter_content(100000):

	        saveFile.write(chunk)
	        
	saveFile.close()