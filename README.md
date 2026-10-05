# Práctica Individual N° 2

## Formulación y análisis preliminar de un sistema real

**Estudiante:** Kevin Mauricio Espinoza Vera

### Caso
Análisis del tiempo de espera de clientes en una fila de atención al cliente de una tienda.

### Contenido del repositorio

```text
practica2_apEspinoza_Kevin/
├── datos/
│   └── datos.csv
├── scripts/
│   └── analisis.py
├── reporte/
│   └── informe.txt
└── README.md
```

### Datos

Se utilizaron 30 observaciones simuladas de tiempo de espera, expresadas en minutos.

### Análisis

El script `scripts/analisis.py` calcula:

- Número de observaciones.
- Media.
- Mediana.
- Mínimo y máximo.
- Rango.
- Varianza muestral.
- Desviación estándar muestral.
- Z-Score de cada observación.
- Valores atípicos mediante el criterio `|Z| > 3`.

### Ejecución

Desde la carpeta raíz del repositorio:

```bash
python scripts/analisis.py
```

No se requieren librerías externas; el análisis utiliza únicamente módulos incluidos en Python.

### Resultado principal

Media: 6.55 minutos  
Mediana: 5.75 minutos  
Desviación estándar muestral: 4.57 minutos  
Outliers detectados: 1

### Observación

Los datos son simulados y se utilizan exclusivamente para la práctica académica.
