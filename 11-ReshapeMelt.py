import pandas as pd

df=pd.read_excel("weather_melt.xlsx")

print(df)

print("")

df1 = pd.melt(df,id_vars=["day"], var_name="city", value_name="temperature") # id_vars - keep that column intact ; var_name will update variable ; value_name will update value

print(df1)

print("")

df2 = df1[df1["city"] == "chicago"] #will filter and print only chicago values

print(df2)