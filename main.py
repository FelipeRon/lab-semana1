import pandas as pd
from pathlib import Path

from carga import cargar, guardar, limpiar, reporte_nulos

url = "https://archive.ics.uci.edu/static/public/183/data.csv"


if __name__ == "__main__":
	df = cargar(url)

	print(df.head())
	print(reporte_nulos(df))

	df_limpio = limpiar(df)
	print(df_limpio.head())

	ruta_salida = Path("data") / "limpio.parquet"
	ruta_salida.parent.mkdir(parents=True, exist_ok=True)
	guardar(df_limpio, ruta_salida)
