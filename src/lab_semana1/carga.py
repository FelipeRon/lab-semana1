import numpy as np
import pandas as pd


def cargar(url, na_values=None):
    return pd.read_csv(url, na_values=na_values)


def reporte_nulos(df):
    reporte = pd.DataFrame(
        {
            "nulos": df.isna().sum(),
            "porcentaje": df.isna().mean() * 100,
        }
    )

    return reporte.sort_values("nulos", ascending=False)


def limpiar(df):
    df = df.copy()

    # 1. Infinitos -> NaN
    df = df.replace([np.inf, -np.inf], np.nan)

    # 2. Eliminar duplicados
    df = df.drop_duplicates()

    # 3. Limpiar columnas de texto
    columnas_texto = df.select_dtypes(include="object").columns

    for col in columnas_texto:
        df[col] = df[col].str.strip().str.lower()

    # 4. Tratamiento de faltantes
    for col in df.columns:
        if df[col].isna().sum() == 0:
            continue

        porcentaje = df[col].isna().mean()

        if porcentaje >= 0.80:
            df = df.drop(columns=[col])

        elif pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())

        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    # 5. Reiniciar índice
    df = df.reset_index(drop=True)

    return df


def guardar(df, ruta):

    # Guarda un DataFrame en formato Parquet.

    df.to_parquet(ruta, index=False)
    return ruta


if __name__ == "__main__":
    URL = "https://archive.ics.uci.edu/static/public/183/data.csv"

    df = cargar(URL, na_values=["?"])

    print("Dimensiones originales:")
    print(df.shape)

    print("\nReporte de nulos:")
    print(reporte_nulos(df).head(20))

    limpio = limpiar(df)

    print("\nDimensiones después de limpiar:")
    print(limpio.shape)

    guardar(limpio, "data/limpio.parquet")

    print("\nArchivo guardado en data/limpio.parquet")
