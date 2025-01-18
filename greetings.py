# Импортируем datetime для работы с датами

from datetime import date

# Создаем переменные

username = 'Аня Хамаганова'
title = 'Заметка'
content = 'Тестовая заметка'
status = 'new'
created_date = date.today()
issue_date = date(2025, 1, 21)

# Выводим переменные

print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', f"{created_date:%d-%m-%Y}")
print('Дата истечения заметки (дедлайн): ', f"{issue_date:%d-%m-%Y}")