#Tarea 6

#Tarea 7
import math

def sumatoria_sin_loop():
    return sum(map(lambda n: math.exp(n) * (n + 1), range(1, 101))) #retornamos las funciones en un rango de 1 a 101

resultado = sumatoria_sin_loop() #guardamos el resultado 
print(resultado) 

#Tarea 8
import numpy as np #importamos los modulos
import math
import matplotlib.pyplot as plt 

def f(x):
    return x * np.sin(x) #funcion original
k = 0
def serie_taylor(x, n_terminos=10):
    for k in range (0,10):
        return sum(((-1)**k)*(x**(2*k + 2))) / math.factorial(2*k + 1) #aproximación con taylor hasta el termino 10
x = np.linspace(-6, 6, 100)
y_original = f(x)
y_taylor = serie_taylor(x)

plt.figure(figsize=(10,6))
plt.plot(x, y_original, label = 'f(x)', color = 'blue', linestyle='-', linewith=2)
plt.plot(x, y_taylor, label = 'aproximación de taylor', color = 'red', linestyle='-', linewith=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparación de funciones')
plt.legend()
plt.show()