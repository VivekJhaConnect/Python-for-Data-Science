from pyspark.sql import SparkSession


spark = SparkSession.builder.master('local').appName('MySpace').getOrCreate()

print(spark.version) 