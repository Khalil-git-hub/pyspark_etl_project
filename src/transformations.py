"""
Ce fichier contient toutes les transformations appliquées
sur les DataFrames PySpark.

Chaque fonction doit :
- prendre un DataFrame en entrée
- retourner un DataFrame transformé
""" 

def rename_columns(df):
    """
    Renomme les colonnes pour améliorer la lisibilité.
    """
    return df.withColumnRenamed("old_name", "new_name")