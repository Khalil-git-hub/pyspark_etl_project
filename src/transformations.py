"""
Ce fichier contient toutes les transformations appliquées
sur les DataFrames PySpark.
"""

from pyspark.sql.functions import avg


def rename_columns(df):
    """
    Renomme les colonnes pour améliorer la lisibilité.
    """
    return df.withColumnRenamed("old_name", "new_name")


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