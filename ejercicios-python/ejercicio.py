#!/usr/bin/python
# -*- coding: utf-8 -*-

# Paso 1: Almacenar nuestros datos
nombres = [
    ["Eurídice Granados", "sandra.euridice@gmail.com"],
    ["Pablo Duarte", "pablocyan@yahoo.com.mx"],
    ["Juan Lago", "juan.l33@gmail.com"],
    ["Margarita Calderon", "cavamaga2708@gmail.com"],
    ["Ericka Morales", "erymor@yahoo.com.mx"]
]

# Paso 2: Imprima la lista en orden alfabético
# con nombre y email

# Ordeamos la lista con la instrucción .sort()
nombres.sort()

for nom in nombres:
    print(nom)

# Paso 3: Imprima la lista con sólo el nombre
# pero indique cuantas letras tiene cada nombre
print() # Colocar una línea en blanco
print("Cantidad de letras")
print()

for dato in nombres:
   caracteres = len(dato[0])-1
   print (dato[0] + " " + str(caracteres))

# Paso 4: Imprima la lista con sólo el dominio
# del email, en otras palabras imprima la lista
# de los dominios de donde provienen las emails
print()
print("Dominios:")
print()

for nom in nombres:
    # El primer 1 es para elegir el email de
    # cada usuario
    # El segundo 1 es para elegir el dominio de
    # cada email
    dominio = nom[1].split("@")[1]
    print(dominio)
