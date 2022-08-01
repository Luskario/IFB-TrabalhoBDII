from database.MysqlConnection import conn

cursor = conn.cursor()

def create(sql):
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql)
        conn.commit()
        print("Campo cadastrado com sucesso")
    except:
        print("Falha ao cadastrar")
    cursor.close()

    

def read(data):
    cursor = conn.cursor()
    sql = "SELECT * FROM %s" % data
    try:
        cursor.execute(sql)
        resultado = cursor.fetchall()
    except:
        print("Falha ao imprimir")
    for result in resultado:
        print(result)
    cursor.close()



def update(data):
    cursor = conn.cursor()
    try:
        cursor.execute(data)
        conn.commit()
        print("Campo atualizado com sucesso")
    except:
        print("Falha ao atualizar")
    cursor.close()



def delete(data):
    cursor = conn.cursor()
    sql = "DELETE FROM %s WHERE %s = %s" % data
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print("ID não cadastrado")
    if cursor.rowcount != 0:
        print("Campo exluido com sucesso")
    else:
        print("ID não cadastrado")
    cursor.close()

    