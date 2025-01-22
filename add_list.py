# Импортируем datetime для работы с датами

from datetime import datetime

# Просим пользователя ввести данные

username = input('Введите имя пользователя: ')
title1 = input('Введите 3 заголовка заметок: \n1: ')
title2 = input('2: ')
title3 = input('3: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
temp_created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
temp_issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')

# Объединяем заголовки в список

titles = [title1, title2, title3]

# Переводим полученные даты из строк в даты

created_date = datetime.strptime(temp_created_date, '%d-%m-%Y')
issue_date = datetime.strptime(temp_issue_date, '%d-%m-%Y')

# Выводим данные

print('Имя пользователя:', username)
print('Заголовки заметки:', titles)
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', f"{created_date:%d-%m}")
print('Дата истечения заметки (дедлайн):', f"{issue_date:%d-%m}")