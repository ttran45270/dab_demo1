gold_df = silver_df.groupBy("location").count("*")

display(gold_df)
