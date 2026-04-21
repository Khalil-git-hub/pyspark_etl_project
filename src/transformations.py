"""
Ce fichier contient toutes les transformations appliquées
sur les DataFrames PySpark.

Chaque fonction doit :
- prendre un DataFrame en entrée
- retourner un DataFrame transformé
"""

from pyspark.sql.functions import avg

def average_sales(df):
    """
    Calcule la moyenne des ventes par région.

    groupBy :
    regroupe les données par colonne (comme SQL GROUP BY)

    agg :
    applique une fonction d’agrégation
    """
    # Chaque région aura une seule ligne dans le résultat,
    # avec la moyenne des ventes calculée sur toutes ses lignes.
    return df.groupBy("region").agg(avg("sales").alias("avg_sales"))
