class Pessoa:
    olhos = 2    # atributo default ou atributo de classe
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'



if __name__ == '__main__':
    julio = Pessoa(nome ='Julio')
    luciano = Pessoa(julio, nome ='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    #print(luciano.sobrenome)
    del luciano.filhos
    luciano.olhos = 1
    print(julio.__dict__)
    print(luciano.__dict__)
    Pessoa.olhos = 3
    del luciano.olhos    # apaga o atributo do objeto e não da classe
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(julio.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(julio.olhos))
