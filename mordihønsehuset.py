# todo: (priotitet 1)
# lav et bedre 'game loop', som tjekker, hvor mange point hver spiler har, så man er ude, når man har - point
# fioutput 'træk fra point' delen (kommer an på hvor mange gange man slår det antal øjne, som man fik over 30)
# lav bedre output format, og game flow (prettytables)
# lav et function som tjekker om hvornår en spiller vinder

from prettytable import PrettyTable

players = []
points = []

print("hvor mange spillere er der?")
a = int(input("> "))


def scoreboard():
    j = 0
    output = PrettyTable()
    output.field_names = ["navn", "point"]
    for player in players:
        output.add_row([player, points[j]])
        j += 1
    else:
        return output


def point(arg1):
    return (arg1 - 30)


i = 1

while i <= a:
    print("indtast spiller", i)
    player = input()
    players.append(player)
    i += 1

else:
    for player in players:
        points.append(30)
    else:
        print(scoreboard())

while points[0] and points[1] > 0:
    h = 0
    for player in players:
        print("hvor mange point fik", player, "?")
        rpoint = int(input("> "))
        if rpoint > 30:
            if h == 1:
                points[h - 1] = points[h - 1] - (rpoint - 30)
            else:
                points[h + 1] = points[h + 1] - (rpoint - 30)
        else:
            points[h] = points[h] + point(rpoint)
        h += 1
    else:
        print(scoreboard())


# FTODO:
    # lav programmet til et spil, dvs. gøre så der bliver simuleret terning slag for hver spiller hver
    # runde, hvor de skal vælge en eller flere terninger fra(antallet af terninger mindskes af antallet, der tages fra)
    # indtil alle terningen er valgt
