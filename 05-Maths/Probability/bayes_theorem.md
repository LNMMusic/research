# Resumen del Teorema de Bayes

El Teorema de Bayes es un principio fundamental en la teoría de probabilidades. Se utiliza para calcular la probabilidad de un evento basándose en conocimientos previos y condiciones relacionadas. Matemáticamente, se expresa como:

$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$

Donde:
- $P(A|B)$ es la probabilidad de que ocurra el evento A dado que B es verdadero.
- $P(B|A)$ es la probabilidad de que ocurra el evento B dado que A es verdadero.
- $P(A)$ es la probabilidad de que ocurra el evento A.
- $P(B)$ es la probabilidad de que ocurra el evento B.

# Ejemplo con COVID-19 y Pruebas

Supongamos que tenemos una tabla de resultados de pruebas de COVID-19:

| Condición  | Test Positivo | Test Negativo | Total |
|------------|---------------|---------------|-------|
| COVID      | 50            | 2             | 52    |
| No COVID   | 5             | 200           | 205   |
| Total      | 55            | 202           | 257   |

## Cálculos

1. **Probabilidad Total de un Test Positivo** ($P(\text{Positivo})$):
   $P(\text{Positivo}) = \frac{\text{Total Test Positivo}}{\text{Total Personas}} = \frac{55}{257}$

2. **Probabilidad Total de tener COVID** ($P(\text{COVID})$):
   $P(\text{COVID}) = \frac{\text{Total con COVID}}{\text{Total Personas}} = \frac{52}{257}$

3. **Probabilidad de Test Positivo dado que tiene COVID** ($P(\text{Positivo}|\text{COVID})$):
   $P(\text{Positivo}|\text{COVID}) = \frac{\text{COVID y Test Positivo}}{\text{Total con COVID}} = \frac{50}{52}$

4. **Probabilidad de tener COVID dado un Test Positivo** ($P(\text{COVID}|\text{Positivo})$) usando el Teorema de Bayes:
   $P(\text{COVID}|\text{Positivo}) = \frac{P(\text{Positivo}|\text{COVID}) \times P(\text{COVID})}{P(\text{Positivo})} = \frac{\frac{50}{52} \times \frac{52}{257}}{\frac{55}{257}} = \frac{50}{55}$

Este cálculo muestra que, dada una prueba positiva, la probabilidad de tener realmente COVID-19 es $\frac{50}{55}$.
