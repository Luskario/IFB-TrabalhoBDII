from controller import Cliente, Empresa, Festa
from view import menu

def opMenuPrincipal(op):
    if op == 1:
        menu.menuEmpresas()
    elif op == 2:
        menu.menuClientes()
    elif op == 3:
        menu.menuFestas()
    elif op == 4:
        menu.menuClientes()
    elif op == 5:
        menu.menuFuncionario()
    elif op == 6:
        menu.menuHistorico()
    elif op == 0:
        print("volte sempre")
    else:
        menu.menuPrincipal()

def opMenuEmpresas(op):
    if op == 1:
        Empresa.criar()
    elif op == 2:
        Empresa.ler()
    elif op == 3:
        Empresa.atualizar()
    elif op == 4:
        Empresa.deletar()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuEmpresas()

def opMenuClientes(op):
    if op == 1:
        Cliente.criar()
    elif op == 2:
        Cliente.ler()
    elif op == 3:
        Cliente.atualizar()
    elif op == 4:
        Cliente.deletar()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuClientes()

def opMenuFestas(op):
    if op == 1:
        Festa.criar()
    elif op == 2:
        Festa.ler()
    elif op == 3:
        Festa.atualizar()
    elif op == 4:
        Festa.deletar()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuFestas()

def opMenuFuncionario(op):
    if op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuFuncionario()

def opMenuExtra(op):
    if op == 1:
        print("f1")
    elif op == 2:
        print("f1")
    elif op == 3:
        print("f1")
    elif op == 4:
        print("f1")
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuExtra()

def opMenuHistorico(op):
    if op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 1:
        print("f1")
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuHistorico()