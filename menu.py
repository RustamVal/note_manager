from datetime import date
import datetime

# Функция для поиска подстроки в строке. Для поиска переводит все в нижний регистр
def is_str_in_field(in_str, field):
    if (field.lower().find(in_str.lower())) != -1:
        return True
    else:
        return False

# функция вывода всех заметок в отформатированном виде
def display_notes(in_notes):
    note_num = 0
    for note in in_notes:
        note_num += 1
        print(f"{note_num}. Имя пользователя: {note["username"]}, Заголовок: {note["title"]}, Описание: {note["content"]}, Статус: {note["status"]}, Дедлайн: {note["issue_date"]}")

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
        flag_correct_input = is_str_correct(title,"Заголовок заметки")

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

    return {"username":username, "title":title, "content":content, "status":status, "create_date":create_date, "issue_date":correct_date}

# функция для заполнения заметок дефолтными значениями
def default_notes():

    in_notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    return in_notes

# функция обновления заметки
def update_note(in_note, in_exception_list, in_statuses): # входной параметр словарь со значениями полей заметки
    print("Ваша заметка: ", in_note)
    print("Вы можете изменить значения в следующих полях:")
    l_field_list=[]
    for l_key, l_value in in_note.items():
        if l_key not in in_exception_list:
            print(l_key)
            l_field_list.append(l_key)
    l_correct_input = False
    while not l_correct_input:
        edit_field = input("Введите название поле для изменения: ")
        l_correct_input = edit_field in l_field_list
        if not l_correct_input:
            print("Ошибка! Наименование поля для изменения введено некорректно. Повторите ввод")

    l_correct_input = False
    while not l_correct_input:
        new_value = input(f"Введите новое значение поля {edit_field}: ")
        if edit_field == "issue_date":
            if is_date_correct(new_value) is not None:
                l_correct_input = True
        elif edit_field == "status":
            l_correct_input = is_status_correct(new_value, in_statuses)
        else:
            l_correct_input = is_str_correct(new_value, edit_field)
    in_note[edit_field] = new_value
    print("Заметка успешно обновлена")

# удаление в цикле всех заметок имеющих аналогичные имя пользователя или заголовок
def delete_note(name_or_title, in_notes):
    # for l_note in in_notes:
    for i in range(len(in_notes)-1,-1,-1):
        l_note = in_notes[i]
        if l_note["username"].lower() == name_or_title or l_note["title"].lower() == name_or_title:
            in_notes.remove(l_note)
    #return in_notes

# Функция для форматированного вывода на печать
def print_note (in_note, in_note_num):
    if in_note_num == 1:
        print("Найдены заметки:")
    print("Заметка №", in_note_num, ": ")
    print("Имя пользователя: ", in_note["username"])
    print("Заголовок: ", in_note["title"])
    print("Описание: ", in_note["content"])
    print("Статус: ", in_note["status"])

# Функция поиска в заметках по ключевому полю или статусу
def search_notes(in_notes, keyword=None, status=None):
    if len(in_notes) == 0:
        print("Список заметок пуст")
        return
    rec_num = 0 # счетчик найденных записей
    for l_note in in_notes:
        try:
            flag_keyword = (is_str_in_field(keyword, l_note["title"])) or (is_str_in_field(keyword,l_note["username"]))  or (is_str_in_field(keyword,l_note["content"]))
        except:
            flag_keyword = False
        flag_status = (l_note["status"] == status)
        if (keyword is not None) and (status is not None):
            result = flag_status and flag_keyword
        elif (keyword is not None):
            result = flag_keyword
        elif (status is not None):
            result = flag_status
        if result:
            rec_num += 1  # если запись удовлетворяет условиям печатаем и увеличиваем счетчик
            print_note(l_note, rec_num)
    if rec_num == 0:
        print("Заметок удовлетворяющих условиям поиска не найдено")

# создаем словарь со статусами
statuses = {"1":"новая","2":"в процессе","3":"выполнено"}
# включаем в список исключения поля, которые нельзя редактировать
exception_list=["id","create_date"]

notes = []
while True:
    print("МЕНЮ КОМАНД:")
    print("1: Создать новую заметку (вызов функции create_note()).")
    print("2: Показать все заметки (вызов функции display_notes()).")
    print("3: Обновить заметку (вызов функции update_note()).")
    print("4: Удалить заметку (вызов функции delete_note()).")
    print("5: Найти заметки (вызов функции search_notes()).")
    print("7: Заполнить дефолтными значениями.")
    print("6: Выйти из программы.\n")
    try:
        your_choice = int(input("Введите ваш выбор команды (цифра от 1 до 7): "))
    except:
        your_choice = 0
        print("Некорректный выбор номера пункта. Проверьте вводимое значение (цифра от 1 до 7)")
    if your_choice == 1:
        print("------------------------------------------------")
        print("Ваш выбор - создать новую заметку")
        print("------------------------------------------------")
        note = create_note()
        notes.append(note)
        print("Заметка успешно добавлена")
    elif your_choice == 2:
        print("------------------------------------------------")
        print("Ваш выбор - вывод всех заметок:")
        display_notes(notes)
        print("------------------------------------------------")
    elif your_choice == 3:
        print("------------------------------------------------")
        print("Ваш выбор - обновить заметку")
        print("------------------------------------------------")
        display_notes(notes)
        flag_correct_input = False
        while not flag_correct_input:
            try:
                rec_num = int(input("Выберите порядковый номер заметки: "))
                if len(notes) > rec_num > -1:
                    flag_correct_input = True
                else:
                    print("Некорректный выбор номера записи, уточните выбранное значение")
            except:
                print("Некорректный выбор номера записи, уточните выбранное значение")
                flag_correct_input = False
        update_note(notes[rec_num-1],[],[])
    elif your_choice == 4:
        print("------------------------------------------------")
        print("Ваш выбор - удалить заметку(заметки)")
        print("------------------------------------------------")
        if len(notes) == 0:
            print("Список заметок пуст, удалять нечего\n")
        else:
            delete_var = input("Введите имя пользователя или заголовок для удаления заметки (регистр не имеет значения): ")
            num_notes = len(notes)  # запоминаем сколько заметок было до удаления
            delete_note(delete_var.lower(), notes)
            if len(notes) != num_notes:  # если количество заметок не совпадает выводим информацию сколько удалено
                print(f"Успешно удалено заметок - {num_notes - len(notes)}. Остались следующие заметки:")
                for note in notes:
                    print_note(note)
            else:  # иначе информируем, что заметок по данным критериям не найдено
                print("Заметок с таким именем пользователя или заголовком не найдено.")
    elif your_choice == 5:
        print("------------------------------------------------")
        print("Ваш выбор - найти заметку")
        print("------------------------------------------------")
        keyword = input("Введите ключевое слово для поиска (пустое значение - не искать по ключевому слову): ")
        if keyword == "":
            keyword = None
        status = input("Введите статус для поиска (пустое значение - не искать по ключевому слову): ")
        if status == "":
            status = None
        search_notes(notes, keyword, status)
    elif your_choice == 7:
        print("------------------------------------------------")
        print("Ваш выбор - заполнение заметок значениями по умолчанию")
        print("------------------------------------------------")
        notes = default_notes()
    elif your_choice == 6:
        print("------------------------------------------------")
        print("Ваш выбор - выйти из программы")
        print("------------------------------------------------")
        break
    else:
        print("Некорректный выбор пункта меню. Выберите цифру от 1 до 7")
