
# -Método construtor [Simplesmente define a classe, ela apenas existe]-----
class Pessoa: 
    def __init__(self, name, age, height, color, weight):
        self.nome = name 
        self.idade = age
        self.altura = height
        self.cor = color
        self.peso = weight

        self.profissao = None
        self.salario = 0
        self.num_filhos = 0

    #Definindo outros métodos da classe -------------
    def fala(self, mensagem):
        '''print(mensagem) - seria uma maneira simples e fixa'''
        print(f"{self.nome} diz: '{mensagem}'")

    def consegue_emprego(self, profession, salary):
        self.profissao = profession
        self.salario = salary

    def aumento_salario(self, percentage):
        self.salario = self.salario*(1 + percentage)

#Criar um objeto [Instanciação] ------------

Marcelo = Pessoa("Marcelo", 19, 185, "White", 73) #Marcelo é um objeto
Rafael = Pessoa("Rafael", 39, 173, "White", 72)

'''print(Marcelo.nome) # sintaxe objeto.atributo
print(Marcelo.idade)
print(Marcelo.altura)
print(Marcelo.cor)
print(Marcelo.peso)'''

print(vars(Marcelo)) #forma de visualizar tudo na classe de maneira facil
print(vars(Rafael))
print(Marcelo.fala("Meu nome é Manara"))
Rafael.consegue_emprego("Empreendedor", 5500.0)
#print(vars(Rafael))
print(f"{Rafael.nome} conseguiu a profissão '{Rafael.profissao}' com o salário médio de R${Rafael.salario}")
Rafael.aumento_salario(0.3)
print(f"{Rafael.nome} recebeu um aumento de salario, totalizando em R${Rafael.salario} mensais.")

    