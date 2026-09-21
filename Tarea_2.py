#Tarea 2.9 Benjamín Collao
import numpy as np 
from math import factorial

def f_obvio(x):
  return (np.exp(x) - 1) / x

def f_taylor(x):
  suma = 0
  for k in range (8): #ciclo for para la serie de yailor hasta el termino 8
    suma += x**k / factorial(k+1)
  return suma

def kappa(x):
  if x == 0:
    return 0 
  num = (x-1)*np.exp(x) + 1
  den = np.exp(x) -1
  return abs(num/den)

#condicionamiento
print("condicionamiento de f [-1,1]")
for x in [-1, 0.5, 0, 0.5, 1]:
  print("kappa(%.1f) = %.5f" % (x, kappa(x)))
#se ve que kappa va en aumento y el maximo queda en x=1
print("maximo (aprox en x=1):", kappa(1), "\n")
#ahora comparamos los metodos
print("x obvio taylor dif relativa")
for e in range(2, 9):
    x = 10**(-e)
    a = f_obvio(x)
    b = f_taylor(x)
    dif = abs(a-b)/abs(b)
    print(f"1e-{e}   {a:.15f}   {b:.15f}   {dif:.3e}")

#conclusiones:
#kappa(1) ~ 0.58 < 1, entonces el condicionamiento está bien, el problema es que el algoritmo obvio tiene un error, 
#cuando x es pequeño e**x queda muy cercano a 1 y al calcular e**x - 1 se cancelan casi todos los digitos importantes, quedando solo el error de redondeo de punto flotante.
#La serie de Taylor no hace esta resta, por lo tanto, no pierde precisión, por eso mismo el error crece mucho menos cuando x es cada vez más chico.
#En resumen, taylor es más preciso para x ~ 0, debido a que el algoritmo obvio es numéricamtne inestable.
