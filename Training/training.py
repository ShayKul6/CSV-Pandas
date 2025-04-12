# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# --- Option 1 --- #
# temperature_dict = data["temp"].to_dict()
# num_of_temp = len(temperature_dict)
# total = 0
# for temp in temperature_dict.values():
#     total += temp
# avg = (total / num_of_temp)
# print(avg)

# --- Option 2 --- #
# temperature_list = data["temp"].to_list()
# avg = data["temp"].mean()
# print(avg)

# max_temp = data["temp"].max()  # Get maximum temperature
# raw_highest_temp = (data[data.temp == max_temp])  # Row with of the highest temperature

# monday_temp_fahr = ((data[data.day == "Monday"]).temp[0] * 9/5) + 32
# print(monday_temp_fahr)


# --- Create DataFrame from scratch --- #
# data_dict = {
#     "students": ["Shay", "Chen", "Tommy"],
#     "Scores": [69, 76, 81]
# }
# df = pandas.DataFrame(data_dict)
# print(df)
# data.to_csv("new_data.csv")


# --- The Great Squirrel Census --- #
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color = data["Primary Fur Color"]  # the line of fur color
count_gray = 0
count_black = 0
count_cinnamon = 0

for color in primary_fur_color:
    if color == "Gray":
        count_gray += 1
    if color == "Black":
        count_black += 1
    if color == "Cinnamon":
        count_cinnamon += 1

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")