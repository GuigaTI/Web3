class Cliente:
    def __init__(self,_id,_nome):
        self.id = _id
        self.nome = _nome
    def __str__(self):
        return f"{self.nome} (ID: {self.id})"