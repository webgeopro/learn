bol = True
while bol:
    year = int(input('Введите год рождения А.С Пушкина: '))
    if year == 1799:
        day = int(input('Введите день рождения А.С Пушкина: '))
        while day != 6:
            day = int(input('Введите день рождения А.С Пушкина: '))
        else:
            print('Верно')
            bol = False
