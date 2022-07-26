from database.MysqlConnection import DBConn
import mysql.connector

teste = DBConn()

teste.execute("Select now()")