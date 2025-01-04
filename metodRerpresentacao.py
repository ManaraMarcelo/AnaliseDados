# Método de Representação ------------------
'''
Serve para estilizar a saida do nosso resultado, tornar mais amigavel a saida de nossos escopos
'''
class Horario: 
    def __init__ (self, hour, minute, second):
        self.horas = hour
        self.minutos = minute
        self.segundos = second
 
    def __repr__ (self): #forma mais tecnica do metodo de representação -----------
        '''
        Essa forma não costuma ser usada com o print, o certo seria o __str__.
        O modo __repr__ é usado para modos mais técnicos de visualização
        '''
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos}"
agora = Horario(16, 3, 45)
    
print(agora)