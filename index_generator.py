#!/bin/python3
import sys

def delete_lines_after_index(output_file_path):
    lines_to_keep = []

    # Leer las líneas del archivo de salida y encontrar la línea "# INDICE"
    with open(output_file_path, 'r') as output_file:
        for line in output_file:
            if line.startswith("# INDICE"):
                lines_to_keep.append(line)
                break  # Detenerse después de encontrar la línea "# INDICE"

            lines_to_keep.append(line)

    # Sobreescribir el archivo de salida con las líneas a mantener
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(lines_to_keep)

def extract_and_append(input_file_path, output_file_path, file_identifier):
    lines_to_append = []

    # Leer las líneas del archivo de entrada y encontrar las que comienzan con "# Texto"
    with open(input_file_path, 'r') as input_file:
        lines_to_append.append(f"\n# {file_identifier}\n\n")  # Agregar el texto asociado al archivo
        for line in input_file:
            if line.startswith("#"):
                lines_to_append.append(line)

    # Añadir las líneas al archivo de salida
    with open(output_file_path, 'a') as output_file:
        output_file.writelines(lines_to_append)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py archivo_salida")
        sys.exit(1)

    output_file_path = sys.argv[1]

    input_file_data = [
        {"path": "ANKI_Personal/tarjetas_anki.txt", "identifier": "General"},
        {"path": "ANKI_Labs/tarjetas_anki.txt", "identifier": "Labs"},
        {"path": "ANKI_Legislacion/tarjetas_anki_legislacion.txt", "identifier": "Legislación"},
        # Agrega aquí más entradas para tus archivos de entrada con sus identificadores
    ]

    delete_lines_after_index(output_file_path)  # Borrar líneas debajo de "# INDICE"

    for entry in input_file_data:
        extract_and_append(entry["path"], output_file_path, entry["identifier"])

    print("Se han extraído y añadido las líneas de los archivos de entrada al archivo de salida.")
