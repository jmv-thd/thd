import pandas as pd
import json
import os

# Definir la carpeta donde están los archivos JSON
carpeta_json = "C:/Users/NombreUsuario/Desktop/cves"

# Lista para almacenar los datos de cada archivo JSON
datos = []

# Recorrer todos los archivos JSON en la carpeta
for archivo in os.listdir(carpeta_json):
    if archivo.endswith(".json"):  # Filtrar solo archivos JSON
        ruta_archivo = os.path.join(carpeta_json, archivo)
        
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extraer los valores requeridos con manejo de errores
        cve_id = data["cveMetadata"]["cveId"]

        # Validar si "descriptions" existe en el JSON
        description_value = "No disponible"  # Valor por defecto
        if "descriptions" in data["containers"]["cna"]:
            try:
                description_value = data["containers"]["cna"]["descriptions"][0]["value"]
            except (KeyError, IndexError):
                description_value = "No disponible"

        # Manejar el caso en que "metrics" no existe
        base_score = None  # Valor por defecto
        if "metrics" in data["containers"]["cna"]:
            try:
                base_score = data["containers"]["cna"]["metrics"][0]["cvssV3_1"]["baseScore"]
            except (KeyError, IndexError):
                base_score = "No disponible"

        # Agregar los datos a la lista
        datos.append({
            "Name": cve_id,
            "Description": description_value,
            "Score": base_score
        })

# Convertir la lista en un DataFrame
df = pd.DataFrame(datos)

# Guardar todos los datos en un solo archivo CSV
df.to_csv("C:/Users/NombreUsuario/Desktop/cve.csv", index=False, encoding="utf-8")

print("Archivo CSV generado con todos los JSON exitosamente.")