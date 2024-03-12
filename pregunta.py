"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.dropna(inplace=True)

    # convierto todas las columnas a cadenas para manipular
    df = df.apply(lambda x: x.astype(str))

    # limpio caracteres no deseados
    df = df.apply(lambda x: x.str.replace("$", ""))
    df = df.apply(lambda x: x.str.replace(",", ""))
    df = df.apply(lambda x: x.str.replace("_", "-"))
    df = df.apply(lambda x: x.str.replace("-", " "))
    df = df.apply(lambda x: x.str.lower())

    # convierto el monto del credito a float
    df.monto_del_credito = df.monto_del_credito.astype(float)

    # convierto fecha a formano año-mes-dia
    df.fecha_de_beneficio = pd.to_datetime(
        df["fecha_de_beneficio"], dayfirst=True, format="mixed"
    )

    df.drop_duplicates(inplace=True)

    return df
