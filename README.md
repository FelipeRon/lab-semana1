# Lab Semana 1 - <Communities and Crime>
 - Persona A: <Felipe Ron>- Persona B: <Juan Sebastian Villarreal>- Dataset: <archive.ics.uci.edu/static/public/183
/data.csv>- Tarea: <regresion>   Variable objetivo: <columna>
 
## Como correr
 
    uv sync
    uv run pytest -q
    uv run python main.py
 
## Hallazgos

(B) - Primero, que hubo una remoción de más de 20 columnas que tenían más del 80% de datos faltantes, una lástima porque algunas de esas columnas eran datos sobre a policía como el número de policías por población, el número de tipos de drogas en la comunidad, etc.

- Dentro de uno de los pocos análisis que se hizo, se pudo ver que lamentablemente el número de inmigrantes parece estar correlacionado con el número de crímenes violentos.

- También, la cantidad de empleo tiene una relación inversamente proporcional al número de crímenes violentos.

- Al analizar la frecuencia de crímenes violentos por poblador, se puede ver que en general la frecuencia común es menor al 20%. Sin embargo, esto es preocupante ya que respecto a crímenes violentos, es un indicador que está muy alto.
 
## Decisiones de limpieza