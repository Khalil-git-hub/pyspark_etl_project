from pyspark.sql import SparkSession
from transformations import clean_nulls, average_sales, rename_columns

def create_spark_session():
    spark = SparkSession.builder \
        .appName("ETL Pipeline") \
        .getOrCreate()
    return spark


if __name__ == "__main__":
    spark = create_spark_session()

    # 📥 Lecture des données
    df = spark.read.csv("data/ventes.csv", header=True, inferSchema=True)

    # 🔄 Pipeline ETL
    df = clean_nulls(df)
    df = rename_columns(df)
    df = average_sales(df)

    # 📤 Résultat
    df.show()

    print("Pipeline exécuté avec succès 🚀")