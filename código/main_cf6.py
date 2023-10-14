import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from inicialization import initialization_cf6, window, calcular_vecinos
from cf6 import cf6, cf6_constraint_1, cf6_constraint_2
from reproduction import reproduction_cf6, actualization_z, actualization_population_cf6, actualization_population_cf6_selection

def leer_archivo(archivo):
    variables = []

    with open(archivo, 'r') as file:
        for linea in file:
            variables.append(linea)   
    
    return variables

if len(sys.argv) > 1:
    archivo = sys.argv[1]
    try:
        subproblemas, generaciones, vecindad, limite_inferior_1, limite_superior_1, limite_inferior_n, limite_superior_n, dimensiones, factor_cruce, factor_mutacion, violation = leer_archivo(archivo)
        subproblemas, generaciones, vecindad, limite_inferior_1, limite_superior_1, limite_inferior_n, limite_superior_n, dimensiones, factor_cruce, factor_mutacion, violation = int(subproblemas), int(generaciones), float(vecindad), float(limite_inferior_1), float(limite_superior_1), float(limite_inferior_n), float(limite_superior_n), int(dimensiones), float(factor_cruce), float(factor_mutacion), int(violation)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
else:
    subproblemas = int(input("Ingrese un valor para número de subproblemas (individuos): "))
    generaciones = int(input("Ingrese un valor para numero de generaciones: "))
    vecindad = float(input("Ingrese un valor para vecindad: "))
    limite_inferior_1 = float(input("Ingrese un valor para el límite inferior de la primera dimension: "))
    limite_superior_1 = float(input("Ingrese un valor para el límite superior de la primera dimension: "))
    limite_inferior_n = float(input("Ingrese un valor para el límite inferior de las siguientes dimensiones: "))
    limite_superior_n = float(input("Ingrese un valor para el limite superior de las siguientes dimensiones: "))
    dimensiones = int(input("Ingrese un valor para dimensiones: "))
    factor_cruce = float(input("Ingrese un valor para el factor de cruce: "))
    factor_mutacion = float(input("Ingrese un valor para el factor de mutacion: "))
    violation = int(input("Ingrese el valor para tipo de penalizacion (penalty: 0, selection: 1): "))

z = [None, None]
vectores_lambda = window(subproblemas)
population_list = initialization_cf6(subproblemas, limite_inferior_1, limite_superior_1, limite_inferior_n, limite_superior_n, dimensiones)

evaluated_functions = []
vecindades = calcular_vecinos(vectores_lambda, vecindad)

for x in population_list:
    f1, f2 = cf6(x, dimensiones)
    evaluated_functions.append([f1, f2])

for f in evaluated_functions:
    z = actualization_z(z, f)

for generacion in range(generaciones):
    print("Generacion "+ str(generacion)+ " con Z: " + str(z))

    for individuo in range(len(population_list)):
        vecindad_individuo = list(vecindades.items())[individuo][1]
        nuevo_individuo = reproduction_cf6(population_list[individuo], vecindad_individuo, limite_superior_1, limite_inferior_1, limite_inferior_n, limite_inferior_n, dimensiones, population_list, factor_cruce, factor_mutacion)
        f1, f2 = cf6(nuevo_individuo, dimensiones)
        if violation == 0:
            constraint_1, constraint_2 = cf6_constraint_1(nuevo_individuo, dimensiones), cf6_constraint_2(nuevo_individuo, dimensiones)
            valor_restriccion = abs(constraint_1) + abs(constraint_2)
            f1, f2 = f1 + 0.5 * valor_restriccion, f2 + 0.5 * valor_restriccion
            z = actualization_z(z, [f1, f2])
            population_list = actualization_population_cf6(vecindad_individuo, nuevo_individuo, population_list, dimensiones, z, [f1, f2])
        else:
            z = actualization_z(z, [f1, f2])
            population_list = actualization_population_cf6_selection(vecindad_individuo, nuevo_individuo, population_list, dimensiones, z, [f1, f2])

def funcion_a_trozos(x):
    if 0 <= x <= 0.5:
        return (1 - x)**2
    elif 0.5 < x <= 0.75:
        return 0.5 * (1 - x)
    else:
        return 0.25 * math.sqrt(1 - x)

x = np.linspace(0, 1, 400)
y = [funcion_a_trozos(xi) for xi in x]

plt.plot(x, y, label='Función a Trozos', color='blue')

valores_finales = []
for i in range(len(population_list)):
    f1, f2 = cf6(population_list[i], dimensiones)
    print(f"Individuo {i} tiene los valores de funciones {f1}, {f2}")
    valores_finales.append((f1, f2))
       
x, y = zip(*valores_finales)

plt.plot(x, y, marker='o', linestyle='', color='green', label='Puntos')

plt.xlabel('f1')
plt.ylabel('f2')
plt.title('valores cf6')

plt.legend()

# Mostrar el gráfico
plt.show()