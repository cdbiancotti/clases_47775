# # funciones

# password = '123456'
# contador_errores = 0

# def muestra_y_conteo_de_errores(valor_previo_contador):
#     # contador_errores += 1 # contador_errores = contador_errores + 1
#     contador_errores_interno = valor_previo_contador + 1
#     print(f'Llevas {contador_errores_interno} ingresos invalidos.')
#     if contador_errores_interno < 0: # queda de ejemplo pero no se ejecutaria nunca
#         return 'No me importa nada'
#     print('Vuelva a intentarlo.')
#     return contador_errores_interno

# def suma_de_2(numero1, numero2):
#     print('Se esta haciendo la suma...')
#     return numero1 + numero2

# repetir_menu = True # bandera/flag
# while repetir_menu:
#     print('''
# ==============
#      Menu de Usuario
# ==============
# 1. Cambiar contraseña.
# 2. Suma 2 valores.
# 3. Salir
# ''')
#     opcion_elegida = input('Ingrese la operacion a realizar: ')
#     if opcion_elegida == '1':
#         new_pass = input('Ingrese su nueva contrasenia: ')
#         if new_pass.isalpha():
#             password = new_pass
#         else:
#             print('Se ingreso una contrasenia incorrecta.')
#             contador_errores = muestra_y_conteo_de_errores(contador_errores)
#     elif opcion_elegida == '2':
#         valor1 = int(input('Ingrese un numero: '))
#         valor2 = float(input('Ingrese otro numero: '))
#         print(suma_de_2(valor1, valor2))
#     elif opcion_elegida == '3':
#         repetir_menu = False
#         print('Hasta luego!')
#     else:
#         print('Opcion invalida.')
#         contador_errores = muestra_y_conteo_de_errores(contador_errores)
        


# ej 1
# def saludo(ciudad):
#     return f'¡Hola bienvenidx a {ciudad}!'

# print(saludo(input('Ingrese un nombre de una ciudad: ')))


# ej 2

# lista = [1,2,3,45,1,123,14,12,234,2,1,23,12]

# def media(lista):
#     return sum(lista)/len(lista)
    
# print(f'La media de los numeros {lista} es {media(lista):.2f}')


# ej 3

# def anio_bisiesto(anio):
#     if not anio.isnumeric():
#         print('Ingresa un numero')
#         return
#     else:
#         anio = int(anio)
        
#     if anio%4==0 and (anio%100!=0 or anio%400==0) :
#         print("El año año es bisiesto")
#     else:
#         print("El año año no es bisiesto")

# anio_bisiesto(input('Ingrese un numero: '))

















# ====================================================================
# ====================================================================

# def NOMBRE(PARAMETROS??): # correcto nombramiento de las funciones
#     SENTENCIAS
#     return EXPRESION??
    
# ====================================================================
# ====================================================================

# def mostrar_palabra():
#     print('Perro')
#     # return
    
# mostrar_palabra() 
# valor_retornado = mostrar_palabra()
# print(valor_retornado)


# def retornar_palabra():
#     return 'Perro'

# retornar_palabra()
# print(retornar_palabra())
# valor_retornado = retornar_palabra()
# print(valor_retornado)
# print(type(retornar_palabra()))
# print(valor_retornado * 5)
# print(retornar_palabra() * 5)
# nuevo_texto = f'{retornar_palabra()} es un animal'
# print(nuevo_texto)


# def devolver_una_lista():
#     return list(range(6))

# valores = devolver_una_lista()
# print(valores)
# print(valores[1:4])
# print(devolver_una_lista())
# print(devolver_una_lista()[1:4])

# ====================================================================
# ====================================================================

# scope ( alcance )

# valor1 = 4

# def sumar_numeros():
#     # print(valor1)
#     # global valor1
#     # valor1 = 15
#     # print(valor1)
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3

# valor1 = 4

# suma_de_valores = sumar_numeros()

# print(valor1)
# # print(valor2)

# # valor1 = 4

# print(suma_de_valores)

# ====================================================================
# ====================================================================

# def suma(valor1, valor2):
#     return valor1 + valor2

# print(suma(15, 16))
# valor1 = 15
# valor2 = 15
# print(suma(valor1, valor2))

# ====================================================================
# ====================================================================

# lista = [1,2,3,4,5,7,1,1,5,21,5,2,2,3,4,25,2]
# tupla = (1,2,3,4,5,7,1,1,5,21,5,2,2,3,4,25,2)

# print(sum(lista))

# def mi_sum(coleccion_de_valores):
#     suma = 0
#     for valor in coleccion_de_valores:
#         # print('Sumando el valor', valor)
#         suma += valor
#     return suma
#     # print(suma)

# print(mi_sum(lista))
# print(mi_sum(tupla))
# mi_sum(lista)

# ====================================================================
# ====================================================================

# print(len('Hola'))
# print(len('ricardo lo mas'))

# # cant_letras = 0
# # for letra in 'Hola':
# #     cant_letras += 1
    
# # print(cant_letras)

# def contame_las_letras(palabras_a_contar): # snake_case
#     cant_letras = 0
#     for letra in palabras_a_contar:
#         cant_letras += 1
#     return cant_letras

# print(contame_las_letras('Hola'))
# print(contame_las_letras('ricardo lo mas'))

# ====================================================================
# ====================================================================

# def desordeno_tus_argumentos(param1, param2, param3, param4, param5):
#     # tupla = (param3, param5, param4, param1, param2)
#     # return tupla
#     return param3, param5, param4, param1, param2

# valor1 = 1
# print(desordeno_tus_argumentos(valor1,2,3,4,5))
# primero, segundo, tercero, cuarto, quinto = desordeno_tus_argumentos(valor1,2,3,4,5)

# # primero, segundo, tercero, cuarto, quinto = (1,2,3,4,5)
# print(primero)
# # print(segundo)
# # print(tercero)
# # print(cuarto)
# # print(quinto)

# ====================================================================
# ====================================================================

# Momentos de una funcion
# definimos la funcion
# llamo a la funcion ejecuta su codigo
# revisa si tiene un return
# si no tiene un return devuelve None por defecto
# si tiene un return devuelve lo que tiene a continuacion el return

# ====================================================================
# ====================================================================

# Ej - Par o Impar
# Realizar una función llamada par_o_impar:

# Recibirá un número por parámetro
# Imprimirá Par si el número es par
# Imprimirá Impar si el número es impar
# Si se ingresa algo que no sea número debe indicar que se ingrese un número. (Para los más audaces) 


# ====================================================================
# ====================================================================

# Desafio - Año Bisiesto

# ====================================================================
# ====================================================================
# 
# Realizar una función llamada anio_bisiesto:

# Recibirá un año por parámetro
# Imprimirá “El año es bisiesto” si el año es bisiesto
# Imprimirá “El año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

# Información a tener en cuenta:

# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
# aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 
# 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
