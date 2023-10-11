import sys
from inicialization import initialization, window, calcular_vecinos

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
    

vectores_lambda = window(subproblemas)
#print(vectores_lambda)

vecindades = calcular_vecinos(vectores_lambda, vecindad)
'''
for vector in vecindades.items():
    print(str(vector[0]) + ': '+ str(vector[1]))
'''

population_list = initialization(subproblemas, limite_inferior, limite_superior, dimensiones)

for i in population_list:
    print(i)
