from database.MetodoCrud import create, read, update, delete
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id: '),
        input('nome: '),
        input('telefone: '),
        input('endereço: '),
        input('id empresa: '),
        input('equipe: ')
    )
    os.system('clear') or None
    
    sql = "INSERT Funcionario VALUES (%s, '%s', '%s', '%s', '%s', '%s')" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuFuncionarios()

def ler():
    os.system('clear') or None
    data = ('Funcionario');
    read(data)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuFuncionarios()

def atualizar():
    colunas = ('nome_fun', 'telefone_fun', 'endereco_fun', 'cod_emp', 'equip_fun')
    colunasN = ('nome', 'telefone', 'endereco', 'id empresa', 'equipe')
    i = menu.menuAtualizar(colunasN)
    op = int(input("> ") or i+1)
    if op > i:
        return atualizar()
    elif op == 0:
        return menu.menuFuncionarios()
    else:
        data = (
            colunas[op-1],
            input('valor:'),
            'cod_fun',
            input('codigo:')
        )

    if op == 2 or op == 3 or op == 4:
        sql = "UPDATE Funcionario SET %s = %s WHERE %s = %s" % data
    else:
        sql = "UPDATE Funcionario SET %s = '%s' WHERE %s = %s" % data

    update(sql)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuFuncionarios()


def deletar():
    os.system('clear') or None
    data = ('Funcionario', 'cod_fun', input('codigo:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuFuncionarios()