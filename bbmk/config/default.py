"""
default configuration -- fallback configuration if production configuration fails
"""
import os

# base directory
_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# static image files
STATIC_IMAGES_PATH = os.path.join(_basedir, 'static/images')

# settings
DEBUG = True

# database info
DATABASE_PATH = os.path.join(_basedir, 'storage/database.db')
DATABASE_SCHEMA = os.path.join(_basedir, 'storage/database.sql')
DATABASE = {'name':DATABASE_PATH,
            'engine':'peewee.SqliteDatabase'}

# basic auth defaults
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'admin'

# upload file
UPLOAD_FOLDER = os.path.join(_basedir, 'processing')
ALLOWED_EXTENSIONS = set(['txt', 'xlsx', 'csv'])


# config info 
_config_info = {'root':_basedir,
                'database':DATABASE_PATH,
                'database_schema':DATABASE_SCHEMA,
                'debug':DEBUG}

del os
