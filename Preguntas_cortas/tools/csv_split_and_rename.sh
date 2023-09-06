#!/bin/bash
# parametros $1 numero filas csv, $2 nombre fichero entrante

# dividir fichero en multiples ficheros csv
split -l $1 $2 preguntas_cortas_

# renombrar con contador el nombre fichero csv
count=1
for file in preguntas_cortas_*; do
  mv "$file" "$(printf 'preguntas_cortas_%03d.csv' "$count")"
  count=$((count+1))
done
