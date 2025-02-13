import sys
import geometry  # find and execute geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# 1. current folder
# 2. folders in PYTHONPATH
# 3. predefined folders in sys.prefix
print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)

