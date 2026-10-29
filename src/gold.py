
# Databricks notebook source

from pyspark.sql.functions import count, sum, when, col

# Read Silver
silver_df = spark.table("workspace.demo.silver_arrests")

# Aggregate by location
gold_df = silver_df.groupBy("location").agg(
    count("*").alias("total_arrests"),
    sum(when(col("status") == "Released", 1).otherwise(0))
        .alias("released"),
    sum(when(col("status") == "In Custody", 1).otherwise(0))
        .alias("in_custody")
)

# Save Gold
gold_df.write.mode("overwrite").saveAsTable(
    "workspace.demo.gold_arrests"
)

display(gold_df)
