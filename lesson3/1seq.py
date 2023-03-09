lst = []
cnt = int(input('Введите количество элементов списка: '))
for i in range(1, cnt+1):
    val = int(input(f'Введите {i} элемент: : '))
    lst.append(val)
lst.sort()
print(lst)