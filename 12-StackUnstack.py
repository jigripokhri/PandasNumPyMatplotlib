import pandas as pd

df=pd.read_excel("stack_unstack.xlsx", header=[0,1]) # two headers at row 0  and 1 index

print(df)

print("")

df1=df.stack(level=0) # by default stack will transpose inner most level of row as column (level=0 will transpose first row {outer most row})

print(df1)

print("")

df2=df1.unstack()

print(df2)

print("")

############################################

df3=pd.read_excel("stack_unstack1.xlsx", header=[0,1,2]) # three levels of header rows

print(df3)

print("")

df4=df3.stack()

print(df4)