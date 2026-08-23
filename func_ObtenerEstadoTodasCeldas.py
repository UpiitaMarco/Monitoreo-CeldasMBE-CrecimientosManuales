# Función para obtener el estado actual de todas las Celdas.

# Librerías necesarias:
from snap7 import util
from datetime import datetime
from babel.dates import format_date

# Importando funciones:
from func_DiccionarioElemento import DiccionarioElemento

def ObtenerEstadoTodasCeldas(plc):
    # Definiendo la lista para la operación de la función:
    FechaEstado = format_date(datetime.now(), 'dd-MMM-yyyy', locale = 'es_MX')
    TiempoEstado = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    # Núm. Medición, Fecha, Hora
    # Formato para mostrar el mes en el locale 'es_MX' (para que aparezca en español correctamente) obtenido de https://babel.pocoo.org/en/latest/dates.html (vía https://stackoverflow.com/questions/985505/locale-date-formatting-in-python)
    EstadoTodasCeldas = ['x', FechaEstado, TiempoEstado]

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
            EstadoTodasCeldas.append('Cerrado')
        # Segundo caso: Si el Sensor Abierto esta activado y el Sensor Cerrado esta desactivado:
        elif valorEstadoSensorAbierto == True and valorEstadoSensorCerrado == False:
            # Significa que la Celda se encuentra abierta.
            EstadoTodasCeldas.append('Abierto')
        # Tercer caso: Si tanto el Sensor Abierto como el Sensor Cerrado estan activados:
        elif valorEstadoSensorAbierto == True and valorEstadoSensorCerrado == True:
            # Significa que la Celda se encuentra en un estado no válido.
            EstadoTodasCeldas.append('No Válido')
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
                EstadoTodasCeldas.append('Apertura')
            # Segundo caso: Si `datoEstAbriendo` es Falso y `datoEstCerrando` es Verdadero:
            elif valorEstAbriendo == False and valorEstCerrando == True:
                # Significa que está en un estado de transición de Cierre.
                EstadoTodasCeldas.append('Cierre')
            # Tercer caso: Si tanto `datoEstAbriendo` como `datoEstCerrando` son Falsos:
            elif valorEstAbriendo == False and valorEstCerrando == False:
                # Significa que está en un estado de transición pero en el momento de la lectura no se sabe cuál es. 
                # Esto ocurre cuando la Apertura y/o Cierre de la Celda es Manual.
                EstadoTodasCeldas.append('Transición')
            # Cuarto y último caso: Si tanto `datoEstAbriendo` como `datoEstCerrando` son Verdaderos:
            elif valorEstAbriendo == True and valorEstCerrando == True:
                # Significa que está en un estado de transición inválido.
                EstadoTodasCeldas.append('Transición Inválida')

    # 3. Una vez terminó de obtener el estado de todas las celdas, se devuelve la lista de información final:
    return EstadoTodasCeldas