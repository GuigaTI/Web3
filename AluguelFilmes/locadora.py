class Locadora():
    def __init__(self):
        self.filmes = {}
        self.clientes = {}
        self.alugados = {}
    def adicionar_filme(self,filme):
        if filme.titulo in self.filmes:
            print("Filme já esta no catalogo!")
        else:
            self.filmes[filme.titulo] = filme
        print("Filme adicionado com sucesso!!")
    def adicionar_cliente(self,cliente):
        if cliente.id in self.clientes:
            print("Cliente já registrado!")
        else:
            self.clientes[cliente.id] = cliente
        print("Cliente registrado com sucesso!!")
    def alugar_filme(self,filme,cliente):
        if filme.titulo in self.filmes:
            if cliente.id in self.clientes:
                if filme.disp:
                    self.filmes[filme.titulo].disp = False
                    self.alugados[filme.titulo] = cliente
                    print(f"O filme {filme.titulo} foi alugado com sucesso para o cliente {cliente.nome}")
                else:
                    print(f"O filme {filme.titulo} não está disponivel")
            else:
                print(f'O cliente {cliente.nome} não está registrado!')
        else:
                print(f"O filme {filme.titulo} não está no catalogo")
    def listar_filmes_disponiveis(self):
        if not self.filmes:
            print("Nenhum filme disponivel no momento!")
        else:
            for filme in self.filmes.values():
                if filme.disp:
                    print(f"\nFilme: {filme.titulo} - Ano de Lançamento: {filme.anoLac} - Gênero: {filme.genero}")
    def listar_filmes_alugados(self):
        if not self.alugados:
            print("Nenhum filme alugado no momento!")
        else:
            for t,n in self.alugados.items():
                print(f"\nFilme: {t} alugado pelo cliente {n}")
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente registrado no momento!")
        else:
            for cliente in self.clientes.values():
                print(f"\nID: {cliente.id} - Nome: {cliente.nome} ")