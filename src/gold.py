{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "8233924f-deda-499d-bfe6-6de37f29f9f4",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%run ./silver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "007fdbe6-cb26-4b3b-bb9f-e93a737bf2b9",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "#Python\n",
    "\n",
    "# Databricks notebook source\n",
    "\n",
    "from pyspark.sql.functions import count, sum, when, col\n",
    "\n",
    "# Aggregate by location\n",
    "gold_df = silver_df.groupBy(\"location\").agg(\n",
    "    count(\"*\").alias(\"total_arrests\")\n",
    ")\n",
    "\n",
    "# Save Gold\n",
    "#gold_df.write.mode(\"overwrite\").saveAsTable(\"workspace.demo.gold_arrests\")\n",
    "\n",
    "display(gold_df)\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "6"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "gold.py",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
