import sys
import matplotlib.pyplot as plt
from inicialization import initialization, window, calcular_vecinos
from zdt3 import zdt3
from reproduction import reproduction, actualization_z, actualization_population

def leer_archivo(archivo):
    variables = []

    with open(archivo, 'r') as file:
        for linea in file:
            variables.append(linea)   
    
    return variables

if len(sys.argv) > 1:
    archivo = sys.argv[1]
    try:
        subproblemas, generaciones, vecindad, limite_inferior, limite_superior, dimensiones = leer_archivo(archivo)
        subproblemas, generaciones, vecindad, limite_inferior, limite_superior, dimensiones = int(subproblemas), int(generaciones), float(vecindad), float(limite_inferior), float(limite_superior), int(dimensiones)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
else:
    subproblemas = int(input("Ingrese un valor para número de subproblemas (individuos): "))
    generaciones = int(input("Ingrese un valor para numero de generaciones: "))
    vecindad = float(input("Ingrese un valor para vecindad: "))
    limite_inferior = float(input("Ingrese un valor para el límite inferior: "))
    limite_superior = float(input("Ingrese un valor para limite_superior: "))
    dimensiones = int(input("Ingrese un valor para dimensiones: "))


z = [None, None]
vectores_lambda = window(subproblemas)
population_list = initialization(subproblemas, limite_inferior, limite_superior, dimensiones)

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
        nuevo_individuo = reproduction(population_list[individuo], vecindad_individuo, limite_superior, limite_inferior, dimensiones, population_list)
        f1, f2 = zdt3(nuevo_individuo, dimensiones)
        evaluated_functions.append([f1, f2])
        z = actualization_z(z, [f1, f2])
        population_list = actualization_population(vecindad_individuo, nuevo_individuo, population_list, dimensiones, z, [f1, f2])

valores_finales = []
for i in range(len(population_list)):
    f1, f2 = zdt3(population_list[i], dimensiones)
    print(f"Individuo {i} tiene los valores de funciones {f1}, {f2}")
    valores_finales.append((f1, f2))
       
x, y = zip(*valores_finales)

plt.plot(x, y, marker='o', linestyle='', color='blue', label='Puntos')

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
