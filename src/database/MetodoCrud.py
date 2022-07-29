from database.MysqlConnection import conn

cursor = conn.cursor()

def create(data):
    cursor = conn.cursor()
    sql = "INSERT INTO %s VALUES (%s)"
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("Campo cadastrado com sucesso")
    except:
        print("Falha ao cadastrar")
    cursor.close()
    

def read(data):
    cursor = conn.cursor()
    sql = "SELECT * FROM %s"
    try:
        cursor.execute(sql,data)
        resultado = cursor.fetchall()
    except:
        print("Falha ao imprimir")
    for result in resultado:
        print(result)
    cursor.close()


def update(data):
    cursor = conn.cursor()
    sql = "UPDATE %s SET %s = %s WHERE id = %s"
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("Campo atualizado com sucesso")
    except:
        print("Falha ao atualizar")


def delete(data):
    cursor = conn.cursor()
    sql = "DELETE FROM %s WHERE id = %s"
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("Campo exluido com sucesso")
    except:
        print("ID não cadastrado")
    cursor.close()
    