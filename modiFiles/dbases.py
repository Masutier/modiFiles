import os

def dbSqlite(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'senadlake.db'),
        }
    }

    return DATABASES


def dbPostgres(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'senadb',
            'USER': config['DB_USER'],
            'PASSWORD': config['DB_PASSPORT'],
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    
    return DATABASES
    

def dbmariadb(BASE_DIR):
	import sys
	import mariadb

	# Connect to MariaDB Platform
	try:
	    conn = mariadb.connect(
		user="db_user",
		password="db_user_passwd",
		host="192.0.2.1",
		port=3306,
		database="employees"

	    )
	except mariadb.Error as e:
	    print(f"Error connecting to MariaDB Platform: {e}")
	    sys.exit(1)

	# Get Cursor
	cur = conn.cursor()
