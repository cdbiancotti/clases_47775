import math


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


class Figura:
    
    def area(self):
        ...
    
    # v2
    def mostrar_area(self):
        print(self.area())

class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura