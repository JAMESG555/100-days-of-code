import csv

# Challenge 1
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# Challenge 2
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# Challenge 3
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))

# temp = data["temp"].to_list()
# # print(temp)
# avg_temp = sum(temp) / len(temp)
# print(avg_temp)
#
# print(data["temp"].mean())
# # Return Max Value
# print(data["temp"].max())

# #Get Data in Row
# monday = data[data.day == "Monday"]
# # #Get Max Temperature Row
# # print(data[data.temp == data.temp.max()])
# f = (monday.temp * 9/5) + 32
# print(f)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)