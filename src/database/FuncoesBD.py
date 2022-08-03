from database.MysqlConnection import conn

cursor = conn.cursor()


def exe_post(sql, mensagem):
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql)
        conn.commit()
        print(mensagem)
    except:
        print("Falha")
    cursor.close()

def exe_read(sql):
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for result in resultado:
            print(result)
    except:
        print("Falha ao imprimir")
    
    cursor.close()