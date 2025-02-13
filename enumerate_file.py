# import os
# import glob

with open('DATA/words.txt') as words_in:
    for i, raw_line in enumerate(words_in):
        line = raw_line.rstrip()
        print(line)
        if i == 100:
            break