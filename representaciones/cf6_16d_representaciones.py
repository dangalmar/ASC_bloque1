import matplotlib.pyplot as plt
import numpy as np
import math


ruta_archivo_Agr= '../resultados/CF6_16D_AGR/EVAL4000/P100G40/cf6_16d_selection_final_popp100g40_seed01.out'
ruta_archivo_NSGAII = '../resultados/CF6_16D/EVAL4000/P100G40/cf6_16d_final_popp100g40_seed01.out'

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
