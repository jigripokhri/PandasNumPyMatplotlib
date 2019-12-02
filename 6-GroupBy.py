import pandas as pd
import matplotlib.pyplot as pt

df = pd.read_excel("weather_by_cities.xlsx")

print(df)

# SPLIT APPLY COMBINE

g=df.groupby("city")

print(g)

for city, city_df in g:	
	print(city)   # city namecl
	print(city_df) # city data frame

print("")

print(g.get_group("mumbai")) # Get title with mumbai as city

print("")

print(g.max())  #prints max temperature by city since g is grouped by city

print("")

print(g.mean()) #prints average

print("")

print(g.describe())

print("")

pt.plot(g.mean())
pt.show()