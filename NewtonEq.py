import matplotlib.pyplot as plt


def test():
    # v = {0: 0,
    #      2: 1,
    #      3: 3,
    #      5: 2}
    v = {
        -1:-2,
        1:1,
        5: 10,
        10:1,
        15: 1,
        20:10,
        25:1,
        28:-2,

    }
    solve(v)


def calcDivDif(v):
    divDif = [0] * len(list(v))
    for i in range(len(list(v))):
        divDif[i] = [0] * len(list(v))

    for i in range(len(list(v))):
        divDif[0][i] = v[list(v)[i]]

    for i in range(1, len(list(v))):
        for j in range(0, len(list(v)) - i):
            divDif[i][j] = (divDif[i - 1][j + 1] - divDif[i - 1][j]) / (list(v)[j + i] - list(v)[j])
    # print(divDif)
    for i in divDif:
        print(i)
    return divDif


# def calcQarray(n):

def buildString(v, divDif):
    vx = list(v)
    xstring = ''
    totalString = ''
    for i in range(len(divDif)):
        totalString += '(' + str(divDif[i][0]) + xstring + ')+'

        xstring += f'*(x - {vx[i]})'
    totalString = totalString[:len(totalString) - 1]
    print(totalString)
    return totalString


def solve(v: dict):
    divDif = calcDivDif(v)
    eq = buildString(v, divDif)
    print(list(v.values()))
    minx = min(list(v))
    maxx = max(list(v))
    difx = maxx - minx
    miny = min(v.values())
    maxy = max(v.values())
    dify = maxy - miny
    plt.axis([minx - difx / 2, maxx + difx / 2, miny - dify / 2, maxy + dify / 2])
    allx = [0] * 1002
    index = 0
    nowx = minx - difx / 2
    while nowx < maxx + difx / 2:
        allx[index] = nowx
        nowx += ((maxx + difx / 2) - (minx - difx / 2)) / 1000
        index += 1
    ally = [0] * 1002
    for i in range(len(allx)):
        x = allx[i]
        y = eval(eq)
        ally[i] = y
    plt.plot(allx, ally, "bo")
    plt.plot(list(v.keys()), list(v.values()), 'ro')
    plt.grid(True)
    plt.show()


test()
