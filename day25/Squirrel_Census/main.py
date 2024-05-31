import pandas
import csv

# Count of "Primary Fur Color"
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
s_count = data.groupby("Primary Fur Color").size()
s_count = s_count.reset_index()
s_count = s_count.set_axis([ 'Fur Color', 'Count'], axis=1)
s_count = s_count.sort_values(by='Count', ascending=False)
print(s_count)
s_count.to_csv("squirrel_count.csv")