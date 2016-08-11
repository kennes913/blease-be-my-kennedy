import os

def load_config(something):
	raise NotImplementedError


def create_db_file(name):
	"""Create a sqlite3 db file.
	
	:params name: str, name of database file 
	"""
	root = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
	file = open(root+'/storage/{}.db'.format(name), 'w')
	file.close()
	 
def delete_db_file(name):
	"""Delete target sqlite3 db file.
	
	:params name: str, name of database file 
	"""
	root = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
	os.remove(root+'/storage/{}.db'.format(name))
	








