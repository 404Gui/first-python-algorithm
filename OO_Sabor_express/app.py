from modelos.restaurante import Restaurante

restaurante_pizzaloka = Restaurante('pizza loka', 'Pizzaria')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_barato = Restaurante('Baratos foods', 'Comida Barata')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':