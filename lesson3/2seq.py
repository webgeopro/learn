"""
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается 
в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9
"""
str = input('Введите любые цифры через запятую: ')
lst = str.replace(" ", "").split(sep=',')
#lst = ['1', ' 2', ' 2', ' 2', ' 2', ' 3', ' 4', ' 5', ' 6', ' 6', ' 6']
lst = list(map(int, lst))
set(lst)
print(set(lst))