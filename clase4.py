# if, elif, else

# if

# if False:
#     print('Es verdadero!') # representa un bloque de codigo
#     valor1 = 2
#     valor2 = 5
#     suma = valor1 + valor2
#     print(suma)


# if 3 < 2: # si es correcta la condicion hacemos esto
#     print('Es verdadera la segunda!')
# else: # si no, hacemos esto
#     print('La condicion no se cumplio')

# print('Codigo que esta despues de los if')


# if 3 < 2: print('Es verdadera la segunda!')
# else: print('La condicion no se cumplio')

# print('Es verdadera la segunda!') if 3 < 2 else print('La condicion no se cumplio')


# texto = 'Es mayor' if 3 < 2 else 'No es mayor'

# print(texto)




# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))
    
# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')

# if primer_numero > segundo_numero:
#     print('El primer valor es mayor al segundo')
#     print('Y tambien muestro esto porque sigo estando en el mismo bloque de codigo')

# if primer_numero == segundo_numero:
#     print('Ambos valores son iguales')


# if primer_numero < segundo_numero: # si
#     print('El primer valor es menor al segundo')
# elif primer_numero > segundo_numero: # sino, si
#     print('El primer valor es mayor al segundo')
#     print('Y tambien muestro esto porque sigo estando en el mismo bloque de codigo')
# else: # sino
#     print('Ambos valores son iguales')


# primer_numero = int(input('Ingrese una numero: '))

# if primer_numero < 20:
#     print('es menor a 20')
# if primer_numero < 30:
#     print('es menor a 30')
# if primer_numero < 40:
#     print('es menor a 40')
# if primer_numero < 50:
#     print('es menor a 50')


# if primer_numero < 50:
#     print('es menor a 50')
#     if primer_numero < 40:
#         print('es menor a 40')
#         if primer_numero < 30:
#             print('es menor a 30')
#             if primer_numero < 20:
#                 print('es menor a 20')


# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('es menor a 30')
# elif primer_numero < 40:
#     print('es menor a 40')
# elif primer_numero < 50:
#     print('es menor a 50')
# else:
#     print('no se cumplio ninguna condicion de las anteriores')

# var = 15
# primer_numero = int(input('Ingrese una numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero == segundo_numero:
#     print('son iguales')
#     if primer_numero < var:
#         print('son menores a var')
#     else:
#         print('son mayores a var')
# else:
#     print('no son iguales')
#     if primer_numero < var:
#         print('primer_numero es menor a var')
#         if segundo_numero < var:
#             print('segndo_numero es menor a var')
#         else:
#             print('segndo_numero es mayor a var')
#     else:
#         print('primer_numero es mayor a var')

# print('Estoy fuera de los if')


# ejercicio generaciones

# anio = int(input('Ingrese un anio:'))

# if 1920 <= anio <= 1945: 
#     print('Generacion Silenciosa')
# elif 1946  <= anio <=  1964:
#     print('Baby Boomer')
# elif 1965  <= anio <=  1979:
#     print('Generacion X')
# elif 1980  <= anio <=  2000:
#     print('Generacion Y')
# elif 2001  <= anio <=  2010:
#     print('Generacion Z')
# else:
#     print('No existe generación asociada')
    
# ejercicio Aprobacion credito bancario
# edad_cliente = 15
# antiguedad = 10
# ingreso = 1500

# if edad_cliente >= 18 and ((antiguedad >= 3 and ingreso > 2500) or ingreso >= 4000):
#     print('Se aprobo')
# else:
#     print('No se aprueba')

# ejercicio Marvel vs Capcom (20min)
# Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una 
# preferencia (Marvel o Capcom).
# El grupo A está formado por fans de Marvel con un nombre anterior a la 
# M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y preferencia, 
# y muestre por pantalla el grupo que le corresponde.

# nombre = input('Ingrese su nombre: ').lower()
# prefe = input('Ingrese si le gusta "Marvel" o "Capcom": ').lower()

# if (prefe == 'marvel' and  nombre < 'm') or (nombre > 'n' and prefe == 'capcom'):
#     print('Sos del grupo A')
# else:
#     print('Sos del grupo B')