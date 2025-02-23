import random
lines = 1000
columns = 1000
def main():
    matrix = [] #Создаем пустой список
    for i in range(lines):
        rows = []
        for i in range(columns):
            rows.append(random.randint(10,40)) #Генерируем случайное чсло
        matrix.append(rows) #Заполняем список поэлементно
