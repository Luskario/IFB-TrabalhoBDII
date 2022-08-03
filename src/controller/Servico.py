from database.MetodoCrud import create, read, update, delete
from controller import Extra
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id festa: '),
        input('id extra: ')

    )
    os.system('clear') or None
    
    sql = "INSERT Servico VALUES (%s, %s)" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuServicos()

def deletar():
    os.system('clear') or None
    data = ('Servico', 'cod_fes', input('id festa:') +" AND cod_ext = " + input('id extra:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuServicos()

#----------------------------------------------------------#
 
def fun1():
    os.system('clear') or None



    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuServicos()