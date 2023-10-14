import math

def zdt3(individual, dimensions):
    f_1 = individual[0]
    g = 1 + (9 / (dimensions - 1)) * sum(individual[1:])
    h = 1 - (math.sqrt(f_1 / g) + (f_1 / g) * math.sin(10 * math.pi * f_1))
    f_2 = g * h

    return f_1, f_2