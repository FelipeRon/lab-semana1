import numpy as np
import pandas as pd

from src.lab_semana1.carga import limpiar


def test_carga():
    df = pd.DataFrame(
        {
            "edad": [20, 20, 30, np.nan],
            "ingreso": [1000, 1000, np.inf, 2000],
            "ciudad": [" Quito ", " Quito ", "Guayaquil", "Quito"],
        }
    )

    resultado = limpiar(df)

    # Verificar que se eliminaron los duplicados
    assert len(resultado) == 3

    # Verificar que no quedan nulos en columnas numéricas
    columnas_numericas = resultado.select_dtypes(include="number")

    assert not columnas_numericas.isna().any().any()

    # Verificar que no quedan infinitos
    assert not np.isinf(columnas_numericas).any().any()

    # Verificar que el texto fue limpiado
    assert resultado["ciudad"].tolist() == [
        "quito",
        "guayaquil",
        "quito",
    ]
