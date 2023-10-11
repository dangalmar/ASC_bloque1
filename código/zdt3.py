import math

def zdt3(individuo, dimensions):
    f_1 = individuo[0]
    g = 1 + 9 / (dimensions - 1) * sum(individuo[1:])
    h = 1 - (math.sqrt(f_1 / g) + f_1 / g * math.sin(10 * math.pi * f_1))
    f_2 = g * h

    return f_1, f_2