import os
#informações para unir com o banco de dados
SECRET_KEY = 'alura'
MYSQL_HOST= "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "calopsitabrasileira" #precisa mudar de acordo com a senha do db
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'