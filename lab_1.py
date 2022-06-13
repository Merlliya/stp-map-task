file = open("access.log") #открытие файта
data = [] #создание списка
s = file.readline().split() #считывание первой строки файла
while s != []: #проверка на непустую строку
    