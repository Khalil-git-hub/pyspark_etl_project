"""
Transformations PySpark ETL
"""

from pyspark.sql.functions import col, avg


def clean_nulls(df):
    return df.dropna()


def rename_columns(df):
    return df.withColumnRenamed("produit", "product")


def average_sales(df):
    df = df.withColumn("sales", col("prix") * col("quantite"))
    return df.groupBy("region").agg(avg("sales").alias("avg_sales"))