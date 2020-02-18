# https://docs.python.org/3/tutorial/datastructures.html voor al het gedeelte 5.4. Sets gebruikt
def WhitePointsPc(a, chosencode):

    return
def BlackPointsPc(a, chosencode):

    return
def BlackPointsPlayer(a, RandomCode):
    a_set = set(a)
    RandomCode_set = set(RandomCode)
    b = a_set & RandomCode_set
    print(len(b))
    return