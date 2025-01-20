from search_notes_function import search_notes
from search_notes_function import print_note
from delete_note import delete_note
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes

def default_notes():

    in_notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'},
        {'username': 'Георгий', 'title': 'Список дел', 'content': 'Съездить в магазин', 'status': 'в процессе',
         'created_date': '20-12-2024', 'issue_date': '26-12-2024'},
        {'username': 'Мария', 'title': 'Список для чтения', 'content': 'Шекспир', 'status': 'выполнено',
         'created_date': '20-09-2024', 'issue_date': '31-12-2024'}
    ]
    return in_notes

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
        print("Заметка успешно добавлена\n")
    elif your_choice == 2:
        print("------------------------------------------------")
        print("Ваш выбор - вывод всех заметок:")
        print("------------------------------------------------")
        if len(notes) == 0:
            print("Список заметок пуст\n")
        else:
            display_notes(notes)
    elif your_choice == 3:
        print("------------------------------------------------")
        print("Ваш выбор - обновить заметку")
        print("------------------------------------------------")
        display_notes(notes)
        flag_correct_input = False
        while not flag_correct_input:
            try:
                rec_num = int(input("Выберите порядковый номер заметки: "))
                if len(notes) >= rec_num > -1:
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
                display_notes(notes)
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
        print("Список заметок заполнен значениями по умолчанию, количество добавленных заметок - ", len(notes))
        print()
    elif your_choice == 6:
        print("------------------------------------------------")
        print("Ваш выбор - выйти из программы. Спасибо за использование")
        print("------------------------------------------------")
        break
    else:
        print("Некорректный выбор пункта меню. Выберите цифру от 1 до 7")
