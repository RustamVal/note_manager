username = input("Введите имя пользователя: ")
title1 = input("Введите основной заголовок заметки: ")
title2 = input("Введите 2-й заголовок: ")
title3 = input("Введите 3-й заголовок: ")
content = input("Введите содержание заметки: ")
status = input("Укажите статус заметки (новая, выполняется, выполнена): ")
created_date = input("Укажите дату создания заметки в формате dd-mm-yyyy: ")
issue_date = input("Укажите плановую дату создания заметки в формате dd-mm-yyyy: ")

titles = [title1, title2, title3]

note = [username, content, status, created_date, issue_date, titles]

print("\nВывод данных по заметке \n",note,"\n")
print("Имя пользователя: ", note[0])
print("Заголовки заметки: ", note[5])
print("Описание заметки: ", note[1])
print("Статус заметки: ", note[2])
print("Дата создания заметки: ", note[3])
print("Дедлайн заметки : ", note[4])
