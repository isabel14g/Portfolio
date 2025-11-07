# Juego Adivina el Número 🎲

Proyecto en Python creado por Isabel Giraldo Álvarez.

## Cómo usarlo

1. Ejecuta el archivo `JuegoIsabelAdivinaNumero.py`.
2. Se mostrará un menú principal con los modos de juego:
   - Modo Solitario
   - 2 Jugadores
   - Modo Supervivencia
   - Estadísticas

## Archivos

- `JuegoIsabelAdivinaNumero.py`: menú principal del juego.
- `MenuDificultades.py`: selección de dificultad.
- `AdivinarNumero.py`: lógica de los modos de juego.
- `ModuloModosJuego.py`: conecta cada modo con sus funciones.
- `EstadisticasJuego.py`: guarda y muestra estadísticas.
- `EstadisticasJuego.xlsx`: archivo donde se registran los datos.
- `instrucciones.txt`: documentación detallada del proyecto.

## Requisitos

Este proyecto necesita las siguientes librerías de Python:

- `openpyxl` – para leer y escribir en archivos Excel (.xlsx)
- `matplotlib` – para generar gráficos de barras
- `os` – para manejo de archivos (estándar)
- `time` – para el modo Supervivencia (estándar)
- `random` – para generar números aleatorios (estándar)
- `getpass` – para ocultar el número secreto en modo 2 jugadores (estándar)

### Instalación rápida
```bash
pip install openpyxl matplotlib
```

## Créditos
Isabel Giraldo Álvarez
