# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///


# COMMAND ----------



# COMMAND ----------

data = [
    (1001, "Washington DC", "2026-10-01", "Released"),
    (1002, "Baltimore", "2026-10-02", "In Custody"),
    (1003, "Arlington", "2026-10-03", "Released"),
    (1004, "Baltimore", "2026-10-04", "In Custody"),
    (1005, "Alexandria", "2026-10-05", "Released") ]

columns = [
    "arrest_id",
    "location",
    "booking_date",
    "status"
]

bronze_df = spark.createDataFrame(data, columns)

display(bronze_df)
