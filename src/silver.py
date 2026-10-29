# Databricks notebook source
# MAGIC %run ./bronze

# COMMAND ----------

from pyspark.sql.functions import col, trim, upper, to_date

silver_df = (
    bronze_df
    .withColumn("location", upper(trim(col("location"))))
    .withColumn("booking_date", to_date(col("booking_date")))
)

display(silver_df)
