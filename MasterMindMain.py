# Main game waar de speler zoekt naar de code
import itertools
from random import choice
from Feedback import BlackPointsPlayer
def code():
    # random code word ge genereerdt
    global RandomCode
    RandomCode = [choice("abcdef") for i in range(4)]
    # print(RandomCode)
    return RandomCode
code()
global teller
teller = 0
def guess(RandomCode, teller):
    # hier raad de speler de code
    global a
    while teller <= 9:
        a = list(input("raad de 4 letterige code "))
        BlackPointsPlayer(a, RandomCode)
        if a == RandomCode:
            print("Did andwoord klopt helemaal")
            break
        else:
            # telt de hoeveelheid pogingen die nog over zijn
            teller += 1
            Pogingen = str(10 - teller)
            print("u heeft nog " + Pogingen + " pogingen")
    return
guess(RandomCode, teller)

