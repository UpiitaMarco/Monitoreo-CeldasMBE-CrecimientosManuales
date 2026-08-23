# Función que compara la lectura dada con la última en el archivo .csv y decide si agregarla o no.

# Librerías necesarias:
from snap7 import Client
import time
import csv

# Importando funciones:
from func_ObtenerPrimerEstadoTodasCeldas import ObtenerPrimerEstadoTodasCeldas
from func_CrearArchivoCSVPrimeraLectura import CrearArchivoCSVPrimeraLectura
from func_ObtenerEstadoTodasCeldas import ObtenerEstadoTodasCeldas

def CompararLecturaArchivoCSV(NombreArchivoCSV, EstadoTodasCeldas):
    # 1. Abre el Archivo CSV y extrae la última lectura agregada:
    with open(NombreArchivoCSV, 'r', encoding = 'utf-8') as csvfile:
        # 1.1. Leyendo la última fila del archivo .csv. Obtenido de https://stackoverflow.com/a/65708623.
        ultimaLectura = csvfile.readlines()[-1].split(',')
    # 1.2. Limpiando el último elemento de la lista para que no tenga el caracter '\n'.
    # Obtenido de https://stackoverflow.com/a/275025.
    ultimaLectura[-1] = ultimaLectura[-1].rstrip()
    # 2. Realiza la comparación entre las listas desde el cuarto elemento al último (estado de las Celdas):
    hayDiferencia = False
    for i in range (3,12):
        # Si hay alguna diferencia:
        if EstadoTodasCeldas[i] != ultimaLectura[i]:
            # Se cambia el valor de la bandera y sale de la comparación:
            hayDiferencia = True
            break
    # 3. Evalúa el resultado de la comparación.
    # Si existió alguna diferencia:
    if hayDiferencia == True:
        # Esta nueva lectura se agrega al registro.
        # 3.1. Se obtiene el Número de Lectura de la última lectura del registro y se agrega a la nueva lectura incrementandola en 1:
        EstadoTodasCeldas[0] = int(ultimaLectura[0]) + 1
        # 3.2. Se escribe la lectura en el Archivo .csv:
        # Obtenido de https://www.geeksforgeeks.org/python/how-to-append-a-new-row-to-an-existing-csv-file/.
        with open(NombreArchivoCSV, 'a', encoding = 'utf-8', newline = '') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(EstadoTodasCeldas)
    # Si no existió ninguna diferencia, esta nueva lectura no es agregada al registro.
    

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
                nombreArchivoCSV = CrearArchivoCSVPrimeraLectura(PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado)
                for i in range(100):
                    print(f'Lectura No. {i}')
                    time.sleep(.1)
                    EstadoTodasCeldas = ObtenerEstadoTodasCeldas(plc)
                    CompararLecturaArchivoCSV(nombreArchivoCSV, EstadoTodasCeldas)

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