# Tarea 3.4

En una población el 20% tiene una enfermedad. El examen da positivo el 90% de las veces si la persona está enferma y el 30% si no lo está. A los que dan positivo se les da una droga que causa manchas rojas en el 20% de los pacientes. Si alguien tiene manchas, ¿cuál es la probabilidad de que haya tenido la enfermedad?

## Solución

Para resolver el problema le asignamos un nombre a cada evento. Llamamos E al evento "tiene la enfermedad", + al evento "examen positivo" y M al evento "tiene manchas". Los datos que me da el enunciado son:

- P(E) = 0.2, por lo tanto P(no E) = 0.8
- P(+|E) = 0.9
- P(+|no E) = 0.3
- P(M|+) = 0.2

Es importante notar que la droga solo se le da a quienes dan positivo, así que sin examen positivo no puede haber manchas. Además, como la probabilidad de manchas es 0.2 para cualquier positivo, no importa si está enfermo o no.

Lo que me piden es P(E|M), es decir, la probabilidad de que haya tenido la enfermedad dado que tiene manchas. Aplicamos Bayes:

P(E|M) = P(M|E) P(E) / P(M)

Para tener manchas debe dar positivo y después tener la reacción, entonces:

- P(M|E) = P(M|+) P(+|E) = 0.2 · 0.9 = 0.18
- P(M|no E) = P(M|+) P(+|no E) = 0.2 · 0.3 = 0.06

Para el denominador usamos probabilidad total:

P(M) = 0.18 · 0.2 + 0.06 · 0.8 = 0.036 + 0.048 = 0.084

Entonces:

P(E|M) = 0.036 / 0.084 = 3/7 ≈ 0.4286

## Por lo tanto:

La probabilidad de que una persona con manchas haya tenido la enfermedad es 3/7 ≈ 0.43.
