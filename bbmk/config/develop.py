"""
develop config -- will load first amongst develop, default and production configs

"""
import os

# base directory
_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# database info
DATABASE_PATH = os.path.join(_basedir, 'storage/database.db')
DATABASE_SCHEMA = os.path.join(_basedir, 'storage/database.sql')
DATABASE = {'name':DATABASE_PATH,
    		'engine':'peewee.SqliteDatabase'}
# settings
DEBUG = True
SECRET_KEY = 'develop'

# admin
email = 'admin@bleasebemykennedy.com'

# config info 
_config_info = {'root':_basedir,
				'database':DATABASE_PATH,
				'database_schema':DATABASE_SCHEMA,
				'debug':DEBUG}
del os
