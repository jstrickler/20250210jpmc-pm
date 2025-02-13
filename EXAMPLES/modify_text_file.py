import os  # os.path

file_name = 'states.txt'
temp_name = "temp.txt"

with open(file_name) as file_in:
    with open(temp_name, "w") as file_out:
        for line in file_in:  # read states.txt
            new_line = line.upper() 
            file_out.write(new_line)  # write to temp.txt

os.rename(file_name, file_name + '.BAK')  # 'states.txt.BAK'
os.rename(temp_name, file_name)   # 'states.txt
