# Функция для поиска подстроки в строке. Для поиска переводит все в нижний регистр
def is_str_in_field(in_str, field):
    if (field.lower().find(in_str.lower())) != -1:
        return True
    else:
        return False
# Функция для форматированного вывода на печать

def print_note (in_note, in_note_num):
    if in_note_num == 1:
        print("Найдены заметки:")
    print("Заметка №", in_note_num, ": ")
    print("Имя пользователя: ", in_note["username"])
    print("Заголовок: ", in_note["title"])
    print("Описание: ", in_note["content"])
    print("Статус: ", in_note["status"])
    print()

# Функция поиска в заметках по ключевому полю или статусу
def search_notes(in_notes, keyword=None, status=None):
    if len(in_notes) == 0:
        print("Список заметок пуст")
        return
    rec_num = 0 # счетчик найденных записей
    for l_note in in_notes:
        result = False
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

if __name__ == '__main__':
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    print("Тестирование")
    # первый блок тестирования
    print("Поиск по ключевому слову: Ввод:")
    print("search_notes(notes, keyword='покупок')")
    search_notes(notes,"покупок")
    print("")
    # второй блок тестирования
    print("Поиск по статусу: Ввод:")
    print("search_notes(notes, status='в процессе')")
    search_notes(notes, status='в процессе')
    print("")
    # третий блок тестирования
    print("Поиск по ключевому слову и статусу: Ввод")
    print("search_notes(notes, keyword='работы', status='выполнено')")
    search_notes(notes, keyword='работы', status='выполнено')
