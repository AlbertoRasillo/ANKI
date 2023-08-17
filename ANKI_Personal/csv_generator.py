#!/bin/python3
import os
import shutil
from datetime import datetime
import argparse

def clean_lines(lines):
    # Eliminar líneas en blanco y espacios en blanco al principio y al final
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines

def create_backup(source_file, backup_folder):
    # Obtener la fecha actual
    current_date = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Nombre del archivo de backup con la fecha actual
    backup_filename = f"{os.path.splitext(os.path.basename(source_file))[0]}_{current_date}.txt"

    # Ruta completa del archivo de backup
    backup_path = os.path.join(backup_folder, backup_filename)

    # Copiar el archivo de origen al archivo de backup
    shutil.copy(source_file, backup_path)

def clean_output_folder(output_folder):
    # Eliminar todos los archivos CSV en la carpeta de salida
    for filename in os.listdir(output_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(output_folder, filename)
            os.remove(file_path)

def main(source_file):
    # Rutas de archivos y carpetas
    backup_folder = "backups"
    csv_output_folder = "ANKI_output"

    # Crear una carpeta de backups si no existe
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Crear un backup del archivo de origen
    create_backup(source_file, backup_folder)

    # Limpiar la carpeta de salida antes de generar nuevos archivos
    clean_output_folder(csv_output_folder) 

    with open(source_file, "r") as file:
        lines = file.readlines()

    # Limpia las líneas del archivo
    cleaned_lines = clean_lines(lines)

    # Variables auxiliares para almacenar el contenido de los CSV
    current_header = None
    current_content = []

    for line in cleaned_lines:
        if line.startswith("#"):
            # Si encontramos un encabezado, terminamos el archivo anterior y comenzamos uno nuevo
            if current_header:
                filename = current_header.strip("#").strip().replace(" ", "_") + ".csv"
                csv_output_path = os.path.join(csv_output_folder, filename)
                with open(csv_output_path, "w") as csv_file:
                    csv_file.write("\n".join(current_content))
            current_header = line
            current_content = []
        else:
            # Agregamos las líneas al contenido actual
            current_content.append(line)

    # Finalmente, escribimos el último archivo CSV
    if current_header:
        filename = current_header.strip("#").strip().replace(" ", "_") + ".csv"
        csv_output_path = os.path.join(csv_output_folder, filename)
        with open(csv_output_path, "w") as csv_file:
            csv_file.write("\n".join(current_content))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera múltiples archivos CSV a partir de un archivo de entrada.")
    parser.add_argument("source_file", help="Nombre del archivo de entrada")
    args = parser.parse_args()
    main(args.source_file)
