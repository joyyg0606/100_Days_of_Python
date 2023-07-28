import pandas, csv

data = pandas.read_csv("CSV Data & Pandas Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cin_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cin_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

with open("CSV Data & Pandas Library/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

with open("CSV Data & Pandas Library/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)

data = pandas.read_csv("CSV Data & Pandas Library/weather_data.csv")
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

print(data['temp'].to_list())
    
print(data['temp'].mean())

print(data['temp'].max())

print(data.condition)

# Get data in row
print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']

monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 1.8 + 32

print(f"{monday_temp_f}°F")

# Create a dataframe from scratch
data_dict = {
    "students": ["a", "b", "c"],
    "scores": [1, 2, 3]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")