import googletrans

'''takes input text and translates it into russian'''
def trans(text):
	try:
		if text.isinstance(text, str):
			translator = googletrans.Translator()
			translator.translate(text)