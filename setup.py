try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'code for the pairing process',
    'author': 'John Doherty',
    'url': 'URL',
    #'download_url': 'Where to download it.',
    'version': '0.1',
    'install_requires': ['nose', 'gspread', 'time', 'oauth2client'],
    #folder named NAME in the basic folder
	'packages': ['OPEN'],
    'name': 'Open Ears'

}

setup(**config)
