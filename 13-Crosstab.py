import pandas as pd
import numpy as np

df=pd.read_excel("crosstab_survey.xlsx")

print(df)

print("")

df1=pd.crosstab(df["Nationality"],df["Handedness"]) #first value - nationality to be index(first column) and following are the columns

print(df1)

print("")

df2=pd.crosstab(df.Sex,[df.Handedness, df.Nationality], margins=True) # margins will add total frequency

print(df2)

print("")

df3=pd.crosstab([df.Sex, df.Nationality],df.Handedness, margins=True) 

print(df3)

print("")

df4=pd.crosstab(df["Sex"],df["Handedness"], normalize="index") # normalize will add % values

print(df4)

print("")

df5=pd.crosstab(df["Sex"],df["Handedness"], values=df["Age"], aggfunc=np.average)

print(df5)
