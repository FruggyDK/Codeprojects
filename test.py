'''todo:
    fix problemet med while-loop, og implementer funktionen til, hvis man får
    over 30, så skal man blive ved med at slå, hvis man får det tal som man har
    over 30 (31 - 30 = 1, så 1'er) 6 slag max (men der behøves der ikke user, der 
    skal bare slå's og så tager programmet selv fra, men printer i konsolen, hvor mange man får // add dem 
    til en liste (TempMinusPoint = [1,1,1,1], så kan man enten bruge antalØjne, eller 
    sige len(TempMinusPoints) * 1, så i vores tilfælde 4 * 1 = 4 point fra modstanderen')
'''

import random

rslag = []
gslag = []


def generateSlag(arg1):
    i = 1
    while i <= arg1:
        rslag.append(random.randint(1, 6))
        i += 1
    else:
        return rslag
        print(rslag)


def antalØjne(list):
    a = 0
    for number in gslag:
        a += number
    else:
        return a


h = 6
# fix - med det menes der; når der er en terning tilbage vælges den automatisk, og hvis der
while len(gslag) < 6:
    i = 0
    rslag = generateSlag(h)
    rslag.sort()
    print(rslag)

    while i <= len(rslag) - 1:
        print("Vil du gemme", rslag[i], '?')
        tempv = input("> ")

        if tempv.lower() == 'ja':
            gslag.append(rslag[i])
            h -= 1
        elif tempv.lower() == 'nej':
            pass
        else:
            print("forket input, brug 'ja' og 'nej' ")
            i -= 1
        i += 1
    else:
        print("deres terninger", gslag, "=", antalØjne(gslag))
        rslag.clear()

if antalØjne(gslag) > 30:
    TempMinusPoint = (antalØjne(gslag) - 30)
    print("du skal slå efter", TempMinusPoint)
    TempMinusPoints = int(input("Hvor mange", TempMinusPoint, "slog du?"))
    #points[i-1]-= TempMinusPoint
    # print(scoreboard)
