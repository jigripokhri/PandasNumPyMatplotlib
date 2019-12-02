import pandas as pd
import numpy as np

df = pd.read_excel("weather_data_cbasics1.xlsx")

print(df)

 # new_df = df.replace([-888,-99999],np.NaN) - will replace -888 & -99999 with NaN (none)

new_df = df.replace({                    #replacing in specific columns
	"temperature" : -99999,
	"windspeed"   : [-99999,-888],
	"event"       : 0
	}, np.NaN)

print(new_df)

new_df1 = df.replace({                   #direct replacing in all columns
	"event" : 0 # np.Nan = 0
	}, "Sunny") 

print(new_df1)

new_df2 = new_df1.replace({
	"temperature" : "[A-Z,a-z]",
	"windspeed"   : "[A-Z,a-z]"
	}, "", regex=True)

print(new_df2)