import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >= ", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("строк: ", 1, None)
columns = get_int("столбцов: ", 1, None)
minimum = get_int("минимум (или Enter для 0): ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("максимум (или Enter для " + str(default) + "): ",
                  minimum, default)

row = 0
while row < rows: # обрабатывает строки
    line = ""
    column = 0
    while column < columns: # обрабатывает столбцы 
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10: # обрабатывает символы
            s = "" + s
        line += s
        column += 1
    print(line)
    row +=1

    
