import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from inicialization import initialization_zdt3, window, calcular_vecinos
from zdt3 import zdt3
from reproduction import reproduction_zdt3, actualization_z, actualization_population_zdt3

def leer_archivo(archivo):
    variables = []

    with open(archivo, 'r') as file:
        for linea in file:
            variables.append(linea)   
    
    return variables

if len(sys.argv) > 1:
    archivo = sys.argv[1]
    try:
        subproblemas, generaciones, vecindad, limite_inferior, limite_superior, dimensiones, factor_cruce, factor_mutacion = leer_archivo(archivo)
        subproblemas, generaciones, vecindad, limite_inferior, limite_superior, dimensiones, factor_cruce, factor_mutacion = int(subproblemas), int(generaciones), float(vecindad), float(limite_inferior), float(limite_superior), int(dimensiones), float(factor_cruce), float(factor_mutacion)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
else:
    subproblemas = int(input("Ingrese un valor para número de subproblemas (individuos): "))
    generaciones = int(input("Ingrese un valor para numero de generaciones: "))
    vecindad = float(input("Ingrese un valor para vecindad: "))
    limite_inferior = float(input("Ingrese un valor para el límite inferior: "))
    limite_superior = float(input("Ingrese un valor para el limite superior: "))
    dimensiones = int(input("Ingrese un valor para dimensiones: "))
    factor_cruce = int(input("Ingrese un valor para el factor de cruce: "))
    factor_mutacion = int(input("Ingrese un valor para el factor de mutacion: "))


z = [None, None]
vectores_lambda = window(subproblemas)
population_list = initialization_zdt3(subproblemas, limite_inferior, limite_superior, dimensiones)

evaluated_functions = []
vecindades = calcular_vecinos(vectores_lambda, vecindad)

for x in population_list:
    f1, f2 = zdt3(x, dimensiones)
    evaluated_functions.append([f1, f2])

for f in evaluated_functions:
    z = actualization_z(z, f)


for generacion in range(generaciones):
    print("Generacion "+ str(generacion)+ " con Z: " + str(z))

    for individuo in range(len(population_list)):
        vecindad_individuo = list(vecindades.items())[individuo][1]
        nuevo_individuo = reproduction_zdt3(population_list[individuo], vecindad_individuo, limite_superior, limite_inferior, dimensiones, population_list, factor_cruce, factor_mutacion)
        f1, f2 = zdt3(nuevo_individuo, dimensiones)
        z = actualization_z(z, [f1, f2])
        population_list = actualization_population_zdt3(vecindad_individuo, nuevo_individuo, population_list, dimensiones, z, [f1, f2])

def funcion_zdt(x):
    return 1 - math.sqrt(x) - x * math.sin(10 * math.pi * x)

# Crea un conjunto de puntos x en el rango [0, 1]
x = np.linspace(0, 1, 400)

# Calcula la función a trozos en cada punto de x
y = [funcion_zdt(xi) for xi in x]

# Dibuja la función a trozos
plt.plot(x, y, label='Función a Trozos', color='blue')

valores_finales = []
for i in range(len(population_list)):
    f1, f2 = zdt3(population_list[i], dimensiones)
    print(f"Individuo {i} tiene los valores de funciones {f1}, {f2}")
    valores_finales.append((f1, f2))
       
x, y = zip(*valores_finales)

plt.plot(x, y, marker='o', linestyle='', color='green', label='Puntos')

plt.xlabel('f1')
plt.ylabel('f2')
plt.title('valores zdt3')

plt.legend()

# Mostrar el gráfico
plt.show()









'''
vectores_lambda = window(subproblemas)
print(vectores_lambda)

vecindades = calcular_vecinos(vectores_lambda, vecindad)

for vector in vecindades.items():
    print(str(vector[0]) + ': '+ str(vector[1]))


population_list = initialization(subproblemas, limite_inferior, limite_superior, dimensiones)

for i in population_list:
    print(i)
'''
