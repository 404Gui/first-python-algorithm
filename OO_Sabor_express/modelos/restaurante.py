class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = True
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}') 
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
   
    def alternar_estado(self):
        self._ativo = not self._ativo

'''Próxima Aulas é sobre métodos especiais'''
'''dir(nome_variável) mostra todas os métodos, um deles é o __init__'''
##########################################################################




































# Código abaixo foi um exercício
# class Musica:
#     def __init__(self, nome, artista, duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

#     def __str__(self):
#         return f'{self.nome} | {self.artista} | {self.duracao}'


# musico = Musica('OO', 'Pappi', '3500')
# musico2 = Musica('Saturday Night', 'Misfits', '3500')

# print(musico)
# print(musico2)