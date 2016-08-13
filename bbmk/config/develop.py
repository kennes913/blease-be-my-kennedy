"""
develop config -- will load first amongst develop, default and production configs

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
