import os

def dir():
    cur = os.getcwd()
    parent = os.path.dirname(cur)
    res = os.listdir(parent)
    for el in res:
        print(el)