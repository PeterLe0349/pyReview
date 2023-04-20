import os

def sayHello(phrase):
    print("Hello ", getName(phrase))

def getName(name):
    return "Mr. " + name

# sayHello('Peter')
# print(getName('Petrus'))

def work_on():
    path = os.getcwd()
    print(f'Working on {path}')

# work_on()

def printSetasList():
    aset = {3,4,5, 3, 1}
    # print(type(aset))
    printList(aset)

def printList(alist: list[int]):
    for x in alist:
        print(x)

# printSetasList()

# def read_file(filepath: str):
#     alist = []
#     with open(filepath) as f:
#         alist = [ line.strip() for line in f]
#     return alist

def read_file(filepath: str):
    alist = []
    with open(filepath) as f:
        alist = [ line.strip() for line in f]
    return alist
    
def double_read(file1, file2):
    print('reading: ',read_file(file1))
    print('reading: ',read_file(file2))

# double_read('list.txt', 'list2.txt')

def print_stuff():
    stuff = 'ad'
    return stuff

def side_feed(input: str):
    # print(input)
    return input

def side_print(something):
    print(side_feed(something))
    print(side_feed(something))

# side_print('hi')