import math
import matplotlib.pyplot as plt

cycles = 100  # Максимальное количество итераций уточненияя (но обычно заканчивает раньше)
close = 3  # Определяет, что мы считаем за "Близко к концу таблицы" (номер с конца)


def get():  # Инпут таблицы (не тестировался)
    n = int(input("Введите количество известных пар x y(x)"))
    print("Введите ", n, " пар {x y(x)} \n(каждая пара на отдельной строке)")
    v = [n]

    for i in range(n):
        s = input()
        s.split()
        v[i] = [s[0], s[1]]

    return v


def getX():  # инпут Х для поиска (не тестировался)
    n = int(input("Введите количество Х, У от которых необходимо найти"))
    xv = [n]
    print("Введите " + str(n) + " значений Х \n(каждое значение на отдельной строке)")
    for i in range(n):
        xv[n] = int(input())
    return xv


def solve(v, xv):
    # v - массив пар [x,y]
    vcopy = [0] * len(v)
    for i in range(len(v)):
        vcopy[i] = v[i]

    allAns = []
    answersa = []
    answersb = []
    for X in xv:
        dif = X - vcopy[0][0]
        h = abs(vcopy[0][0] - vcopy[1][0])
        x0 = vcopy[0][0]
        y0 = vcopy[0][1]
        i0 = 0
        index = 0
        n = 3

        for i in vcopy:  # find x0 y0
            if abs(X - i[0]) < dif:
                x0 = i[0]
                y0 = i[1]
                i0 = index
                dif = abs(X - i[0])
            index += 1

        u = (X - x0) / h

        v = vcopy[i0-n:i0+n+1]  # делаем обрезание нашемо массиву пар [x,y]
        print(v)


        global cycles
        allDy = [[]] * (cycles + 1)  # allDy массив массивов дельта-ириков. Индекс равен степени дельты. Каждая
        # следующая дельта содержит на 1 элемент меньше передыдущей

        for i in v:  # v - массив пар [x,y]
            allDy[0].append(i[1])  # вносим в allDy[0] наши y
        for i in range(1, cycles + 1):  # подсчёт всех dy со всеми степенями
            allDy[i] = [0] * (len(v) - i)
            for j in range(len(allDy[i])):
                allDy[i][j] = allDy[i - 1][j + 1] - allDy[i - 1][j]

        print('f')
        print(allDy)  # дебажный лог, можно удалить

        global close  # задаётся в верху программы

        ans = y0  # нулевая итерация цикла

        for i in range(1, n+1):

            t1 = u / math.factorial(2 * i - 1)
            t2 = 1
            for j in range(1, i):
                t2 *= u * u - j * j
            t3 = (allDy[2 * i - 1][-(i - 1)+n] + allDy[2 * i - 1][-i+n]) / 2
            s1 = t1 * t2 * t3
            t4 = (u * u) / math.factorial(2 * i)
            t5 = 1
            for j in range(1, i):
                t5 *= u * u - j * j
            t6 = allDy[2*i][-i+n]
            s2 = t4*t5*t6
            print(s1+s2)
            print(s1, s2)
            ans += s1+s2

        allAns.append("Y(" + str(X) + ") = " + str(ans))
        answersa.append(X)
        answersb.append(ans)
    for i in allAns:
        print(i)

    #for i in answers:
    #    v.append(i)
    #v.sort()

    a = [0] * len(v)
    b = [0] * len(v)
    for i in range(len(v)):
        a[i] = v[i][0]
        b[i] = v[i][1]

    plt.axis([min(a)-(min(a)+max(a))/4, max(a)+(min(a)+max(a))/4, min(b)-(min(b)+max(b))/4, max(b)+(min(b)+max(b))/4])

    plt.plot(a,b,'r')
    plt.plot(a, b, 'ro')

    plt.plot(answersa, answersb,'bo')
    plt.grid(True)
    plt.show()


def test():  # Удобный способ захардкоженного инпута (запускается внизу программы)
    v = [
        [0,0],
         [1, 2],
         [2, 5],
         [3, 10],
         [4, 15],
         [5, 20],
         [6, 22],
         [7, 24],
         ]
    vx = [4.3, 3.4]
    solve(v, vx)


def main():
    solve(get(), getX())


test()
