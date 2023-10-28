import matplotlib.pyplot as plt
import numpy as np
import math


ruta_archivo_Agr= '../resultados/ZDT3_AGR/EVAL4000/P100G40/zdt3_final_popp100g40_seed03.out'
ruta_archivo_NSGAII = '../resultados/ZDT3/EVAL4000/P100G40/zdt3_final_popp100g40_seed03.out'

def funcion_zdt(x):
    return 1 - math.sqrt(x) - x * math.sin(10 * math.pi * x)

# Crea un conjunto de puntos x en el rango [0, 1]
x = np.linspace(0, 1, 400)

# Calcula la función a trozos en cada punto de x
y = [funcion_zdt(xi) for xi in x]

# Dibuja la función a trozos
plt.plot(x, y, label='Función a Trozos', color='blue')

with open(ruta_archivo_Agr, 'r') as archivo:
    f = []
    cv = []

    for linea in archivo:
        valores = linea.strip().split('  ')
        
        f.append((float(valores[0]), float(valores[1])))
        cv.append(float(valores[2]))

with open(ruta_archivo_NSGAII, 'r') as archivo:
    f_NS = []
    cv_NS = []

    next(archivo)
    next(archivo)

    for linea in archivo:
        valores = linea.strip().split('\t')[len(valores) - 100:]
        
        f_NS.append((float(valores[0]), float(valores[1])))
        cv_NS.append(float(valores[2]))

x, y = zip(*f)
plt.plot(x, y, marker='o', linestyle='', color='green', label='Puntos')

x, y = zip(*f_NS)
plt.plot(x, y, marker='o', linestyle='', color='red', label='Puntos')

plt.xlabel('f1')
plt.ylabel('f2')
plt.title('valores zdt3')

plt.legend()

# Mostrar el gráfico
plt.show()
