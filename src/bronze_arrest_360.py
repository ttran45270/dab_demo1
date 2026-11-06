
spark.sql("USE CATALOG uip_eid_uc")



# breakpoint()
#just some note

x=10
y=20

# breakpoint()


result=x+y
print(result)


# breakpoint()


result=x-y
print(result)

df=spark.read.table("ice_ero_eofy_historical_data.ero_cdi_eofy25")

#14 ero_cdi_eofy25
df1 = df.select(
    [c for c in df.columns if "criminality" in c.lower()]
).distinct()

display(df1)

df1.show()