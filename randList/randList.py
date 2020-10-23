import random
def randList():
    List = []
    for i in range(10):
        List.append(random.randint(1,50))
    return List

if __name__ == '__main__':
    l = randList()
    print(l)
# print(randList())