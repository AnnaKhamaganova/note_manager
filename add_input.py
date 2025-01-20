# Импортируем datetime для работы с датами

import datetime as DT

# Просим пользователя ввести данные

username = input('Введите имя пользователя: ')
title = input('Введите название заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
temp_created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
temp_issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год": ')

# Переводим полученные даты из строк в даты

created_date = DT.datetime.strptime(temp_created_date, '%d-%m-%Y').date()
issue_date = DT.datetime.strptime(temp_issue_date, '%d-%m-%Y').date()