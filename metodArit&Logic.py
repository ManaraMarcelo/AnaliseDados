
class Horario: 
    def __init__ (self, hour, minute, second):
        self.horas = hour
        self.minutos = minute
        self.segundos = second
 
    def __str__ (self): 
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
    
    # Métodos Aritiméticos ------------------
    '''
    Serve para estilizar a forma como eu quero que expressões aritiméticas reajam ao meu código
    '''
    def __add__ (self, other):
        h = self.horas + other.horas
        m = self.minutos + other.minutos
        s = self.segundos + other.segundos

        if s >= 60: 
            s -= 60
            m += 1

        if m >= 60: 
            m -= 60
            h += 1

        if h >= 24:     
            h -= 24

        return Horario(h, m, s)
    
    # Métodos Lógicos --------------------------------
    '''
    - Posso definir como os operadores lógicos vão reagir à minha classe
    - Quando defino um operador lógico, seus complementares mudam também
    '''
    def __gt__ (self, other): # gt = 'greater than' ou seja '>'
        if self.horas > other.horas:
            return True
        elif self.horas == other.horas and self.minutos > other.minutos: 
            return True
        elif self.horas == other.horas and self.minutos == other.minutos and self.segundos > other.segundos:
            return True
        else: return False

entrada = Horario(9, 22, 30)
expediente1 = Horario(8, 25, 60)
expediente2 = Horario(8, 25, 33)
saida = entrada + expediente1

print(f"Hoje eu entrei as: {entrada}\nTrabalhei por: {expediente1}\nPor isso saí às: {saida}")
print(expediente1 > expediente2)



