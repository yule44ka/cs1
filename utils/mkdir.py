import os
import utils.name as n

def mkdir():
    name = n.get_name()
    os.mkdir(name)