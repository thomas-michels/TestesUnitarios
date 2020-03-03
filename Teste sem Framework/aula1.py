
class Pessoa():

    def __init__(self):
        self.nome = ''
        self.idade = 0

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade


if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.set_nome('AAAA')

    assert isinstance(pessoa, Pessoa), 'Não é um objeto da classe Pessoa'
    assert pessoa.get_nome() == 'AAAA', 'Nome incorreto'