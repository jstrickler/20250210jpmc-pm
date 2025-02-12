
colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

for i, color in enumerate(colors):  # enumerate() returns iterable of (index, value) tuples
    print(i, color)
print()
print(f"{list(enumerate(colors)) = }\n")



for num, month in enumerate(months, 1):  # Second parameter to enumerate is added to index
    print(f"{num} {month}")
