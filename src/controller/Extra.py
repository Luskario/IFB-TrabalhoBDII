from database.MetodoCrud import create, read, update, delete
from view import menu
import os


def criar():
    os.system('clear') or None
    data = (
        input('id: '),
        input('nome: '),
        input('preço: '),
        'disp',
        input('carga horaria: '),
        input('tipo: ')
    )
    os.system('clear') or None
    
    sql = "INSERT Extra VALUES (%s, '%s', '%s', '%s', '%s', '%s')" % data
    
    create(sql)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuExtras()

def ler():
    os.system('clear') or None
    data = ('Extra');
    read(data)
    op = int(input('Presione ENTER para voltar')or 10)
    menu.menuExtras()

def atualizar():
    colunas = ('nome_ext', 'preco_ext', 'hora_ext', 'tipo_ext')
    colunasN = ('nome', 'preço', 'carga horaria', 'tipo')
    i = menu.menuAtualizar(colunasN)
    op = int(input("> ") or i+1)
    if op > i:
        return atualizar()
    elif op == 0:
        return menu.menuExtras()
    else:
        data = (
            colunas[op-1],
            input('valor:'),
            'cod_ext',
            input('codigo:')
        )

    if op == 2 or op == 3 or op == 4:
        sql = "UPDATE Extra SET %s = %s WHERE %s = %s" % data
    else:
        sql = "UPDATE Extra SET %s = '%s' WHERE %s = %s" % data

    update(sql)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuExtras()


def deletar():
    os.system('clear') or None
    data = ('Extra', 'cod_ext', input('codigo:'))
    delete(data)
    op = int(input('Presione ENTER para voltar') or 10)
    menu.menuExtras()