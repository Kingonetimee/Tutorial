travel_log = [
{
    "country": "France",
    "visits": 2,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
]


def add_new_country(country, visits, cities=[]):
    travel_log.append(
          {
         "country": country,
         "visits": visits,
         "cities": cities,
        }
    )
       
country = input("Country: ")
visits = input("how many times have you visited?: ")
cities = [input("Name the cities you have been to seperate with a comma: ")]

add_new_country(country, visits, cities)
print(travel_log)