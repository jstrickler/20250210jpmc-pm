
#  myfunction(arg1, arg2)

#               positional    named
def word_search(word, *files, ignore_case, output_file="pdf"):
    print(f"{word = }")
    print(f"{files = }")
    # for file in files:
    #   open file ...
    

word_search('spaghetti', 'food1.txt', 'food2.txt', output_file="txt")
word_search('wombat', 'file1.txt', 'file2.txt', ignore_case=True)

def spam(*args):
    pass

def toast(*, first_name, last_name):
    pass

toast(first_name="John", last_name="Smith")
toast(last_name="Smith", first_name="John")


def greet(whom="world"):
    print(f"Hello, {whom}")

greet("Mom")
greet()