import random

def A():
    mylist = []
    r = 1
    x = random.random()
    print(x)
    if  x > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)


for i in range(100):
    A()