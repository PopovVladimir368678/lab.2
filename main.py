import csv   # R3140 368678 Popov лабораторная 2
import os


def cvet(code):  # объявляю функцию покраски
    return f'\u001b[{code}m'   # возвращяю код конкретного цвета


black = cvet(40)    # каждому нужному цвету присваиваю результат вызова функции cvet от нужного значения
red = cvet(41)
green = cvet(42)
yellow = cvet(43)
white = cvet(47)
end = cvet(0)

        # задание 1

print('Флаг')
for i in range(6):
     print(green + '      ' * 4 + red + '      ' * 6 + end)  # рисую верхнюю половину флага. 6 строк
for i in range(6):
     print(green + '      ' * 4 + yellow + '      ' * 6 + end)   # нижнюю

                # задание 2
print('Узор')
square = black + ' ' * 3  # чёрный квадратик
no = white + ' ' * 3  # пустой квадратик

print((no * 4 + square * 1 + no * 3) * 4 + no * 1 + end) # первая строчка
for i in range(4): # повторяюсь столько раз, сколько рядов надо
    print((no * 3 + square * 3 + no * 2) * 4 + no * 1 + end)  # рисую верхнюючасть строки узора, без уже нарисованой пересекающейся строки
    print((no * 2 + square * 5 + no * 1) * 4 + no * 1 + end)
    print((no * 1 + square * 7 + no * 0) * 4 + no * 1 + end)

    print(no * 0 + square * 33 + end)  # рисую середину строки узора

    print((no * 1 + square * 7 + no * 0) * 4 + no * 1 + end)  # дорисовываю стороку узора с нижней строчкой.
    print((no * 2 + square * 5 + no * 1) * 4 + no * 1 + end)
    print((no * 3 + square * 3 + no * 2) * 4 + no * 1 + end)
    print((no * 4 + square * 1 + no * 3) * 4 + no * 1 + end)

            # задание 3

print('График y = x + 1')
razmer = 11                                     # задаю размер
pole = [[0 for i in range(razmer)] for t in range(razmer)]  # создаю масив, матрицу нулей размера razmer
for i in range(razmer):
     for t in range(razmer):
         if t == 0:
             pole[i][t] = razmer - i - 1
         if i == razmer - 1:
             pole[i][t] = t   # пробегаю по всем "клеточкам" и задаю значения клеточкам у края поля


for x in range(1, razmer):
     if 0 <= razmer - 2 - x:
         pole[razmer - x - 2][x] = '/'  # ставлю '/' во все клетки принадлежащие графику


for i in range(razmer-1): #  для всех клкточек
     riad = ''
     for t in range(razmer):
         if pole[i][t] == '/':
             riad += black + '  '  # задаю цвет линии графика
         elif pole[i][t] == 0:
             riad += white + '  ' + black  # задаю цвкт фона и ограничиваю покраску
         else:
             riad += white + str(pole[i][t]) + ' '  # задаю чвет и значения оси у
     print(riad)
print(white + '0 1 2 3 4 5 6 7 8 9 10' + black)  # подписываю ось х и ограничиваю покраску



                    # задание 3

print('Процентное соотношение')

bolee_150 = 0
menee_150 = 0  # задаю 2 счётчика
with open('books.csv') as csvfile:  # открываю файл
    tablica = list(csv.reader(csvfile, delimiter=';'))[1:]
    for book in tablica:  # передираю записи
        if float(book[7].replace(',', '.')) > 150:
            bolee_150 += 1
        else:
            menee_150 += 1 # cчитаю сколько в каждой группе
symma = bolee_150 + menee_150
procehtbolee_150 = round(bolee_150 / symma * 100)
procentmenee_150 = round(menee_150 / symma * 100)  # считаю процент одних и вторых


razmer = 20
for i in range(razmer):
    if ((20-i)*5 > procehtbolee_150) and ((20-i+1)*5 > procentmenee_150):
        print(black + str((20-i)*5) + '% |' + black)
    elif ((20-i)*5 < procehtbolee_150) and ((20-i+1)*5 > procentmenee_150):
        print(black + str((20 - i) * 5) + '% |' + ' ' * 16 + white + '    ' + black)
    elif ((20-i)*5 > procehtbolee_150) and ((20-i+1)*5 < procentmenee_150):
        print(black + str((20 - i) * 5) + '% |' + ' ' * 6 + white + '    ' + black)
    else:
        if (20-i) > 1:
            print(black + str((20 - i) * 5) + '% |' + ' ' * 6 + white + '    ' + black + ' ' * 6 + white + '    ' + black)
        else:
            print(black + str((20 - i) * 5) + '%  |' + ' ' * 6 + white + '    ' + black + ' ' * 6 + white + '    ' + black)

print(black + '     _ _ _ _ _ _ _ _ _ _ _ _')
print(black + '           >150     <=150')   # рисую график по строкам.


