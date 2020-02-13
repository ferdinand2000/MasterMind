# Main game loop and visuals
from Compare import compare
import random
def code():
    global RandomCode
    RandomCode = random.randrange(1000, 9999)
    print(RandomCode)
    return RandomCode
code()

def guess(RandomCode):
    global a
    a = int(input("raad de 4 cijferige code "))
    if a == RandomCode:
        print("Did andwoordt klopt helemaal")
    return
guess(RandomCode)

compare(a, RandomCode)
