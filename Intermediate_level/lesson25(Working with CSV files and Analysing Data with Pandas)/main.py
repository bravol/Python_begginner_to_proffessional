import csv

# csv in full comma separated values.
# with open('weather_data.csv') as data_file:
#     data =csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
# print(type(data['temp']))

data_dict=data.to_dict()
# print(data_dict)
temp_list= data['temp'].to_list()
print(temp_list)
print(data['temp'].mean())
print(data['temp'].max())

# get the dataframes
print(data['condition'])
# print(data.condition)

# get data in a row
day1= data[data.day=='Monday']
# print(day1)
max1= data[data.temp==data.temp.max()]
# print(max1)

monday=data[data.day =='Monday']
print(monday.condition)


# CREATE DATA FRAME FROM SCRATCH
data1_dict ={
    "students":['Any','James','Angela'],
    "scores":[76,65,89]
}

data = pandas.DataFrame(data1_dict)
data.to_csv('new_data.csv')