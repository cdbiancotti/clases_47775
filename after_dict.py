# pop en diccionarios
# bucles

'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''

# cant_pisos = int(input('Ingrese el numero de pisos del triangulo: '))

# for iteracion in range(1, cant_pisos + 1):
#     print('*' * iteracion)

# for letra in 'hola como va?':
#     print(letra)

# pepe = 2+2
# otro = 'hola' if True else 'Jacinto'


# cant_pisos = int(input('Ingrese el numero de pisos del triangulo: '))

# for iteracion in range(1, cant_pisos + 1):
#     print('*' * iteracion)
    
# piso = 1
# while piso <= cant_pisos:
#     print('*' * piso)
#     piso += 1
    
    
auto = {
    'motor': 'v8', 
    'color': 'Negro',
    'vidrios': (6, 'blindadas'),
    'pasajeros': 4,
}

otro_auto = {
    'motor': 'v8', 
    'color': 'Negro',
    'vidrios': (6, 'blindadas'),
    'pasajeros': 4,
}

# valor = auto.pop('motor')
# print(auto)
# print(valor)

for llave in auto:
    valor = otro_auto.pop(llave)
    print(otro_auto)
    print(valor)
    print('')




