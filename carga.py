
import numpy as np
import pandas as pd


def cargar(url,na_values=None):
    """
    Carga un archivo CSV desde una URL y devuelve un DataFrame de pandas.

    Parámetros:
    url (str): La URL del archivo CSV.
    na_values (list, optional): Lista de valores que deben considerarse como NaN.

    Retorna:
    pd.DataFrame: Un DataFrame con los datos cargados.
    """
    df = pd.read_csv(url, na_values=na_values)
    return df

def reporte_nulos(df):
    """
    Genera un reporte de valores nulos en un DataFrame.

    Parámetros:
    df (pd.DataFrame): El DataFrame a analizar.

    Retorna:
    pd.DataFrame: Un DataFrame con una fila por columna, su conteo de
        nulos y su porcentaje de nulos, ordenado de mayor a menor conteo.
    """
    faltantes = df.isnull() | df.eq("?")
    reporte = faltantes.sum().rename("nulos").reset_index()
    reporte = reporte.rename(columns={"index": "columna"})
    reporte["porcentaje"] = reporte["nulos"] / len(df) * 100

    return reporte.sort_values("nulos", ascending=False).reset_index(drop=True)


def limpiar(df):
    """
    Limpia un DataFrame y trata sus valores faltantes por columna.

    Reemplaza infinitos y el símbolo "?" por valores nulos, elimina
    duplicados, normaliza las columnas de texto e imputa las columnas
    numéricas con la mediana y las demás columnas con la moda.

    Parámetros:
    df (pd.DataFrame): El DataFrame a limpiar.

    Retorna:
    pd.DataFrame: El DataFrame limpio con un índice nuevo.
    """
    limpio = df.copy()
    limpio = limpio.replace([np.inf, -np.inf, "?"], np.nan)
    limpio = limpio.drop_duplicates()

    for columna in limpio.columns:
        serie = limpio[columna]
        valores_numericos = pd.to_numeric(serie, errors="coerce")
        es_numerica = (
            valores_numericos.notna().sum() == serie.notna().sum()
            and serie.notna().any()
        )

        if es_numerica:
            limpio[columna] = valores_numericos
        elif pd.api.types.is_object_dtype(serie) or pd.api.types.is_string_dtype(serie):
            limpio[columna] = serie.astype("string").str.strip().str.lower()

    for columna in limpio.columns:
        if not limpio[columna].isna().any():
            continue

        if pd.api.types.is_numeric_dtype(limpio[columna]):
            valor = limpio[columna].median()
            limpio[columna] = limpio[columna].fillna(0 if pd.isna(valor) else valor)
        else:
            moda = limpio[columna].mode(dropna=True)
            valor = moda.iloc[0] if not moda.empty else "desconocido"
            limpio[columna] = limpio[columna].fillna(valor)

    return limpio.reset_index(drop=True)


def guardar(df, ruta):
    """
    Guarda un DataFrame en formato Parquet.

    Parámetros:
    df (pd.DataFrame): El DataFrame que se desea guardar.
    ruta (str): Ruta del archivo Parquet de salida.

    Retorna:
    str: La ruta del archivo guardado.
    """
    df.to_parquet(ruta, index=False)
    return ruta

