#  print(obj1, obj2, ...) print()
core_value = 38.39023923
person = "Ferd Berfel"
city = "Houston"

print(core_value, person, city)
print(core_value, person, city, sep="#")
print(core_value, person, city, sep=", ")
print(city, end=" ")
print("whatever", end=" ")
print(core_value)

print(core_value, person, city, sep=" ", end="\n")  # redundant!

# city: person
s = f"{city}: {person}"
print(s)
print(f"{city}: {person}")
