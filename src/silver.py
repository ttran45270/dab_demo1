# Databricks notebook source

from pyspark.sql.functions import col, trim, upper, to_date

# Read ALL data from Bronze
bronze_df = spark.table("workspace.demo.bronze_arrests")

# Clean the data
silver_df = (
    bronze_df
    .withColumn("location", upper(trim(col("location"))))
    .withColumn("booking_date", to_date(col("booking_date")))
)

# Save Silver table
silver_df.write.mode("overwrite").saveAsTable(
    "workspace.demo.silver_arrests"
)

display(silver_df)
