"""
Ce fichier contient toutes les transformations appliquées
sur les DataFrames PySpark.

Chaque fonction doit :
- prendre un DataFrame en entrée
- retourner un DataFrame transformé
"""

def clean_nulls(df):
    """
    Supprime toutes les lignes contenant des valeurs nulles.

    Explication :
    Spark stocke les données sous forme de DataFrame distribué.
    dropna() supprime les lignes où au moins une colonne est NULL.
    """
    return df.dropna()