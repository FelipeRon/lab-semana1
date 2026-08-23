import matplotlib.pyplot as plt
import pandas as pd

# from src.analisis import (
#    recta_minimos_cuadrados,
#    resumen_por_grupo,
#    top_k,
# )

from src.lab_semana1.carga import cargar, reporte_nulos, limpiar


URL = "https://archive.ics.uci.edu/static/public/183/data.csv"


def main():

    # ---------------------------------
    # 1. Cargar dataset
    # ---------------------------------
    df = cargar(URL, na_values=["?"])

    print("=== REPORTE DE NULOS ===")
    print(reporte_nulos(df).head(20))

    # ---------------------------------
    # 2. Limpiar
    # ---------------------------------
    print("=== DATASET LIMPIO ===")
    df_limpio = limpiar(df)
    print(df_limpio)

    # ---------------------------------
    # 3. Resumen por grupo
    # ---------------------------------
    # Aquí debes escoger una columna categórica
    # disponible después de revisar el dataset.

    # ---------------------------------
    # 4. Top 5
    # ---------------------------------
    # top = top_k(
    #    df_limpio,
    #    "ViolentCrimesPerPop",
    #    5
    # )

    # print("\n=== TOP 5 ===")
    # print(top)

    # ---------------------------------
    # 5. Mínimos cuadrados
    # ---------------------------------
    # Escoger dos variables numéricas
    # después de revisar el dataset.

    # ---------------------------------
    # 6. Gráfico
    # ---------------------------------
    plt.figure()

    plt.hist(df_limpio["ViolentCrimesPerPop"], bins=30)

    plt.xlabel("ViolentCrimesPerPop")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de ViolentCrimesPerPop")

    plt.savefig("figura.png")
    plt.close()


if __name__ == "__main__":
    main()
