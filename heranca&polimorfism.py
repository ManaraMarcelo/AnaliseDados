'''1. Herança
O que é?
Permite criar uma classe "filha" que herda atributos e métodos de uma classe "pai". Assim, você pode reutilizar código e criar hierarquias.

Exemplo:
Uma classe geral Animal pode ter características comuns, como nome e método de alimentação. Classes específicas, como Carnívoro e Herbívoro, podem herdar de Animal e adicionar comportamentos próprios.
'''
# Classe Pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def alimentar(self):
        print(f"{self.nome} está se alimentando.")

# Classes Filhas
class Carnivoro(Animal):
    def alimentar(self):
        print(f"{self.nome} está comendo carne.")

class Herbivoro(Animal):
    def alimentar(self):
        print(f"{self.nome} está comendo plantas.")
'''2. Polimorfismo
O que é?
Permite que métodos com o mesmo nome ajam de forma diferente dependendo do contexto ou da classe que os implementa.

Exemplo:
No exemplo acima, o método alimentar() age de forma diferente para Carnívoro e Herbívoro, mas ambos usam o mesmo nome.
'''
# Uso
leao = Carnivoro("Leão")
elefante = Herbivoro("Elefante")

# Polimorfismo em ação
animais = [leao, elefante]
for animal in animais:
    animal.alimentar()

# Saída:
# Leão está comendo carne.
# Elefante está comendo plantas.
'''Resumo Rápido
Herança: Reutiliza código criando classes filhas que herdam de uma classe pai.
Exemplo: Carnívoro e Herbívoro herdando de Animal.
Polimorfismo: Permite que métodos como alimentar() tenham comportamentos diferentes em classes específicas.'''