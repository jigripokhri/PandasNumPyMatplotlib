import pandas as pd

df=pd.read_excel("weather_data_cbasics.xls", parse_dates=["day"])
print(type(df.day[0]))
print(df)

df.set_index("day", inplace=True) # day is new index
print(df)

#new_df = df.fillna(0) #replaces NaN with 0 or whatever you put in place of 0
#print(new_df) # new_df - new dataframe with 0 instead of NaN

new_df = df.fillna({
	"temperature": 0,
	"windspeed" : 0,
	"event" : "no event"
	})
print (new_df)

new_df = df.fillna(method="ffill", limit=1) #"bfill" for backward value # axis instead of method for making column changes # limit - limiting action to one column or row 
print(new_df)


print(df)
new_df2 = df.interpolate(method="time") #getting averate values wrt time
print(new_df2)

new_df3 = df.dropna(how="all") #drops rows with atleast one blank or NaN & adding how="all" will get rid of colums with all blank values
print(new_df3)     #(thresh=1) - to keep values with 1 value

print(df)

dt=pd.date_range("01-01-2017","01-11-2017") #adding all dates for df
idx=pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)