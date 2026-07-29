# import csv

# with open("weather_data.csv") as data:
#     content = csv.reader(data)
#     temperature = []

#     for row in content:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
        
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]
m_temp = (monday.temp * 1.8) + 32
print(m_temp)