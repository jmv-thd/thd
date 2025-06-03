import os
import shutil

def copiar_archivos(origen, destino):

    # Crear la carpeta de destino si no existe
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Recorrer la carpeta de origen y sus subcarpetas
    for carpeta_raiz, _, archivos in os.walk(origen):
        for archivo in archivos:
            ruta_origen = os.path.join(carpeta_raiz, archivo)
            ruta_destino = os.path.join(destino, archivo)

            # Copiar el archivo a la carpeta destino
            shutil.copy2(ruta_origen, ruta_destino)

# Rutas de origen y destino (modifica según necesites)
carpeta_origen = "C:/Users/NombreUsuario/Downloads/cvelistV5-main/cves/2025"
carpeta_destino = "C:/Users/NombreUsuario/Desktop/cves"

copiar_archivos(carpeta_origen, carpeta_destino)

print("Los archivos JSON se copiaron exitosamente.")