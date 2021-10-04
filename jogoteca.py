from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# App Config 'Separar as Configurações pra outro arquivo Python'
app.config.from_pyfile('config.py')


# Database SetUp
db = MySQL(app)

from views import *

if __name__ == '__main__':
    app.run()
