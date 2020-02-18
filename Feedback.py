# https://docs.python.org/3/tutorial/datastructures.html voor al het gedeelte 5.4. Sets gebruikt
def WhitePointsPc(a, chosencode):
    # Verglijkt de lijsten en kijkt of er 2 elementen op de zelfde plek staan voor MasterMindMainComputer.py
    return
def BlackPointsPc(a, chosencode):
    # Verglijkt de lijsten en kijkt hoeveel unique elementen het zelfde zijn voor MasterMindMainComputer.py
    return
def WhitePointsPlayer(a, RandomCode):
    # Verglijkt de lijsten en kijkt of er 2 elementen op de zelfde plek staan voor MasterMindMain.py
    a_set = set(a)
    RandomCode_set = set(RandomCode)
    b = a_set & RandomCode_set
    print(len(b))
    return
def BlackPointsPlayer(a, RandomCode):
    # Verglijkt de lijsten en kijkt hoeveel unique elementen het zelfde zijn voor MasterMindMain.py
    a_set = set(a)
    RandomCode_set = set(RandomCode)
    b = a_set & RandomCode_set
    print(len(b))
    return