import pandas as pd

df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
	})

print(df)

new_df = df.replace(["poor","average","good","exceptional"], [1,2,3,4])
print(new_df)
