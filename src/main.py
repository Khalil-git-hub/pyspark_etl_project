from pyspark.sql import SparkSession

def create_spark_session():
    """
    Initialise une SparkSession.
    C’est le point d’entrée de toute application PySpark.
    """
    spark = SparkSession.builder \
        .appName("ETL Pipeline") \
        .getOrCreate()
    
    return spark


if __name__ == "__main__":
    spark = create_spark_session()
    print("Spark Session créée avec succès")