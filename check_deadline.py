import datetime
from datetime import date

#Инициируем и создаем заметку
username = "Leonardo"
title = "Тестовая заметка"
content = "Заметка для тестирования функционала и возможностей"
status = "в процессе"
created_date = "22-12-2024"
issue_date = "29-12-2024"
titles = []
titles.append(title)
#создаем заметку
note = [username, content, status, created_date, issue_date, titles]

# инициализация и вывод на экран сегодняшней даты
today_date=date.today()
print("Текущая дата: ",today_date)

#блок ввода даты дедлайна с проверкой корректности ввода
flag_correct_input = False
issue_date_conv=today_date
while not flag_correct_input:
    issue_date = input("Введите дату дедлайна (в формате день-месяц-год): ")
    format = '%d-%m-%Y'
    try:
        issue_date_conv = datetime.datetime.strptime(issue_date,format) # попытка конвертации строки в дату, если формат неверный, сработает исключение
        flag_correct_input = True
    except:
        print("Введен некорректный формат даты, Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024, повторите ввод")
        flag_correct_input = False
    finally:
        print()
estimate_days = today_date-issue_date_conv.date()
#блок сопоставления даты дедлайна и текущей даты
if today_date>=issue_date_conv.date():
    if  today_date==issue_date_conv.date():
        print("Дедлайн сегодня!")
    else:
        print(f"Внимание! Дедлайн истёк {estimate_days.days} дня назад")
else:
    print(f"До дедлайна осталось {estimate_days.days} дня")
