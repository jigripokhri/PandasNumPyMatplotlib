import pandas as pd

df=pd.read_excel("weather_pivot.xlsx")

print(df)

print("")

### PIVOT

df1=df.pivot(index="date",columns="city", values="temperature") #values will only display that column

print(df1)

print("")

### PIVOT TABLE

df2 = pd.read_excel("weather_pivot_table.xlsx")

print(df2)

print("")

df3 = df2.pivot_table(index="city",columns="date", margins=True) # if you add aggfunc="count" will count values

print(df3)

print("")

df4=pd.read_excel("weather_pivot_table2.xlsx")

df4["date"] = pd.to_datetime(df4["date"]) #converting date to timestamp

print(df4)

df5 = df4.pivot_table(index=pd.Grouper(freq="M", key="date"), columns="city") #average temperature and humidity based on M - month

print("")

print(df5)