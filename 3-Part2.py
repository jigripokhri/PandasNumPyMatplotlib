import pandas as pd

def convert_people_cell(cell):
	if cell=="n.a.":
		return "sam walton"
	return cell

def convert_revenue_cell(cell1):
	if cell1 < 0:
		return None
	return cell1


df=pd.read_excel("stock_data.xlsx", "Sheet1", converters={
	"people" : convert_people_cell,
	"revenue" : convert_revenue_cell
	})
print(df)

df.to_excel("FINAL_stock.xlsx", sheet_name="Stocks", index=False, startrow=1, startcol=2)

with pd.ExcelWriter("stocks_&_weather.xlsx") as writer:
	stock1.to_excel(writer, sheet_name="stocks")
	weather1.to_excel(writer, sheet_name="weather")