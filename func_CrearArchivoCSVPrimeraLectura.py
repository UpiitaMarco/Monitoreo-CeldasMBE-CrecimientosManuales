# Función para crear el archivo .csv y guardar la primera lectura del monitoreo.

# Importando funciones:
from func_ObtenerPrimerEstadoTodasCeldas import ObtenerPrimerEstadoTodasCeldas

# Librerías necesarias:
import csv
from snap7 import Client

def CrearArchivoCSVPrimeraLectura(PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado):
    # 1. Se crea el archivo .csv a generar a través de la fecha y la hora del primer estado:
    nombreArchivoCSV = 'RegistroMonitoreo_' + FechaPrimerEstado + '_' + HoraPrimerEstado + '.csv'
    # Información para crear el archivo .csv obtenida de https://www.geeksforgeeks.org/python/working-csv-files-python/.
    Encabezado = ['Num. Lectura', 'Fecha', 'Hora', 'Al', 'Ga', 'N', 'In', 'As', 'Be', 'Mn', 'Si', 'Mg']
    with open(nombreArchivoCSV, 'w', encoding = 'utf-8', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(Encabezado)
        # 2. Se guarda la información de la primera lectura del monitoreo.
        csvwriter.writerow(PrimerEstadoTodasCeldas)
    # 3. Finalmente, devuelve el nombre del archivo para su uso en futuras funciones:
    return nombreArchivoCSV

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
                PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado = ObtenerPrimerEstadoTodasCeldas(plc)
                print(PrimerEstadoTodasCeldas)
                CrearArchivoCSVPrimeraLectura(PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado)

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