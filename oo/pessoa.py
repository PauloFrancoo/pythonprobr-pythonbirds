class Pessoa:
    olhos = 2  # atributo Default  ou atributo de classe
    def __init__(self, *filhos, nome=None, idade=59):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    @staticmethod
    def metodo_estatico():
        return 59

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    lucia = Pessoa(felipe, nome='Lucia')
    print(Pessoa.cumprimentar(lucia))
    print(id(lucia))
    print(lucia.cumprimentar())
    print(lucia.nome)
    print(lucia.idade)
    for filho in lucia.filhos:
        print("A ", lucia, "tem um filho chamado ", filho.nome)

        ## criando atributo dinamicoamente  (sobrenome)
    lucia.sobrenome = 'Franco'
    print(lucia.nome +' '+ lucia.sobrenome)
    print(lucia.__dict__)
    print(felipe.__dict__)
    print(Pessoa.olhos)
    print(lucia.olhos)
    print(felipe.olhos)
        ########## Todos os objetos da classe pessoa tem 2 olhos e o mesmo ( id de olhos)
    print(id(Pessoa.olhos), id(lucia.olhos), id(felipe.olhos))
    ################
    print(Pessoa.metodo_estatico(), lucia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), lucia.nome_e_atributos_de_classe())
