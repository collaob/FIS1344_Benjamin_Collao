#Tarea 1.1 Benjamín Collao
d = 2 #definimos variables
t = 0.3
a = 9.81
def velocidad_inicial(d, t, a):
    v0 = (d - 0.5 * a * t**2) / t #definimos la funcion que calcula la velocidad inicial
    return v0 #responde el valor
print("La velocidad inicial es:", velocidad_inicial(d, t, a)) #imprimimos el resultado de la funcion
