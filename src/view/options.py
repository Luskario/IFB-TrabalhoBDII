from controller import Cliente, Empresa, Festa, Extra, Funcionario, Servico
from view import menu

def opMenuPrincipal(op):
    if op == 1:
        menu.menuEmpresas()
    elif op == 2:
        menu.menuClientes()
    elif op == 3:
        menu.menuFestas()
    elif op == 4:
        menu.menuFuncionarios()
    elif op == 5:
        menu.menuExtras()
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
    elif op == 5:
        menu.menuServicos()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuFestas()

def opMenuFuncionarios(op):
    if op == 1:
        Funcionario.criar()
    elif op == 2:
        Funcionario.ler()
    elif op == 3:
        Funcionario.atualizar()
    elif op == 4:
        Funcionario.deletar()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuFuncionarios()

def opMenuExtras(op):
    if op == 1:
        Extra.criar()
    elif op == 2:
        Extra.ler()
    elif op == 3:
        Extra.atualizar()
    elif op == 4:
        Extra.deletar()
    elif op == 0:
        menu.menuPrincipal()
    else:
        menu.menuExtras()

def opMenuServicos(op):
    if op == 1:
        Servico.criar()
    elif op == 2:
        Servico.deletar()
    elif op == 0:
        menu.menuFestas()
    else:
        menu.menuServicos()