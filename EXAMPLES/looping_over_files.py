import sys

for file_path in sys.argv[1:]:  # skip script name (aka sys.argv[0])
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        pass   #  read each file here

#   python myscript.py customer_id firstfile nextfile otherfile 