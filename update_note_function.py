from datetime import date
import datetime
# функция проверки на непустое значение
def is_str_correct(l_str,l_field_name):
    l_flag=True
    if l_str=="":
        l_flag=False
        print(f"Значение поля ''{l_field_name}'' не может быть пустым. Повторите ввод")
    return l_flag
# функция проверки корректности статуса, True - если статус есть в словаре, False - если нет
def is_status_correct(in_status, in_statuses):# входные данные in_status - значение статуса для проверки, in_statuses - словарь возможных статусов
    l_result = False
    for key_dict, f_status in in_statuses.items():
        if f_status == in_status:
            l_result = True
    if not l_result:
        print("Ошибка в введенном значение статуса. Проверьте правильность написания!")
        print("Возможные варианты значения:")
        for key_dict, f_status in in_statuses.items():
            print(f_status)
    return l_result

# функция проверки корректности ввода даты
def is_date_correct(l_date):
    convert_date = None
    try:
        format_date = '%d-%m-%Y'
        convert_date = datetime.datetime.strptime(l_date, format_date).date()  # попытка конвертации строки в дату, если формат неверный, сработает исключение
    except:
        print("Введен некорректный формат даты, Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024, повторите ввод")
    return convert_date

def update_note(in_note, in_exception_list, in_statuses): # входной параметр словарь со значениями полей заметки
    print("Ваша заметка: ", in_note)
    print("Вы можете изменить значения в следующих полях:")
    l_field_list = []
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

def fill_notes():
    new_note = {"id":"1", "name": "Антон", "titles": "Список для чтения",
                "content": "Достоевский, Тургенев, Маркс, Энгельс", "status": "В процессе", "create_date": "01-09-2024",
                "issue_date": "31-05-2025"}
    l_notes= [new_note]
    return l_notes

if __name__ == '__main__':
    # включаем в список исключения поля, которые нельзя редактировать
    exception_list=["id","create_date"]
    # создаем словарь со статусами
    statuses = {"1":"новая","2":"в процессе","3":"выполнено"}
    # заполяем заметку значениями по умолчанию
    new_note = fill_notes()
    # вызываем функцию обновления заметки
    update_note(new_note[0], exception_list, statuses)
    print (new_note)