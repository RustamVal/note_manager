# функция проверки уникальности статуса в словаре 0 - если такого статуса нет, значение ключа - если присутствует
def isstatusunique(in_statuses, in_note_stat):
    l_key=0 # статуса нет в словаре
    for key_dict, f_status in in_statuses.items():
        if f_status == in_note_stat:
            l_key = key_dict # если находим такой статус, запоминаем значение ключа
    return l_key
# функция проверки корректности введенного ключа статуса, True - если такой ключ есть в словаре, False - если нет
def isstatuscorrect(in_key, in_statuses):
    l_result = False
    for key_dict, f_status in in_statuses.items():
        if in_key==key_dict:
            l_result = True
    return l_result

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

#создаем словарь со статусами
statuses = {"1":"новая","2":"в процессе","3":"выполненная","4":"отложенная"}

status_str = ""
#собираем все статусы из словаря в строку
for key, status in statuses.items():
    status_str =status_str + " " + status

#вывод текущего статуса заметки
print("Текущий статус заметки: ",note[2])

while True:
    answer = input("Хотите изменить статус заметки (да/нет)? ")
    if answer == "да":
        # вывод словаря на экран для отображения вариантов выбора
        print("Возможные варианты статуса:")
        for key, status in statuses.items():
            print(key, status)
        # запрос на дальнейшие действия
        new_status = input("Выберите цифру статуса заметки (0 - новый статус, стоп - выход): ")
        if new_status!="стоп": # если введено не стоп обрабатываем команду, если стоп - выходи из цикла
            if new_status=="0": # если выбран вариант добавить значение в словарь
                while True:
                    new_status_name = input("Введите новое название статуса (пустое значение для выхода): ")
                    if new_status_name == "":# если введено пустое значение выходим из цикла
                        break
                    status_key = isstatusunique(statuses,new_status) # проверка на уникальность введенного значения, если нет в словаре - добавляем
                    if status_key==0:
                        statuses[str(len(statuses.items())+1)] = new_status_name #добавляем новое значение в словарь
                        print("Добавлен новый статус в словарь: ", new_status_name)
                        break
                    else:
                        print("Ошибка! Данный статус уже присутствует в словаре, повторите ввод")
            else:
                if isstatuscorrect(new_status,statuses)!=0: # проверка корректности введенного значения (наличия в словаре), если все нормально меняем статус
                    note[2]=statuses[new_status]
                    print("Значение статуса успешно изменено. Новое значение: ", note[2])
                    break
                else:
                    print("Введено некорректное значение цифры статуса, проверьте вводимое значение на соответствие словарю статусов")
        else:
            break
    else:
        break
