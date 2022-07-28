from view.options import opMenuPrincipal, opMenuClientes, opMenuEmpresas, opMenuFestas
import os

def menuPrincipal():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Empresas
        [2] Clientes
        [3] Festas
        [4] ...
        [5] ...
        [0] sair!
        """
    )
    op = int(input("> ") or "10")
    opMenuPrincipal(op)
    
def menuEmpresas():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Empresa
        [2] Listar Empresas
        [3] Atualizar Empresa
        [4] Deletar Empresa
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuEmpresas(op)


def menuClientes():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Cliente
        [2] Listar Clientes
        [3] Atualizar Cliente
        [4] Deletar Cliente
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuClientes(op)

def menuFestas():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Festa
        [2] Listar Festas
        [3] Atualizar Festa
        [4] Deletar Festa
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuFestas(op)