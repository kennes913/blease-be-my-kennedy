"""
TODO: add module docstring
"""

import app

# This is for cli control of database and testing.
if not app.app_config.DEBUG:
    del app
    
