value = 56

if value > 75:
    print("koala")
    print("kookaburra")
elif value > 50:  # else if
    print("platypus")
    print("kangaroo")
    if value > 60:
        print("quokka")
else:
    print("wombat")
    print("wallaby")

print("ALL DONE")

if value:   # DON'T DO THIS: if bool(value) == True:
    print("wahooooo")

s = ""
if not s:
    print("Python is the best!")

# C family (curly brace heaven) A ? B : C    
# C C++ C# Java PHP Perl kotlin scala javascript awk objective-C

# Python family B if A else C

debug = False

color = "red" if debug else "green"

print(f"{color = }")
# print(f"abc = {color}")

# logging.error("abc = %s", color)

print(f"{color = }")
print(f"{color = }")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

#  == != > < >= <=

# = assignment
# == comparison

x = 4
# x == 4  # don't do this....
if x == 4:
    print("all is well")


a = 'otter'
b = 'wolverine'

if a.startswith('o') and b.startswith('w'):
    print("yayyyyy")

if a.startswith('m') and b.startswith('w'):
    print("booo")

#  java &&
#  python and or not in del 

if a.startswith('o') or b.startswith('w'):
    print("yayyyyy again")
