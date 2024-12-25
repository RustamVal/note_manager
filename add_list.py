username = input("Введите имя пользователя: ")
title1 = input("Введите основной заголовок заметки: ")
title2 = input("Введите 2-й заголовок: ")
title3 = input("Введите 3-й заголовок: ")
content = input("Введите содержание заметки: ")
status = input("Укажите статус заметки (новая, выполняется, выполнена): ")
created_date = input("Укажите дату создания заметки в формате dd-mm-yyyy: ")
issue_date = input("Укажите плановую дату создания заметки в формате dd-mm-yyyy: ")

title_lst = []
title_lst.append(title1)
title_lst.append(title2)
title_lst.append(title3)

print(username,title1,title2,title3,content,status,created_date,issue_date)
print("Список: ",title_lst)