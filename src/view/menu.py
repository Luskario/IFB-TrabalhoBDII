from view.options import opMenuExtras, opMenuFuncionarios, opMenuPrincipal, opMenuClientes, opMenuEmpresas, opMenuFestas, opMenuServicos, opMenuGerenciaFestas
import os

def menuPrincipal():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Empresas
        [2] Clientes
        [3] Festas
        [4] Funcionários
        [5] Extras

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
        
        [5] Gerência Festas

        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuFestas(op)

def menuFuncionarios():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Funcionario
        [2] Listar Funcionario
        [3] Atualizar Funcionario
        [4] Deletar Funcionario

        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuFuncionarios(op)

def menuExtras():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Extra
        [2] Listar Extra
        [3] Atualizar Extra
        [4] Deletar Extra

        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuExtras(op)

def menuAtualizar(colunas):
    os.system('clear') or None
    op = 10
    i = 1
    print('Qual campo deseja atualizar')
    for x in colunas:
        texto = "[%s]  " % i + x
        print(texto)
        i = i+1
    print("")
    print("[0]  voltar!")   
    return i
    
def menuServicos():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Adicionar Serviço
        [2] Remover Serviço
        [3] Serviços Contratados
        
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuServicos(op)

def menuGerenciaFestas():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Festa Geral
        [2] Conta Festa
        [3] Serviços
        [4] ...
        [5] ...
        
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuGerenciaFestas(op)