fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
# idx = len(fruits) - 1
print(f"{fruits[-1] = }")
print(f"{fruits[-5] = }")

#  [start-at:stop-before] [start-at:stop-before:increment-by]
print(f"{fruits[0:5] = }")
print(f"{fruits[:5] = }")
start = 8
print(f"{fruits[start:start + 4] = }")

food = "veal piccata"
print(f"{food[5:8] = }")
print(f"{food[-4:] = }")
print(f"{food[3:6] = }")

# for var ... in iterable:
#    ...
for fruit in fruits:
    print(fruit, fruit.upper(), fruit.title())

game = "football"
print(game)
print(repr(game))

print(fruits)
print(fruits[0])   # str(...)
print(f"{fruits[0] = }")   # repr(...)


