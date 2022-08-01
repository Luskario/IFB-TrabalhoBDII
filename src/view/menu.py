from view.options import opMenuExtra, opMenuFuncionario, opMenuHistorico, opMenuPrincipal, opMenuClientes, opMenuEmpresas, opMenuFestas
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
        [6] Histórico
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

def menuFuncionario():
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
    opMenuFuncionario(op)

def menuExtra():
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
    opMenuExtra(op)

def menuHistorico():
    os.system('clear') or None
    op = 10
    print(
        """
        [1] Cadastrar Historico
        [2] Listar Historico
        [3] Atualizar Historico
        [4] Deletar Historico
        [0] voltar!
        """
    )
    op = int(input("> ") or "10")
    opMenuHistorico(op)



def menuAtualizar(colunas):
    os.system('clear') or None
    op = 10
    i = 1
    print('Qual campo deseja atualizar')
    for x in colunas:
        texto = "[%s]  " % i + x
        print(texto)
        i = i+1
    print("[0]  voltar!")   
    return i
    