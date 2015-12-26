def LOAD(path_to_secret_file):
	import json
	import gspread
	from oauth2client.client import SignedJwtAssertionCredentials

	#this is loading your key given to you by THE google
	json_key = json.load(open(path_to_secret_file))
	#your not supposed to store this publicly,
	#im not sure how to get around putting this...
	#oh, ill just store it in the cloud somewhere,
	#maybe



	#This is the webpage that the api will find the sheets from. The
	#sheets must be shared with the 'client_email' that is 
	scope = ['https://spreadsheets.google.com/feeds']

	#gives you credientials to acess the url with the given key and your email
	#since im using python2.7 i might not need to encode the key. yup.
	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

	#REMEMBER to share all needed sheets with whatever recorded
	#as your 'client_email'
	#SUCCESS!

	#AUTHORIZE!
	gc = gspread.authorize(credentials)

	return gc
