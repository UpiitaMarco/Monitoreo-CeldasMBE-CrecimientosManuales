# Archivo principal

# Librerías necesarias:
from snap7 import Client
from time import time
from datetime import datetime

# Importando funciones:
from func_Monitoreo import Monitoreo
from func_Portada import Portada

# 1. Imprime la portada:
Portada()
# 1. Crea el cliente Snap7:
# Información para la conexión al PLC obtenida de https://python-snap7.readthedocs.io/en/latest/connecting.html#s7-1200-s7-1500-legacy-put-get.
plc = Client()
try:
    # 2. Inicia la conexión:
    plc.connect('192.168.0.1', 0, 1)
    # En caso de realizar la conexión de manera correcta:
    if plc.get_connected():
        # 3. Avisa al usuario que la conexión fué establecida de manera adecuada:
        print(f"[{datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-3]}] Conexión establecida con el PLC.")
        try:
            # 4. Realiza el Monitoreo:
            Monitoreo(plc)
        # En caso de detectar algún error:
        except Exception as e:
            print(f"[{datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-3]}] Se detecto un error en la operación del Monitoreo.")
            print(f"Detalle del error: {e}")
    else:
        print("Falló la conexión (el PLC rechazó la petición o está apagado).")
except Exception as e:
    print(f"Se detectó un error crítico de red: {e}")
finally:
    # 5. Cierra la conexión al PLC de manera segura:
    if plc.get_connected():
        plc.disconnect()
        print(f"[{datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-3]}] El PLC se ha desconectado de forma segura.")
        # 6. Finaliza el programa hasta que el usuario envíe cualquier tecla. En caso de detectar una interrupción por parte del usuario (Ctrl+C) se interpreta de manera adecuada:
        try:
            inputFinal = input('Fin del programa. Presione Enter para continuar...')
        except KeyboardInterrupt:
            print("Se detectó una interrupción por parte del usuario. Interpretando como petición para salir del programa...")
            time.sleep(3) # Tiempo de espera para que el usuario vea el aviso.