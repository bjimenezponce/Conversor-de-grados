

#kelvin = 0 - 273.15
#centi = 0  + 273.15

import os


while True:

    numero = int(input(" menu principal: \n 1:- convertir de grados centigrados a kelvin \n 2:- convertir de grados kelvin a centigrados \n 3:- salir \n "))

    if numero == 1:
        print("ingrese los grados que quiere convertir en K°")
        valoeConversion = 273.15
        centi = float(input())
        print(" el resultado es")
        print(float(centi) + float(valoeConversion))

    elif numero == 2:
        print("ingrese los grados que quiere convertir en C°")
        valoeConversion = 273.15
        kelvin = float(input())
        print(" el resultado es")
        print(float(kelvin) - float(valoeConversion))

    elif numero == 3:
        print("te esperamos pronto, feliz dia :) ")

    input()
    os.system("cls")
