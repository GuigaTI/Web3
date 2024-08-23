from filme import Filme
from cliente import Cliente
from locadora import Locadora
import sys

loc = Locadora()
while True:
        print("Locadora:")
        print("1. Adicionar novo filme")
        print("2. Adicionar novo cliente")
        print("3. Alugar Filme")
        print("4. Listar filmes disponiveis")
        print("5. Listar filmes alugados")
        print("6. Listar Clientes")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tit = input("Digite o titulo do filme: ")
            ano = input("Digite a data de lançamento do filme: ")
            gen = input("Digite o genero do filme: ")
            filme = Filme(tit,ano,gen)
            loc.adicionar_filme(filme)
        elif opcao == "2":
            id = input("Digite o ID do cliente: ")
            nome = input("Digite o nome do cliente: ")
            cliente = Cliente(id,nome)
            loc.adicionar_cliente(cliente)
        elif opcao == "3":
            tit = input("Digite o titulo do filme a ser buscado: ")
            ano = input("Digite a data de lançamento do filme a ser buscado:")
            gen = input("Digite o genero do filme a ser buscado: ")
            id = input("Digite o ID do cliente a ser buscado: ")
            nome = input("Digite o nome do cliente a ser buscado: ")
            filmeB = Filme(tit,ano,gen)
            clienteB = Cliente(id,nome)
            loc.alugar_filme(filmeB,clienteB)
        elif opcao == "4":
            loc.listar_filmes_disponiveis()
        elif opcao == "5":
            loc.listar_filmes_alugados()
        elif opcao == "6":
            loc.listar_clientes()
        elif opcao == "7":
            print("Saindo do sistema!")
            sys.exit()
        else:
            print("Selecione uma opção valída")
