from database.MetodoCrud import create, read, update, delete
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id: '),
        input('nome: '),
        input('telefone: '),
        input('endereco: ')
    )
    os.system('clear') or None
    
    sql = "INSERT Empresa VALUES (%s, '%s', '%s', '%s')" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuEmpresas()

def ler():
    os.system('clear') or None
    data = ('Empresa');
    read(data)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuEmpresas()

def atualizar():
    colunas = ('nome_emp', 'telefone_emp', 'endereco')
    colunasN = ('nome', 'telefone', 'endereco')
    i = menu.menuAtualizar(colunasN)
    op = int(input("> ") or i+1)
    if op > i:
        return atualizar()
    elif op == 0:
        return menu.menuEmpresas()
    else:
        data = (
            colunas[op-1],
            input('valor:'),
            'cod_emp',
            input('codigo:')
        )

    sql = "UPDATE Empresa SET %s = '%s' WHERE %s = %s" % data

    update(sql)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuEmpresas()


def deletar():
    os.system('clear') or None
    data = ('Empresa', 'cod_emp', input('codigo:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuEmpresas()