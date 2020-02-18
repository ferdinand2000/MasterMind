# Main game waar de pc zoekt naar de code
from Feedback import BlackPointsPc, WhitePointsPc
def choosecode():
    # hier kiest de speler een code die de computer moet raden
    global chosencode
    chosencode = set(list(input("Voer een code van vier letters tussen de A en F in ")))
    a = len(chosencode)
    if a > 4 or a < 4:
        print("De code moet 4 letters lang zijn ")
    return chosencode
choosecode()
def pcGuess():
    # Hier gaat de computer de code proberen te raden
    teller = 0
    global a
    while teller <= 9:
        a = set(list(input("raad de 4 letterige code ")))
        WhitePointsPc(a, chosencode)
        BlackPointsPc(a, chosencode)
        if a == chosencode:
            print("Did andwoordt klopt helemaal")
            break
        else:
            # telt de hoeveelheid pogingen die nog over zijn
            teller += 1
            Pogingen = str(10 - teller)
            print("u heeft nog "+ Pogingen +" pogingen")
    return
pcGuess()
