import pandas as pd

df = pd.read_excel("weather_data.xlsx")
print("Extracted Table:")
print(df)

print("")

print(f"Shape of Table is {df.shape}")
rows, columns = df.shape
print(f"Table has {rows} rows")
print(f"Table has {columns} columns")

print("")

print(df.head(3)) #top three rows
print(df.tail(3)) #bottom three rows

print("")

print(df[2:5]) #print rows 2-4

print("")

print(df.columns) #print all columns

print("")

print(df.Day) #prints Day column print(df["Day"])

print("")

print(df["Event"]) #prints Event Column PLEASE USE THIS 

print("")

print(type(df["Event"])) #Type is series

print("")

print( df[["Day","Event","Temperature"]] ) #print any 3 columns in particular

print("")

print(f"Maximum Temperature is {df['Temperature'].max()}")
print(f"Maximum Temperature is {df['Temperature'].min()}")
print(f"Average Temperature is {df['Temperature'].mean()}")

print("")

print(df.describe()) #Table description

print("")

print(df[ df["Temperature"] >=32 ]) # ALTERNATIVE print(df[df.Temperature >=32])

print("")

print( df[ df["Temperature"] == df.Temperature.max() ]) # print record with max temp
print( df["Day"][df.Temperature == df.Temperature.max()] )
print( df[["Day","Temperature"]][df.Temperature == df.Temperature.max()] )

print("")

print(df.index)

print("")

df.set_index("Day", inplace=True) # Making Day as index column (done to use LOC command)
print(df) # Day indexed table

print( df.LOC["2017-01-03"] ) #Not working (?)