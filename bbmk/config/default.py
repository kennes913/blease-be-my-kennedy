"""
default config -- loads only if develop config is not present

"""
import os

# base directory
_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Database 
DATABASE_PATH = os.path.join(_basedir, '/storage/database.db')
DATABASE_CONNECT_OPTIONS = {}

# miscellaneous shite 
DEBUG = True
SECRET_KEY = 'develop'

del os