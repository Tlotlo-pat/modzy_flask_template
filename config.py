import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'modzy modelops are incredible'

	API_URL = os.environ.get('API_URL') or "https://app.modzy.com/api"
	API_KEY = os.environ.get('API_KEY') or "b7rsdiLdtWfxgZ2J8g7f.S9fLI7sBMgzML7rVCDM2"
	
	DEBUG =  os.environ.get('FLASK_DEBUG') or 0