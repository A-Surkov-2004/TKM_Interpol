def get():  # Инпут таблицы (не тестировался)
    n = int(input("Введите количество известных пар x y(x)"))
    print("Введите ", n, " пар {x y(x)} \n(каждая пара на отдельной строке)")
    v = {}

    for i in range(n):
        s = input()
        s.split()
        v[s[0]] = s[1]

    return v


def getX():  # инпут Х для поиска (не тестировался)
    n = int(input("Введите количество Х, У от которых необходимо найти"))
    xv = [n]
    print("Введите " + str(n) + " значений Х \n(каждое значение на отдельной строке)")
    for i in range(n):
        xv[n] = int(input())
    return xv


global v


def func1(x0, x1):
    global v
    return (v[x1] - v[x0]) / (x1 - x0)


def func2(x0, x1, x2):
    global v
    return (func1(x1, x2) - func1(x0, x1)) / (x2 - x0)


def solve(xv):
    allAns = []
    for X in xv:
        dif = X - list(v)[0]
        x0 = list(v)[0]
        y0 = v[x0]
        i0 = 0
        index = 0

        for i in list(v):  # find x0 y0
            if abs(X - i) < dif:
                x0 = i
                y0 = v[i]
                i0 = index
                dif = abs(X - i)
            index += 1

        allDy = [[]] * 3
        allDy[1] = [0] * (len(v) - 1)
        allDy[2] = [0] * (len(v) - 2)

        print(y0, func1(list(v)[i0], list(v)[i0 + 1]) * (X - x0),
              func2(x0, list(v)[i0 + 1], list(v)[i0 + 2]) * (X - x0) * (X - list(v)[i0 + 1]))

        ans = y0 + func1(list(v)[i0], list(v)[i0 + 1]) * (X - x0) + func2(x0, list(v)[i0 + 1], list(v)[i0 + 2]) * (
                X - x0) * (X - list(v)[i0 + 1])

        allAns.append("Y(" + str(X) + ") = " + str(ans))
    for i in allAns:
        print(i)


def test():  # Удобный способ захардкоженного инпута (запускается внизу программы)
    global v
    v = {0.103: 2.01284,
         0.108: 2.03342,
         0.115: 2.06070,
         0.120: 2.07918,
         0.128: 2.10721,
         0.136: 2.13354,
         0.141: 2.14922,
         0.150: 2.17609}
    vx = [0.112, 0.133]
    solve(vx)


def main():
    solve(getX())


test()
