# Импортируем datetime для работы с датами

from datetime import date

# Создаем переменные

created_date = date.today()
issue_date = date(2025, 1, 21)

# Выводим переменные в лаконичном формате

print('Дата создания заметки:', f"{created_date:%d-%m}")
print('Дата истечения заметки (дедлайн):', f"{issue_date:%d-%m}")