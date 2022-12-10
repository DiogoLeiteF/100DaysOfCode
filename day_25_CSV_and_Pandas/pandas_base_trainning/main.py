# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     new = [i.replace('\n', '').split(",") for i in data]
#     print(new)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
# print(temp_list)
#
# # series mean
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
#
# print(data["temp"].mean())
#
# # max value os the serie
# print(data['temp'].max())
#
# # get Data in Colimns
# print(data["condition"])
# print(data.condition)
#
# # Get data in ROWS
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"monday temp in F: {monday_temp_F}")
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_csv_file.csv")
# print(data)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

blacks_count = len(data[data["Primary Fur Color"] == "Black"])

greys_count = len(data[data["Primary Fur Color"] == "Gray"])

cinnamons_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


new_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [greys_count, cinnamons_count, blacks_count]
}

print(new_dict)

df = pandas.DataFrame(new_dict)
df.to_csv("colors.csv")
