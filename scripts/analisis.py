import csv
import math
from pathlib import Path

# Práctica Individual N° 2
# Análisis del tiempo de espera de clientes en una fila de atención.

BASE = Path(__file__).resolve().parents[1]
ARCHIVO_DATOS = BASE / "datos" / "datos.csv"
ARCHIVO_REPORTE = BASE / "reporte" / "informe.txt"

def media(valores):
    return sum(valores) / len(valores)

def mediana(valores):
    datos = sorted(valores)
    n = len(datos)
    mitad = n // 2
    if n % 2 == 0:
        return (datos[mitad - 1] + datos[mitad]) / 2
    return datos[mitad]

def varianza_muestral(valores):
    m = media(valores)
    return sum((x - m) ** 2 for x in valores) / (len(valores) - 1)

def desviacion_muestral(valores):
    return math.sqrt(varianza_muestral(valores))

with open(ARCHIVO_DATOS, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    valores = [float(fila["tiempo_espera_min"]) for fila in lector]

n = len(valores)
m = media(valores)
med = mediana(valores)
var = varianza_muestral(valores)
desv = desviacion_muestral(valores)
minimo = min(valores)
maximo = max(valores)
rango = maximo - minimo

# Criterio solicitado: un dato es outlier si |Z| > 3.
outliers = []
for i, x in enumerate(valores, start=1):
    z = (x - m) / desv
    if abs(z) > 3:
        outliers.append((i, x, z))

print("=== ANÁLISIS DE LA PRÁCTICA 2 ===")
print(f"Observaciones: {n}")
print(f"Media: {m:.2f} min")
print(f"Mediana: {med:.2f} min")
print(f"Mínimo: {minimo:.2f} min")
print(f"Máximo: {maximo:.2f} min")
print(f"Rango: {rango:.2f} min")
print(f"Varianza muestral: {var:.2f} min²")
print(f"Desviación estándar muestral: {desv:.2f} min")
print("\nOutliers (|Z| > 3):")
if outliers:
    for fila, x, z in outliers:
        print(f"Cliente {fila}: {x:.2f} min, Z = {z:.2f}")
else:
    print("No se detectaron outliers.")

# El informe incluido en el repositorio ya contiene estos resultados.
# El script permite repetir el análisis si se modifican los datos.
