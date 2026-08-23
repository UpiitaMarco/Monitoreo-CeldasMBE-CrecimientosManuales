# Monitoreo de las celdas del Laboratorio MBE para Crecimientos Manuales
Programa en Python que realiza el Monitoreo del movimiento de las celdas del Laboratorio MBE para Crecimientos realizados de manera Manual.

## Características:
- Registro de las celdas con un tiempo de muestreo de aproximadamente 300ms en un archivo .csv con los siguientes atributos:
    - Número de Medición
    - Fecha
    - Hora
    - Estado de las Celdas (Abierto, Cerrado, Transición, Transición Inválida) en el siguiente orden:
        1. Aluminio
        2. Galio
        3. Nitrógeno
        4. Indio
        5. Arsénico
        6. Berilio
        7. Manganeso
        8. Silicio
        9. Magnesio
    Dichos registros son evaluados con la última lectura para guardar únicamente los eventos nuevos.

## Funcionamiento:
Se ejecuta el .exe y el programa funcionará automáticamente. Para pararlo, se presiona Ctrl + C.

## Desarrollo:
Se crea el .exe utilizando PyInstaller:
```bash
python -m PyInstaller .\main.py --onefile
```