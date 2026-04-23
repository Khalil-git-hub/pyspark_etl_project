"""
Ce fichier contient toutes les transformations appliquées
sur les DataFrames PySpark.
"""

from pyspark.sql.functions import avg

def clean_nulls(df):
    """
    Supprime toutes les lignes contenant des valeurs nulles.
    """
    return df.dropna()


def average_sales(df):
    """
    Calcule la moyenne des ventes par région.
    """
    return df.groupBy("region").agg(avg("sales").alias("avg_sales"))