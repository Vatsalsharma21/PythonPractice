travel_log = [{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Little", "Dijon"]
}, {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hanburg", "Stuttgart"]
}]


def add_new_country(country, visits, list_cities):
    temp_dict = {}
    temp_dict["country"] = country
    temp_dict["visits"] = visits
    temp_dict["cities"] = list_cities

    travel_log.append(temp_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Peterborough"])
print(travel_log)
