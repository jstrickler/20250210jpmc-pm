fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

#    [value for var in iterable if condition]
f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

# fruits = [f.upper() for f in fruits]
f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"{f3 = }\n")

with open('DATA/alice.txt') as alice_in:
#               [VALUE for VARIABLE in ITERABLE if CONDITION]
    lizards = [line.rstrip() for line in alice_in if 'Lizard' in line]
print(f"{lizards = }\n")

nums = [800, 80, 14.3, 1000, 32, -3, 8, 18, 255, 400, 5, 88.9, 5000]

ints = [n for n in nums if isinstance(n, int)]
print(f"{ints = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = set([person[3] for person in people])
print(f"{dobs = }\n")

#  (value for var in iterable)
upper_fruits = [f.upper() for f in fruits]  # list comprehension

ifruits = (f.upper() for f in fruits)  # generator expression
print(f"{ifruits = }\n")

fruits.append('raspberry')
fruits.append('tomato')

del fruits[0]
fruits.remove('orange')

for fruit in ifruits:  # fruit = next(ifruits) -> f.upper()
    print(fruit)

