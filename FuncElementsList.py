import random
rows = 1000
columns = 1000
def main(rows,columns):
    my_list = [[random.randint(10,40) for j in range(columns)] for i in range(rows)]
    #Создаем матрицу при помощи генератора