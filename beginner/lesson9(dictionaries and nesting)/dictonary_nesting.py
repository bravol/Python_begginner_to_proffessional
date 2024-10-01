capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
# nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Stuttgart"]
}

# print Lille
print(travel_log["France"][1])

# print D
nested_list = ["A", "B", ["C", "D"], "E"]
print(nested_list[2][1])

tra_log = {
    "France":{
        "num_times_visited": 6,
        "cities_visited": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart"],
        "total_visits": 5
    }
}
print(tra_log['Germany']["cities_visited"][1])