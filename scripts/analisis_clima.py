
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
