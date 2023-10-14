import math

def cf6(individual, dimensions):
    J1 = [j for j in range(dimensions + 1) if j%2==1 and 2<=j]
    J2 = [j for j in range(dimensions + 1) if j%2==0 and 2<=j]

    y1 = [(individual[j-1] - 0.8*individual[0]*math.cos(6*math.pi*individual[0] + j*math.pi/dimensions))**2 for j in J1]
    y2 = [(individual[j-1] - 0.8*individual[0]*math.sin(6*math.pi*individual[0] + j*math.pi/dimensions))**2 for j in J2]
    
    f_1 = individual[0] + sum(y1)
    f_2 = (1 - individual[0])**2 + sum(y2)

    return f_1, f_2

def cf6_constraint_1(individual, dimensions):
    x_1 = individual[0]
    x_2 = individual[1]
    n = dimensions
    sign = sign_func(0.5 * (1 - x_1) - (1 - x_1)**2)
    squart = math.sqrt(abs(0.5 * (1 - x_1) - (1 - x_1)**2))
    contraint_value = x_2 - 0.8 * x_1 *math.sin(6 * math.pi * x_1 + (2 * math.pi / n)) - sign * squart

    if contraint_value >= 0:
        return 0
    
    return contraint_value


def cf6_constraint_2(individual, dimensions):
    x_1 = individual[0]
    x_4 = individual[3]
    n = dimensions
    sign = sign_func(0.25 * math.sqrt(1 - x_1) - 0.5 * (1 - x_1))
    squart = math.sqrt(abs(0.25 * math.sqrt(1 - x_1) - 0.5 * (1 - x_1)))
    contraint_value =  x_4 - 0.8 * x_1 *math.sin(6 * math.pi * x_1 + (4 * math.pi / n)) - sign * squart

    if contraint_value >= 0:
        return 0
    
    return contraint_value

def sign_func(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0