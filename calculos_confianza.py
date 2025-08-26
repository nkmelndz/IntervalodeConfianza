import math
from scipy.stats import norm

# Solicitar la cantidad de datos de la muestra
n = int(input("Ingrese la cantidad de datos de la muestra: "))
muestra = []

# Solicitar cada dato de la muestra
for i in range(n):
    dato = float(input(f"Ingrese el dato #{i+1}: "))
    muestra.append(dato)

# Solicitar el porcentaje para el intervalo de confianza
porcentaje = float(input("Ingrese el porcentaje para el intervalo de confianza (ejemplo: 95): "))

# Calcular la media
media = sum(muestra) / n

# Calcular la varianza (muestral)
varianza = sum((x - media) ** 2 for x in muestra) / (n - 1)

# Calcular la desviación estándar
desviacion_estandar = math.sqrt(varianza)

# Calcular el error típico (error estándar de la media)
error_tipico = desviacion_estandar / math.sqrt(n)

# Calcular el intervalo de confianza
alfa = 1 - porcentaje / 100
z = norm.ppf(1 - alfa / 2)
limite_inferior = media - z * error_tipico
limite_superior = media + z * error_tipico

# Mostrar resultados
print(f"\nResultados:")
print(f"Media: {media:.4f}")
print(f"Varianza: {varianza:.4f}")
print(f"Desviación estándar: {desviacion_estandar:.4f}")
print(f"Error típico: {error_tipico:.4f}")
print(f"Intervalo de confianza al {porcentaje}%: [{limite_inferior:.4f}, {limite_superior:.4f}]")
