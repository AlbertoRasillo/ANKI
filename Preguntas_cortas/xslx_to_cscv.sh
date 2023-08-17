#!/bin/bash

# Obtener la lista de directorios que comienzan con "preguntas_cortas_"
directorios=$(find . -type d -name "preguntas_cortas_*")

# Iterar sobre cada directorio
for directorio in $directorios; do
    echo "Procesando directorio: $directorio"
    
    # Ejecutar el comando para cada archivo en el directorio actual
    archivos=$(find "$directorio" -type f)
    for archivo in $archivos; do
        echo "Procesando archivo: $archivo"
        soffice --headless --convert-to csv:Text -txt-csv:44,34,76 "$archivo"
    done
    
    echo "Directorio $directorio procesado."
done
