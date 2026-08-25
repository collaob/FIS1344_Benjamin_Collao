#Tarea 1
d = 2 #definimos variables
t = 0.3
a = 9.81
def velocidad_inicial(d, t, a):
    v0 = (d - 0.5 * a * t**2) / t #definimos la funcion que calcula la velocidad inicial
    return v0 #responde el valor
print("La velocidad inicial es:", velocidad_inicial(d, t, a)) #imprimimos el resultado de la funcion
#Tarea 2
for i in range(1, 9): #for permite repetir en un intervalo 
    print(i * "1")  #imprime i veces el string "1" debe ir en comillas sino no imprime lo requerido
#Tarea 3
while True: #loop infinito hasta que se cumpla la condicion de salida
    texto = input("Ingrese un texto (o 'salir' para terminar): ") #guarda el texto que el usuario ingresa
    if texto == "salir": #condiciona la salida con el strig "salir", es decir si el ususario ingresa esa palabra el loop se rompe con break, en caso contrario el codigo vuelve a pedir un texto
        print("Programa terminado.")
        break
#Tarea 4
def sumatoria(): #definimos la funcion
    resultado = 0 #el resultado parte de 0
    for n in range (0, 101): #se considera hasta el 101 porque el rango se define por posición y parte con 0 no con 1, es decir si se define hasta 100 calcula hasta 99
        for m in range (0, n + 1): #el rango de m es hasta n+1 porque el rango se define por posición y parte con 0 no con 1, es decir si se define hasta n calcula hasta n-1
            resultado += (0.3**n)**m #el resultado suma los valores 
    return resultado
print ("Resultado de la sumatoria:", sumatoria()) #imprime el resultado de la funcion
#Tarea 5
import math

from sympy import euler #importamos la libreria math 
def sumatoria_euler(tolerancia = 1e-2): #definimos la funcion con un parametro de tolerancia
    resultado = 0 
    n = 0
    while True: #loop infinito hasta que se cumpla la condicion de salida
        resultado += (1 / math.factorial(n)) #el resultado suma los valores
        error = abs(math.exp(1) - resultado) #calcula el error absoluto entre el valor de e y el resultado
        if error < tolerancia: #condiciona la salida con el valor de tolerancia, es decir si el error es menor a la tolerancia el loop se rompe con break, en caso contrario el codigo vuelve a calcular el resultado
            break #salir del loop
        n += 1 #incrementa el valor de n en 1   
    return resultado #responde el valor
euler_aproximado = sumatoria_euler() #guarda el resultado de la funcion en una variable
print("Euler aproximado:", euler_aproximado) #imprime el resultado de la funcion
print("Error de euler:", abs(math.exp(1) - euler_aproximado)) #imprime el error absoluto entre el valor de e y el resultado