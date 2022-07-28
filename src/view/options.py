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
        print("f1")
    elif op == 0:
        print("volte sempre")
    else:
        menu.menuPrincipal()

def opMenuEmpresas(op):
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
        menu.menuEmpresas()

def opMenuClientes(op):
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
        menu.menuClientes()

def opMenuFestas(op):
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
        menu.menuFestas()
