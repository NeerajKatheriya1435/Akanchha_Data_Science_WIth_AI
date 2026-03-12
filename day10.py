import math
# import math as m
# from math import factorial,sqrt,ceil
# from math import *
# from math import factorial as f

# print(math.sqrt(64))
# print(math.floor(6.4))
# print(math.ceil(6.4))

# print(m.factorial(4))

# print(f(4))
# print(sqrt(4))
# print(ceil(4))

# print(dir(math))
# print(math.sin(math.pi/2))

import os

# print(os.getcwd())
# os.mkdir("Rohan")
# os.makedirs("Geeta/Manish/Divya")

# os.chdir("Geeta/Manish")
# print(os.getcwd())
# print(os.listdir())
# os.rename("Rohan","Ajay")

# os.rmdir("Ajay")

# if os.path.exists("day1.py"):
#     print("File exists")
# else:
#     print("Not found")

# print(os.environ)
# print(os.getenv("Path"))

# Local Variables and global varibales

var1=78

def addTwoNum():
    # var1=34
    global var1
    var1=23
    print(var1)
    print("hello")


addTwoNum()

print(var1)