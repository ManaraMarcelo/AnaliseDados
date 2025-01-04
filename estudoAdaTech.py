def cumprimento_parte_dia(nome, parte_dia):
    '''
    Esta função recebe um nome e uma parte do dia e imprime um cumprimento de acordo com os argumentos

    - nome (str): qualquer nome próprio
    - parte_dia (str): unicamente["manhã", "tarde", "noite"]
    '''

    if parte_dia == "manhã":
        cumprimento = "Bom dia"
    elif parte_dia == "tarde":
        cumprimento = "Boa tarde"
    elif parte_dia == "noite":
        cumprimento = "Boa noite"
    else: 
        raise ValueError(f"A parte do dia informada ({parte_dia}), não é válida!")
    cumprimento = f"{cumprimento}, {nome}"
    print(cumprimento)

cumprimento_parte_dia("Marcelo", "manhã")


# --- POO [PROGRAMAÇÃO ORIENTADA A OBJETOS] ---

# Classes: O Molde -------------------------------------------
'''
Imagine que você quer criar vários carros no seu mundo. Primeiro, você precisa de um molde que diga como eles devem ser. Esse molde é a classe.
Ela define o que todos os carros terão em comum, como:

Atributos: características (cor, marca, modelo).
Métodos: ações que os carros podem realizar (acelerar, frear).
'''
class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor         # Atributo
        self.marca = marca     # Atributo
        self.modelo = modelo   # Atributo

    def acelerar(self):        # Método
        print(f"O {self.modelo} está acelerando!")

    def frear(self):           # Método
        print(f"O {self.modelo} está freando!")

# Objetos: O Produto --------------------------------------------
'''
Depois de criar o molde (classe), você pode usar ele para fazer carros de verdade. Cada carro que você cria é um objeto.
Eles têm características únicas, mas todos seguem o molde.
'''
# Criando objetos a partir da classe Carro
carro1 = Carro("vermelho", "Ferrari", "F8")
carro2 = Carro("azul", "Ford", "Mustang")
'''
Agora temos dois carros no nosso mundo:

O carro1 é uma Ferrari vermelha modelo F8.
O carro2 é um Mustang azul. 
'''
# Atributos: As Características --------------------------------------------
'''
Os atributos são as "características" do objeto. Por exemplo:

Cor: vermelho, azul
Marca: Ferrari, Ford
Modelo: F8, Mustang
Essas características definem cada carro, mas elas vêm do molde (classe). Você pode acessá-las e até modificá-las!
'''
print(carro1.cor)   # Saída: vermelho
print(carro2.marca) # Saída: Ford

# Mudando a cor do carro1
carro1.cor = "preto"
print(carro1.cor)   # Saída: preto

# Métodos: As Ações --------------------------------------------
'''
Os métodos são as "ações" que o carro pode realizar. Eles são como "habilidades" que você programou no molde.
'''
carro1.acelerar() # Saída: O F8 está acelerando!
carro2.frear()    # Saída: O Mustang está freando!

# Resumo ------------------------------------------------------
'''
Classe: É o molde ou plano (Carro).
Objeto: É o "carro de verdade" criado a partir do molde.
Atributos: São as características do carro (cor, marca, modelo).
Métodos: São as ações que o carro pode realizar (acelerar, frear).
'''

# 1. Encapsulamento: Protegendo os dados ---------------------------
'''
É como colocar os dados em uma "caixa" e controlar quem pode mexer neles.
Os atributos e métodos de uma classe podem ser privados (só a própria classe pode acessá-los) ou públicos (qualquer um pode acessar).

Por que usar? Para evitar alterações indesejadas nos dados.
Exemplo: Uma conta bancária só permite alterar o saldo com métodos específicos, como depositar() ou sacar().
python
Copiar código
class ContaBancaria:
'''
def __init__(self, saldo):
    self.__saldo = saldo  # Atributo privado

def depositar(self, valor):
    self.__saldo += valor

def ver_saldo(self):
    return self.__saldo
# 2. Abstração: Mostrando só o necessário ----------------------------
'''
É como um carro: você só precisa saber dirigir (volante, pedal), sem entender como o motor funciona.
A ideia é esconder os detalhes complexos e mostrar apenas o essencial para o usuário.

Por que usar? Para simplificar o uso de objetos.
Exemplo: Um método ligarCarro() não precisa mostrar como cada fio é conectado.
python
Copiar código
class Carro:
'''
def ligar(self):
    print("Carro ligado!")  # Só importa que ele ligue; os detalhes internos ficam escondidos.
# 3. Herança: Reutilizando código ------------------------------------
'''
É como herdar características de um "pai". Uma classe pode herdar atributos e métodos de outra, evitando código repetido.

Por que usar? Para reaproveitar funcionalidades e criar hierarquias.
Exemplo: Uma classe Animal pode ter características comuns que Cachorro e Gato herdam.
python
Copiar código
class Animal:
'''
def __init__(self, nome):
    self.nome = nome

def comer(self):
    print(f"{self.nome} está comendo.")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

# Uso
dog = Cachorro("Rex")
dog.comer()  # Saída: Rex está comendo.
dog.latir()  # Saída: Au au!
# 4. Polimorfismo: Formas diferentes de agir ---------------------------------------
'''
É quando várias classes têm o mesmo método, mas cada uma age de forma diferente.
Pense em um botão "fazer som": cada animal pode emitir sons diferentes, mas o método é o mesmo (emitirSom()).

Por que usar? Para permitir flexibilidade no código.
Exemplo: Cachorro late, Gato mia, mas ambos têm o método emitirSom().
python
Copiar código
class Gato(Animal):
'''
def emitirSom(self):
    print("Miau!")

class Cachorro(Animal):
    def emitirSom(self):
        print("Au au!")

# Uso
animais = [Cachorro("Rex"), Gato("Felix")]
for animal in animais:
    animal.emitirSom()  # Saída: Au au! / Miau!

# Resumo Rápido -------------------------------------------
'''
Encapsulamento: Protege os dados e controla quem pode acessá-los.
Abstração: Esconde detalhes complexos, mostrando só o necessário.
Herança: Reaproveita código entre classes "pai" e "filho".
Polimorfismo: Permite que métodos ajam de formas diferentes em classes distintas.
'''