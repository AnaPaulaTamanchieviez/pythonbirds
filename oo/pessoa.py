class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    ana = Pessoa(nome='Ana')
    douglas = Pessoa(ana, nome='Douglas') #o objeto Pessoa (ana) coloquei como filho do objeto douglas
    print(ana.cumprimentar())
    print(ana.nome)



