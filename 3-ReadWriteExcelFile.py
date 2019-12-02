import pandas as pd
#df = pd.read_excel("stock_data.xlsx", header=1) # header=1 or skiprows=1 basically skips first row
#df = pd.read_excel("stock_data.xlsx", header=None, names=["tickers","eps","revenue","price","people"]) # header will insert top row with index values as names and names will rename those index values

#df=pd.read_excel("stock_data.xlsx", nrows=3) #will print top three rows

#df=pd.read_excel("stock_data.xlsx", na_values=["not available","n.a."]) #replace not available and n.a. with NAN - useful to clean up dataset

df=pd.read_excel("stock_data.xlsx", na_values={ "eps" : ["not available", "n.a."],
												"revenue" : ["not available","n.a.",-1.00],
												"people" : ["not available","n.a."],
												"price" : ["not available","n.a."]
											  }) #getting all mentioned values to NaN

print(df)

#df.to_excel("new_stock_data.xlsx", index=False) # creates another excel file with that name with contents of df

print(df.columns)

df.to_excel("second_new_stock_data.xlsx", columns=["tickers","eps"], index=False) # if we add header=False it will skip first row