# tests/test_analisis.py
import numpy as np
import pandas as pd
import pytest
from lab_semana1.analisis import filtrar, zscore, resumen_por_grupo

# Matematica Aplicada a ML con Programacion - USFQ - Laboratorio Semana 1 5

@pytest.fixture # <- se define una sola vez
def df_mini():
    return pd.DataFrame({
    "grupo": ["a", "a", "b", "b"],
    "valor": [10.0, 20.0, 30.0, 40.0],
    })

def test_filtrar(df_mini):
    resultado = filtrar(df_mini, "valor", 21)
    assert len(resultado) == 2

def test_zscore_tiene_media_cero(df_mini): # <- pytest inyecta df_mini
    z = zscore(df_mini[["valor"]].to_numpy())
    assert z.mean() == pytest.approx(0.0, abs=1e-9)

def test_resumen_por_grupo_calcula_la_media(df_mini):
    r = resumen_por_grupo(df_mini, "grupo", ["valor"])
    assert r.loc["a", ("valor", "mean")] == pytest.approx(15.0)