import pandas as pd 

df1 = pd.DataFrame({
	"city" : ["new york", "chicago","orlando"],
	"temperature" : [21,14,35]
	})

print(df1)

print("")

df2 = pd.DataFrame({
	"city" : ["chicago", "new york","orlando"],
	"humidity" : [66,68,75]
	})

print(df2)

print ("")

df3=pd.merge(df1,df2,on="city")

print(df3)


###### JOINS

df4 = pd.DataFrame({
	"city" : ["new york", "chicago","orlando","baltimore"],
	"temperature" : [21,14,35,32]
	})

print(df4)

print("")

df5 = pd.DataFrame({
	"city" : ["chicago", "new york","san francisco"],
	"humidity" : [66,68,71]
	})

print(df5)

print ("")

df61=pd.merge(df4,df5,on="city", how="inner")  # on by default performs INNER join
print(df61)

print("")

df62=pd.merge(df4,df5,on="city", how="outer", indicator=True) # performs OUTER join; indicator tells from which DF the row is from

print(df62)

print("")

df63=pd.merge(df4,df5,on="city", how="left") # performs LEFT join

print(df63)

print("")

df64=pd.merge(df4,df5,on="city", how="right") # performs RIGHT join

print(df64)

print("")


#####################

df100 = pd.DataFrame({
	"city" : ["new york", "chicago","orlando", "baltimore"],
	"temperature" : [21,14,35,38],
	"humidity" : [65,68,71,75]
	})

df101 = pd.DataFrame({
	"city" : [ "chicago","new york","san diego"],
	"temperature" : [21,14,35],
	"humidity" : [65,68,71]
	})

df103=pd.merge(df100,df101,on="city", suffixes=("_left","_right")) # replaces x and y with left and right

print(df103)