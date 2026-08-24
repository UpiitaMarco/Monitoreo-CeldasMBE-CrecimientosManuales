# Función para el Monitoreo del estado de las celdas y su registro en un archivo .csv

# Librerías necesarias:
import time
from snap7 import Client
from datetime import datetime

# Importando funciones:
from func_ObtenerPrimerEstadoTodasCeldas import ObtenerPrimerEstadoTodasCeldas
from func_CrearArchivoCSVPrimeraLectura import CrearArchivoCSVPrimeraLectura
from func_ObtenerEstadoTodasCeldas import ObtenerEstadoTodasCeldas
from func_CompararLecturaArchivoCSV import CompararLecturaArchivoCSV

def Monitoreo(plc):
    # 1. Avisa al usuario que el Monitoreo ha iniciado y la instrucción para detenerlo:
    print('El Monitoreo ha iniciado.\nPara detener pulsa Ctrl + C.')
    # 2. Se obtiene el primer estado de todas las celdas:
    PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado = ObtenerPrimerEstadoTodasCeldas(plc)
    # 3. Esta primera lectura se guarda en un archivo .csv:
    nombreArchivoCSV = CrearArchivoCSVPrimeraLectura(PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado)
    # Los pasos 4 a 6 se repetirán continuamente hasta que ocurra una interrupción presionando Ctrl+C.
    try:        
        while True:
            # 4. Se espera un tiempo de muestreo propuesto de 50ms:
            time.sleep(.050)
            # 5. Se obtiene el estado de todas las celdas:
            EstadoTodasCeldas = ObtenerEstadoTodasCeldas(plc)
            # 6. Esta lectura se compara con la última guardada en el archivo .csv y decide si agregarla al registro o no:
            CompararLecturaArchivoCSV(nombreArchivoCSV, EstadoTodasCeldas)
    # Al detectar la interrupción:
    except KeyboardInterrupt:
        # 7. Avisa al usuario que el monitoreo está finalizando:
        print(f'[{datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-3]}] Finalizando Monitoreo...')
        # 8. Se desconecta la comunicación al PLC y vuelve a conectar. 
        # Esto para dar solución al error `Invalid TPTK version :2` presente en pruebas realizadas.
        plc.disconnect()
        plc.connect('192.168.0.1', 0, 1)
        # En caso de realizar la reconexión nuevamente de manera correcta:
        if plc.get_connected():
            try:
                # 9. Se obtiene el estado de las celdas por última vez:
                EstadoTodasCeldas = ObtenerEstadoTodasCeldas(plc)
                # 10. Se realiza la comparación por última vez:
                CompararLecturaArchivoCSV(nombreArchivoCSV, EstadoTodasCeldas)
            # En caso de presentar algún error en la lectura del DB:
            except Exception as error_lectura:
                print("Reconectó al PLC, pero falló al leer el DB.")
                print(f"Detalle del error: {error_lectura}")
        # En caso de fallar la reconexión: 
        else:
            print("Falló la reconexión (el PLC rechazó la petición o está apagado).")
        # Avisa al usuario que el monitoreo ha finalizado:
        print(f'[{datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-3]}] El Monitoreo ha finalizado.')

# Entorno de pruebas con la función:    
if __name__ == '__main__':
    # Crea el cliente Snap7:
    # Información para la conexión al PLC obtenida de https://python-snap7.readthedocs.io/en/latest/connecting.html#s7-1200-s7-1500-legacy-put-get.
    plc = Client()
    try:
        # Inicia la conexión:
        plc.connect('192.168.0.1', 0, 1)
        
        # Verifica si estamos conectados:
        if plc.get_connected():
            print("✅ ¡ÉXITO! Conexión establecida con el PLC.")

            try:
                Monitoreo(plc)

            except Exception as error_lectura:
                print("⚠️ Conectó al PLC, pero falló al leer el DB.")
                print("Verifica que:")
                print(f" 1. El DB exista en el PLC.")
                print(" 2. Le hayas quitado el 'Acceso optimizado al bloque'.")
                print(" 3. Hayas cargado (Download) los cambios al PLC.")
                print(f"Detalle del error: {error_lectura}")

        else:
            print("❌ Falló la conexión (el PLC rechazó la petición o está apagado).")

    except Exception as e:
        print(f"❌ Error crítico de red: {e}")
        print("Verifica que:")
        print(" 1. Tu PC tenga una IP fija en el mismo rango (ej. 192.168.0.5).")
        print(" 2. El comando 'ping' hacia el PLC funcione en tu terminal.")
        print(" 3. El PLC tenga activado 'Permitir acceso vía PUT/GET'.")

    finally:
        # 4. Cerrar la conexión (Buena práctica)
        if plc.get_connected():
            plc.disconnect()
            print("🔌 Desconectado de forma segura.")