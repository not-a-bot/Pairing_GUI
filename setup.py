try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'code for the pairing process',
    'author': 'Open Ears',
    'url': 'URL',
    #'download_url': 'Where to download it.',
    'version': '0.9',
    'install_requires': ['nose', 'gspread', 'time', 'json',
						 'oauth2client', 'os', 'web'],
    #folder named NAME in the basic folder
	'packages': ['OPEN'],
    'name': 'Pairing Services'

}

setup(**config)
