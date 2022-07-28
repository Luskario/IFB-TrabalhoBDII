from warnings import catch_warnings
import mysql.connector
from mysql.connector import errorcode

dbconfig = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
}

try:
    conn = mysql.connector.connect(**dbconfig)
    print("Conectado com sucesso")
    mycursor = conn.cursor();
except mysql.connector.Error as err:
    print("Falha ao conectar")
