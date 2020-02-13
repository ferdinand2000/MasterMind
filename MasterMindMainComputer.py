def choosecode():
    chosencode = input("voor een code van vier nummers in ")
    return chosencode

def who():
    wich = input("raad de speler of de computer ")
    if wich == ("computer"):
        choosecode()
    else:
        code()
    return
who()