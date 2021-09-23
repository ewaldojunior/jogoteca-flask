from flask import Flask
from flask_mysqldb import MySQL

#iniciando a aplicação
app = Flask(__name__)
app.config.from_pyfile('config.py')

#criar o banco
db = MySQL(app)

from views import *

#só é executado se for compilado no jogoteca.py
if __name__ == '__main__':
    app.run(debug=True)