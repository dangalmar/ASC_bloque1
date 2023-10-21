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
lista_f1 = []
lista_f2 = []
lista_cv = []
vectores_lambda = window(subproblemas)
population_list = initialization_zdt3(subproblemas, limite_inferior, limite_superior, dimensiones)

evaluated_functions = []
vecindades = calcular_vecinos(vectores_lambda, vecindad)

for x in population_list:
    f1, f2 = zdt3(x, dimensiones)
    lista_f1.append(f1)
    lista_f2.append(f2)
    lista_cv.append(0.0)
    evaluated_functions.append([f1, f2])

for f in evaluated_functions:
    z = actualization_z(z, f)


for generacion in range(generaciones - 1):
    print("Generacion "+ str(generacion)+ " con Z: " + str(z))

    for individuo in range(len(population_list)):
        vecindad_individuo = list(vecindades.items())[individuo][1]
        nuevo_individuo = reproduction_zdt3(population_list[individuo], vecindad_individuo, limite_superior, limite_inferior, dimensiones, population_list, factor_cruce, factor_mutacion)
        f1, f2 = zdt3(nuevo_individuo, dimensiones)
        lista_f1.append(f1)
        lista_f2.append(f2)
        lista_cv.append(0.0)
        z = actualization_z(z, [f1, f2])
        population_list = actualization_population_zdt3(vecindad_individuo, nuevo_individuo, population_list, dimensiones, z, [f1, f2])

lista_f1_final = []
lista_f2_final = []
lista_cv_final = []
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
    lista_f1_final.append(f1)
    lista_f2_final.append(f2)
    lista_cv_final.append(0.0)
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
ruta_archivo_all = '../resultados/ZDT3_AGR/EVAL4000/P100G40/zdt3_all_popmp100g40_seed10.out'
ruta_archivo_final = '../resultados/ZDT3_AGR/EVAL4000/P100G40/zdt3_final_popp100g40_seed10.out'

with open(ruta_archivo_all, 'w') as archivo:
    for f1, f2, cv in zip(lista_f1, lista_f2, lista_cv):
        archivo.write(f"{f1:0.6e}   {f2:0.6e}   {cv:0.6e} \n")

with open(ruta_archivo_final, 'w') as archivo:
    for f1, f2, cv, individuo in zip(lista_f1, lista_f2, lista_cv, population_list):
        archivo.write(f"{f1:0.6e}   {f2:0.6e}   ")
        for alelo in individuo:
            archivo.write(f"{alelo:0.6e}    ")
        archivo.write(f"{cv:0.6e} \n")

print("\n Los datos se han escrito en", ruta_archivo_all, ruta_archivo_final)
'''





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
