import pandas as pd
import numpy as np

# df = pd.DataFrame({"Nombre": ["Juan", "Sebastián", "Felipe", "David"],
#                    "Edad": [29,32,24,56],
#                    "Ciudad": ["Quito", "Cuenca", "Guayaquil", "Quito"],
#                    "Altura": [1.77, 1.65, 1.70, 1.89]})

def filtrar (df, columna, umbral):
    df2 = df[df[columna]>umbral]
    return df2

def resumen_por_grupo(df, col_grupo, cols_num):
    df2 = df.groupby(col_grupo)[cols_num].agg(['mean', 'std', 'count'])
    return df2

def zscore(matriz):
    media = matriz.mean(axis=0)
    std = matriz.std(axis=0)
    normalizacion = (matriz - media)/std
    return normalizacion

def top_k(df, columna, k):
    array_indexes = np.argsort(df[columna])
    array_indexes = array_indexes[::-1]
    top_k = array_indexes[0:k]
    df2 = df.iloc[top_k]
    return df2

def recta_minimos_cuadrados (x,y):
    matriz_diseño =np.column_stack((x,np.ones(len(x))))
    coeficientes = np.linalg.lstsq(matriz_diseño, y)[0]
    a = coeficientes[0]
    b = coeficientes[1]
    return a, b

# print(filtrar(df, "Edad", 40))
# print(resumen_por_grupo(df, "Ciudad", ["Edad", "Altura"]))
# print(zscore(np.array([[1,5], [10,23]])))
# print(top_k(df,"Edad",2))
# print(recta_minimos_cuadrados(np.arange(0,4), np.array([0,2,4,6])))

