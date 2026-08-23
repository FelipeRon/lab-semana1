# Lab Semana 1 - <Communities and Crime>
 - Persona A: <Felipe Ron>- Persona B: <Juan Sebastian Villarreal>- Dataset: <archive.ics.uci.edu/static/public/183
/data.csv>- Tarea: <regresion>   Variable objetivo: <ViolentCrimesPerPop>
 
## Como correr
 
    uv sync
    uv run pytest -q
    uv run python main.py

#PERSONA A 
## Hallazgos
 -(A) Se encontro que en los datos hay columnas con datos nulos(?) de alrededor de 84%
 -(A) No eran ni na, ni -200, sino un string de "?"
 -(A) Se sigue el criterio de que si una columna tiene +80% de faltantes se limina y si tenemos menor al 80% se completa con la media de los valores de la columna y por el caso que sea un texto se ingresara en el na un texto del que mas se repita 
 -(A) Se analisa los datos y se observa que la varianle de interes ViolentCrimesPerPop no tiene nulos por lo que se pueden eliminar columnas de datos faltantes que no son nuestro objetivo, cumpliendo lo anteiror.

## Decisiones de limpieza

 -(A) Se sigue el criterio de que si una columna tiene +80% de faltantes se limina y si tenemos menor al 80% se completa con la media de los valores de la columna y por el caso que sea un texto se ingresara en el na un texto del que mas se repita 
 -(A) Se analisa los datos y se observa que la varianle de interes ViolentCrimesPerPop no tiene nulos por lo que se pueden eliminar columnas de datos faltantes que no son nuestro objetivo, cumpliendo lo anteiror.