from database.MetodoCrud import create, read, update, delete
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id: '),
        input('nome: '),
        input('cpf: '),
        input('login: '),
        input('senha: '),
        input('telefone: '),
        input('endereco: ')
    )
    os.system('clear') or None
    
    sql = "INSERT Cliente VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s')" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuClientes()

def ler():
    os.system('clear') or None
    data = ('Cliente');
    read(data)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuClientes()

def atualizar():
    colunas = ('nome_cli', 'cpf_cli','login_cli', 'senha_cli', 'telefone_cli', 'endereco')
    colunasN = ('nome', 'cpf','login', 'senha', 'telefone', 'endereco')
    i = menu.menuAtualizar(colunasN)
    op = int(input("> ") or i+1)
    if op > i:
        return atualizar()
    elif op == 0:
        return menu.menuClientes()
    else:
        data = (
            colunas[op-1],
            input('valor:'),
            'cod_cli',
            input('codigo:')
        )

    sql = "UPDATE Cliente SET %s = '%s' WHERE %s = %s" % data

    update(sql)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuClientes()


def deletar():
    os.system('clear') or None
    data = ('Cliente', 'cod_cli', input('codigo:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuClientes()