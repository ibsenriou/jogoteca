import os


SECRET_KEY = 'alura'


# Database AppConfig
MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306

# Uploads AppConfig
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
