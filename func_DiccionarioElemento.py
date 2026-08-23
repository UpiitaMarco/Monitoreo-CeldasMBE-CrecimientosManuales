# Función que devuelve los datos correspondientes tipo 'Dictionary' del elemento a operar.

# Declarando los datos tipo 'Dictionary' para todos los elementos.
# Valores obtenidos de la DB1 del PLC así como de las constantes de cada elemento definidas en su 'Block Interface' correspondiente.
dictAl = {
    'NombreElemento': 'Aluminio',
    'AbreviaturaElemento': 'Al',
    'tApertura': 0.475,
    'tCierre': 0.475,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 0,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 0,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 0,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 0,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 0,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 0
}

dictGa = {
    'NombreElemento': 'Galio',
    'AbreviaturaElemento': 'Ga',
    'tApertura': 0.775,
    'tCierre': 0.775,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 1,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 1,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 1,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 1,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 1,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 1
}

dictN = {
    'NombreElemento': 'Nitrógeno',
    'AbreviaturaElemento': 'N',
    'tApertura': 0.575,
    'tCierre': 0.575,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 2,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 2,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 2,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 2,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 2,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 2
}

dictIn = {
    'NombreElemento': 'Indio',
    'AbreviaturaElemento': 'In',
    'tApertura': 0.730,
    'tCierre': 0.730,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 3,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 3,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 3,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 3,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 3,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 3
}

dictAs = {
    'NombreElemento': 'Arsénico',
    'AbreviaturaElemento': 'As',
    'tApertura': 0.800,
    'tCierre': 0.800,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 4,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 4,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 4,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 4,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 4,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 4
}

dictBe = {
    'NombreElemento': 'Berilio',
    'AbreviaturaElemento': 'Be',
    'tApertura': 0.560,
    'tCierre': 0.560,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 5,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 5,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 5,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 5,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 5,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 5
}

dictMn = {
    'NombreElemento': 'Manganeso',
    'AbreviaturaElemento': 'Mn',
    'tApertura': 0.500,
    'tCierre': 0.500,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 6,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 6,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 6,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 6,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 6,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 6
}

dictSi = {
    'NombreElemento': 'Silicio',
    'AbreviaturaElemento': 'Si',
    'tApertura': 1,
    'tCierre': 1,
    'Byte_AperturaPuntual': 20,
    'Bit_AperturaPuntual': 7,
    'Byte_CierrePuntual': 24,
    'Bit_CierrePuntual': 7,
    'Byte_EstSensorAbierto': 454,
    'Bit_EstSensorAbierto': 7,
    'Byte_EstSensorCerrado': 456,
    'Bit_EstSensorCerrado': 7,
    'Byte_EstAbriendo': 232,
    'Bit_EstAbriendo': 7,
    'Byte_EstCerrando': 234,
    'Bit_EstCerrando': 7
}

dictMg = {
    'NombreElemento': 'Magnesio',
    'AbreviaturaElemento': 'Mg',
    'tApertura': 1,
    'tCierre': 1,
    'Byte_AperturaPuntual': 21,
    'Bit_AperturaPuntual': 0,
    'Byte_CierrePuntual': 25,
    'Bit_CierrePuntual': 0,
    'Byte_EstSensorAbierto': 455,
    'Bit_EstSensorAbierto': 0,
    'Byte_EstSensorCerrado': 457,
    'Bit_EstSensorCerrado': 0,
    'Byte_EstAbriendo': 233,
    'Bit_EstAbriendo': 0,
    'Byte_EstCerrando': 235,
    'Bit_EstCerrando': 0
}

# Definiendo la función:
def DiccionarioElemento(elemento):
    # De acuerdo con el elemento dado, devuelve el diccionario de datos correspondiente:
    match elemento:
        case 'Al':
            return dictAl
        case 'Ga':
            return dictGa
        case 'N':
            return dictN
        case 'In':
            return dictIn
        case 'As':
            return dictAs
        case 'Be':
            return dictBe
        case 'Mn':
            return dictMn
        case 'Si':
            return dictSi
        case 'Mg':
            return dictMg
        case 'Todos':
            return [dictAl, dictGa, dictN, dictIn, dictAs, dictBe, dictMn, dictSi, dictMg]