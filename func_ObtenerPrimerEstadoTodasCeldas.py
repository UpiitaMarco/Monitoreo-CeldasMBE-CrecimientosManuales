# Función para obtener el primer estado actual de todas las Celdas.

# Librerías necesarias:
from snap7 import Client
from snap7 import util
from datetime import datetime
from babel.dates import format_date

# Importando funciones:
from func_DiccionarioElemento import DiccionarioElemento

def ObtenerPrimerEstadoTodasCeldas(plc):
    # Definiendo las variables para la lista para la operación de la función:
    FechaPrimerEstado = format_date(datetime.now(), 'dd-MMM-yyyy', locale = 'es_MX')
    TiempoPrimerEstado = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    HoraPrimerEstado = datetime.now().strftime("%H%M")
    # Colocando los primeros tres datos de la primera lectura:
    # Núm. Medición (1 por ser la primera), Fecha, Hora
    # Formato para mostrar el mes en el locale 'es_MX' (para que aparezca en español correctamente) obtenido de https://babel.pocoo.org/en/latest/dates.html (vía https://stackoverflow.com/questions/985505/locale-date-formatting-in-python)
    PrimerEstadoTodasCeldas = [1, FechaPrimerEstado, TiempoPrimerEstado]

    # 1. Obtiene, a través de la función `DiccionarioElemento` los datos de todas las celdas:
    diccionarios = DiccionarioElemento('Todos')
    # 2. Se iteran todos los elementos de la lista para obtener los datos de cada celda:
    for dictElemento in diccionarios:
        # 2.1. Se obtiene el estado de los Sensores Abierto y Cerrado:
        # Información para el mapeo de direcciones de TIA-Portal a Python obtenida de https://python-snap7.readthedocs.io/en/latest/reading-writing.html#address-mapping.
        datoEstSensorAbierto = plc.db_read(1, dictElemento['Byte_EstSensorAbierto'], 1)
        valorEstadoSensorAbierto = util.get_bool(datoEstSensorAbierto, 0, dictElemento['Bit_EstSensorAbierto'])
        datoEstSensorCerrado = plc.db_read(1, dictElemento['Byte_EstSensorCerrado'], 1)
        valorEstadoSensorCerrado = util.get_bool(datoEstSensorCerrado, 0, dictElemento['Bit_EstSensorCerrado'])
        # 2.2. Se realizan las comprobaciones adecuadas para obtener el estado de la Celda:
        # Primer caso: Si el Sensor Abierto esta desactivado y el Sensor Cerrado esta activado:
        if valorEstadoSensorAbierto == False and valorEstadoSensorCerrado == True:
            # Significa que la Celda se encuentra cerrada.
            PrimerEstadoTodasCeldas.append('Cerrado')
        # Segundo caso: Si el Sensor Abierto esta activado y el Sensor Cerrado esta desactivado:
        elif valorEstadoSensorAbierto == True and valorEstadoSensorCerrado == False:
            # Significa que la Celda se encuentra abierta.
            PrimerEstadoTodasCeldas.append('Abierto')
        # Tercer caso: Si tanto el Sensor Abierto como el Sensor Cerrado estan activados:
        elif valorEstadoSensorAbierto == True and valorEstadoSensorCerrado == True:
            # Significa que la Celda se encuentra en un estado no válido.
            PrimerEstadoTodasCeldas.append('No Válido')
        # Cuarto y último caso: Si tanto el Sensor Abierto como el Sensor Cerrado estan desactivados:
        elif valorEstadoSensorAbierto == False and valorEstadoSensorCerrado == False:
            # Significa que la Celda se encuentra en un estado de transición (Apertura o Cierre).
            # 2.3.1 Para obtener el estado de transición correcto se harán lecturas en sus variables correspondientes del PLC:
            datoEstAbriendo = plc.db_read(1, dictElemento['Byte_EstAbriendo'], 1)
            valorEstAbriendo = util.get_bool(datoEstAbriendo, 0, dictElemento['Bit_EstAbriendo'])
            datoEstCerrando = plc.db_read(1, dictElemento['Byte_EstCerrando'], 1)
            valorEstCerrando = util.get_bool(datoEstCerrando, 0, dictElemento['Bit_EstCerrando'])
            # 2.3.2 Se realizan las comprobaciones adecuadas para obtener el estado de transición.
            # Primer caso: Si `datoEstAbriendo` es Verdadero y `datoEstCerrando` es Falso:
            if valorEstAbriendo == True and valorEstCerrando == False:
                # Significa que está en un estado de transición de Apertura.
                PrimerEstadoTodasCeldas.append('Apertura')
            # Segundo caso: Si `datoEstAbriendo` es Falso y `datoEstCerrando` es Verdadero:
            elif valorEstAbriendo == False and valorEstCerrando == True:
                # Significa que está en un estado de transición de Cierre.
                PrimerEstadoTodasCeldas.append('Cierre')
            # Tercer caso: Si tanto `datoEstAbriendo` como `datoEstCerrando` son Falsos:
            elif valorEstAbriendo == False and valorEstCerrando == False:
                # Significa que está en un estado de transición pero en el momento de la lectura no se sabe cuál es. 
                # Esto ocurre cuando la Apertura y/o Cierre de la Celda es Manual.
                PrimerEstadoTodasCeldas.append('Transición')
            # Cuarto y último caso: Si tanto `datoEstAbriendo` como `datoEstCerrando` son Verdaderos:
            elif valorEstAbriendo == True and valorEstCerrando == True:
                # Significa que está en un estado de transición inválido.
                PrimerEstadoTodasCeldas.append('Transición Inválida') 

    # 3. Una vez terminó de obtener el estado de todas las celdas, se devuelve la lista de información final junto con la fecha y hora del primer estado:
    return PrimerEstadoTodasCeldas, FechaPrimerEstado, HoraPrimerEstado

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