import sys

print(f"sys.argv: {sys.argv}\n")

print("Script name (sys.argv[0])", sys.argv[0])

raw_celsius = sys.argv[1]  # First command line parameter
print(f"raw_celsius: {raw_celsius}")

#  {x}    set with one element
#  [x]   list with one element
#  (x)    just x
#  (x,)   tuple with one element
#   x,    also tuple with one element
#  {x:y}  dict with one element, x is key, y is value

