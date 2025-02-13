d1 = {
    'spam': 'mail',
    'eggs': 'poached',
    'toast': 'rye',
}

d2 = {
    'ham': 'deli',
    'eggs': 'scrambled',
    'toast': 'wheat',
}

print(f"{d1 = }\n")
print(f"{d2 = }\n")

d3 = d1 | d2  
# same as 
# d3 = dict(d1)
# d3.merge(d2)

print(f"{d3 = } (d1 | d2)\n")

d1 |= d2  
# same as d1.merge(d2)

print(f"{d1 = }\n")

