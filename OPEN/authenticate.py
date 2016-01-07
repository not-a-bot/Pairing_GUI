# Loads the authentication information and authorizes it with google
#
# All spreadsheets that are to be used must be shared with 
#		open-service@pairing-gui.iam.gserviceaccount.com
def LOAD(path_to_secret_file):
	import json
	import gspread
	from oauth2client.client import SignedJwtAssertionCredentials

	# Load authentication information stored as a json file
	json_key = json.load(open(path_to_secret_file))

	# website API finds the sheets from
	scope = ['https://spreadsheets.google.com/feeds']

	# retrieve credentials from the scope, client_email, and private key
	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

	# authorize gspread using the credentials
	gc = gspread.authorize(credentials)

	return gc
