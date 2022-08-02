from database.MetodoCrud import create, read, update, delete
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id: '),
        input('preço: '),
        input('tipo: '),
        input('nome: '),
        input('duração: '),
        input('id cliente: '),
        input('id empresa: '),
    )
    os.system('clear') or None
    
    sql = "INSERT Festa VALUES (%s, %s, '%s', '%s', %s, '%s', '%s')" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuFestas()

def ler():
    os.system('clear') or None
    data = ('Festa');
    read(data)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuFestas()

def atualizar():
    colunas = ('nome_fes', 'preco_fes','tipo_fes', 'duracao_fes', 'cod_cli', 'cod_emp')
    colunasN = ('nome', 'preço', 'tipo', 'duração', 'id cliente', 'id empresa')
    i = menu.menuAtualizar(colunasN)
    op = int(input("> ") or i+1)
    if op > i:
        return atualizar()
    elif op == 0:
        return menu.menuFestas()
    else:
        data = (
            colunas[op-1],
            input('valor:'),
            'cod_fes',
            input('codigo:')
        )

    if op == 2 or op <= 4:
        sql = "UPDATE Festa SET %s = %s WHERE %s = %s" % data
    else:
        sql = "UPDATE Festa SET %s = '%s' WHERE %s = %s" % data

    update(sql)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuFestas()

def deletar():
    os.system('clear') or None
    data = ('Festa', 'cod_fes', input('codigo:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuFestas()