from timeit import Timer

def plan1():
    with open('DATA/words.txt') as words_in:
        for word in words_in:
            x = word

def plan2():
    with open('DATA/words.txt') as words_in:
        all_words = words_in.read().splitlines()
        for word in all_words:
            x = word

setup = 'from __main__ import plan1, plan2'

t1 = Timer('plan1()', setup)
t2 = Timer('plan2()', setup)

print(t1.timeit(1000))
print(t2.timeit(1000))