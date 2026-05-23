
# Se importa el módulo csv para poder leer archivos de ese formato
import csv

# Se crean listas vacías donde se van a guardar los datos
periodos = []
temperaturas = []

# Se abre el archivo CSV guardado en la carpeta datos
with open("datos/clima.csv", "r") as archivo:

    # DictReader permite leer cada fila como un diccionario,
    # usando los nombres de las columnas como claves
    lector = csv.DictReader(archivo)

    # Se recorre el archivo fila por fila
    for fila in lector:

        # Solo se usan los registros de la fuente GCAG
        # porque el archivo tiene dos fuentes distintas para los mismos meses
        if fila["Source"] == "GCAG":

            # Se agrega el periodo y la temperatura a sus listas
            periodos.append(fila["Year"])
            temperaturas.append(float(fila["Mean"]))

print("Datos cargados correctamente. Registros encontrados:", len(periodos))

# -----------------------------------------------------------
# FUNCIONES PARA CALCULAR INDICADORES DE TEMPERATURA
# -----------------------------------------------------------

# Esta función recorre la lista y va sumando todos los valores
# para después dividir por la cantidad y obtener el promedio
def calcular_promedio(lista):
    suma = 0
    for valor in lista:
        suma += valor
    promedio = suma / len(lista)
    return promedio

# Esta función recorre la lista comparando cada valor con el mayor
# encontrado hasta ese momento, y devuelve el más grande
def calcular_maximo(lista):
    maximo = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
    return maximo

# Esta función hace lo mismo pero al revés, buscando el menor valor
def calcular_minimo(lista):
    minimo = lista[0]
    for valor in lista:
        if valor < minimo:
            minimo = valor
    return minimo

# Se llama a cada función y se muestran los resultados
promedio = calcular_promedio(temperaturas)
maximo = calcular_maximo(temperaturas)
minimo = calcular_minimo(temperaturas)

print("Temperatura promedio:", round(promedio, 4))
print("Temperatura máxima:", maximo)
print("Temperatura mínima:", minimo)
