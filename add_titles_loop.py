# Объявляем список в котором будут храниться заголовки
titles = []

# Объявляем переменную, которая будет условием для выполнения цикла (True - выполняется, False - не выполняется)
running = True

# В цикле просим пользователя вводить заголовки
while running:
    title = input('Введите заголовок (или оставьте пустым для завершения): ')
    # Проводим проверку введенной строки, если она пустая - в переменную условия передаем False для завершения цикла
    if title == '':
        running = False
    # Если введенная строка не пустая, то проверяем наличие такого заголовка в списке
    elif title in titles:
        print('Такой заголовок уже есть')
    # Если все в порядке - добавляем новый заголовок в список заголовков
    else: titles.append(title)

# Выводим все заголовки (с помощью for выводим по одному элементу списка до тех пор, пока список не закончится)
print('Заголовки заметки:')
for title in titles:
    print('-', title)