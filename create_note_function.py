from datetime import date
import datetime
# функция проверки корректности статуса, True - если статус есть в словаре, False - если нет
def is_status_correct(in_status, in_statuses):# входные данные in_status - значение статуса для проверки, in_statuses - словарь возможных статусов
    l_result = False
    for key_dict, f_status in in_statuses.items():
        if f_status == in_status:
            l_result = True
    if not l_result:
        print("Ошибка в введенном значение статуса. Проверьте правильность написания!")
    return l_result

# функция проверки не пустого значения
def is_str_correct(l_str,l_field_name):
    l_flag=True
    if l_str=="":
        l_flag=False
        print(f"Значение поля ''{l_field_name}'' не может быть пустым. Повторите ввод")
    return l_flag

# функция проверки корректности ввода даты
def is_date_correct(l_date):
    convert_date = None
    if l_date != "":
        try:
            format_date = '%d-%m-%Y'
            convert_date = datetime.datetime.strptime(l_date, format_date).date()  # попытка конвертации строки в дату, если формат неверный, сработает исключение
        except:
            print("Введен некорректный формат даты, Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024, повторите ввод")
    else:
        convert_date = date.today() + datetime.timedelta(days = 7)
    return convert_date

# функция создания заметки
def create_note():
    # блок проверки правильности ввода имени пользователя
    flag_correct_input = False
    while not flag_correct_input:
        username = input("Введите имя пользователя: ")
        flag_correct_input = is_str_correct(username, "Имя пользователя")

    # блок проверки правильности ввода заголовка заметки
    flag_correct_input = False
    while not flag_correct_input:
        title = input("Введите заголовок заметки: ")
        flag_correct_input = is_str_correct(title, "Заголовок заметки")

    # блок проверки правильности ввода описания заметки
    flag_correct_input = False
    while not flag_correct_input:
        content = input("Введите описание заметки: ")
        flag_correct_input = is_str_correct(content, "Описание заметки")

    # блок проверки правильности ввода статуса заметки
    flag_correct_input = False
    while not flag_correct_input:
        status = input("Введите статус заметки (новая, в процессе, выполнено): ")
        flag_correct_input = is_status_correct(status, statuses)

    create_date = date.today()

    # блок проверки правильности ввода дедлайна, по умолчанию (пустое значение) - 7 дней с момента создания
    flag_correct_input = False
    while not flag_correct_input:
        issue_date = input("Введите дату дедлайна (день-месяц-год). Пустое значение ввода устанавливает срок 7 дней: ")
        correct_date = is_date_correct(issue_date)
        if correct_date is not None:
            flag_correct_input = True

    return {"username": username, "title": title, "content": content, "status": status, "create_date": create_date,
            "issue_date": correct_date}

statuses = {"1":"новая","2":"в процессе","3":"выполнено"}
if __name__ == '__main__':
    # создаем словарь со статусами

    new_note = create_note()
    print(new_note)
