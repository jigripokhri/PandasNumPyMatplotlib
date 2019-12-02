import pandas as pd

#df = pd.read_excel("weather_data.xlsx")
#df = pd.read_csv("weather_data.csv")

#print(df)

weather_data = {"Day" : ['1/1/2017','1/2/2017','1/3/2017'],
				"Temperature" : [32,35,38],
				"Event" : ["Rain","Sunny","Snow"]}

df=pd.DataFrame(weather_data)
print(df)