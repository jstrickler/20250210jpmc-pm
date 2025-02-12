colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

colors_rev = reversed(colors)

colors[0] = "pink"

colors.append("yellow")
del colors[0]
print(f"{colors_rev = }")
for color in colors_rev:
    print(color)


colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors[3:]:
    print(color)