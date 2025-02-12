cities = list()
cities = []  # preferred
cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")
print(f"{len(cities) = }")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

#  LIST.append(obj)  LIST.insert(idx, obj)  LIST.extend(iterable)
x = 5
print(f"{x = }")
del x

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

#  del LIST[idx]  LIST.remove(value)   LIST.pop(idx) LIST.pop()