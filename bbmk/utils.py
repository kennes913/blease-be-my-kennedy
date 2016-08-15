import bbmk.config
import os

def load_config():
	""" Returns config based on presence of various 
	configuration files. 

	return :: app configuration module 
	"""
	try:
		if bbmk.config.develop:
			return bbmk.config.develop
		else:
			return bbmk.config.production
	except AttributeError:
	 	return bbmk.config.default









