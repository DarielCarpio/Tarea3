from matplotlib import colors
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import os

#Actualizacion

dato = pd.read_csv("avocado.csv");
aguacate = pd.Series(dato['AveragePrice'])
 
def menu():
        os.system('clear')
        print ("Selecciona una opción")
        print ("\t1 - Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos")
        print ("\t2 - Mostrar los primeros 100 registros")
        print ("\t3 - Mostrar los últimos 20 registros")
        print ("\t4 - Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos")
        print ("\t5 - Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones")
        print ("\t6 - salir")
 
 
while True:
        menu()
        opcionMenu = input("inserta un numero valor >> ")
 
        if opcionMenu=="1":
            print ("Los datos y columna son ", dato.shape)
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
            print ("Los primero 100 registro son ", dato.head(100))
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            print ("Los ultimo 20 registro son ", dato.tail(20))
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        elif opcionMenu=="4":
            print ("Precio minimo ", aguacate.min())
            print ("Precio mayor ", aguacate.max())
            print ("Precio promedio ", aguacate.mean())
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")
        elif opcionMenu=="5":
            primeraRegion = dato[dato["region"] == "SanFrancisco"]
            segundaRegion = dato[dato["region"] == "SanDiego"]
            terceraRegion = dato[dato["region"] == "Atlanta"]

            x = plt.subplot()
            g_primeraRegion = primeraRegion.plot(x = "year", y = "AveragePrice", kind = "scatter", color = "red", ax = x)
            g_segundaRegion = segundaRegion.plot(x = "year", y = "AveragePrice", kind = "scatter", color = "yellow", ax = x)
            g_terceraRegion = terceraRegion.plot(x = "year", y = "AveragePrice", kind = "scatter", color = "blue", ax = x)

            plt.show()

            print ("Grafico tipo scatter ", )
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")
        elif opcionMenu=="6":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
