import math

def cf6(individuo, dimensions):
    J1 = [j for j in range(len(individuo)) if j%2==1 and 2<=j<=len(individuo)]
    J2 = [j for j in range(len(individuo)) if j%2==0 and 2<=j<=len(individuo)]

    y1 = [individuo[j] - 0.8*individuo[0]*math.cos(6*math.pi*individuo[0] + j*math.pi/len(individuo)) for j in J1]
    y2 = [individuo[j] - 0.8*individuo[0]*math.sin(6*math.pi*individuo[0] + j*math.pi/len(individuo)) for j in J1]
    
    f_1 = individuo[0] + sum(y1**2)
    f_2 = (1 - individuo[0]**2) + sum(y2**2)

    return f_1, f_2