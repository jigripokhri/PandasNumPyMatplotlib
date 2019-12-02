import pandas as pd

india_weather = pd.DataFrame ({
	"city" : ["mumbai","delhi","banglore"],
	"temperature" : [32,45,30],
	"humidity": [80,60,70]
	})

print(india_weather)

us_weather = pd.DataFrame ({                       #creating dataframe
	"city" : ["new york","chicago","orlando"],
	"temperature" : [21,14,35],
	"humidity": [68,65,75]
	})

print(us_weather)

print("")

df = pd.concat([india_weather,us_weather], keys=["india","us"]) # ignore_index=True to get single index for concaneted df

print(df)

print("")

print(df.loc["india"]) #returning indian values from concaneted df

print("")

print(df.loc["us"]) #returning us values from concaneted df

#####

print("")

temperature_df = pd.DataFrame({
	"city" : ["mumbai","delhi","banglore"],
	"temperature" : [32,45,30]
	})

windspeed_df = pd.DataFrame({
	"city" : ["delhi","mumbai"],
	"windspeed" : [7,12]
	}, index=[1,0]) #match index with previous dataframe

df1 = pd.concat([temperature_df,windspeed_df], axis=1) #will append windspeed as additional column

print(df1)

####

print(temperature_df)

s = pd.Series(["Humid","Dry","Rain"], name="event")

df3 = pd.concat([temperature_df, s], axis=1)

print(df3)