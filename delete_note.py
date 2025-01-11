# инициализация значений заметок по умолчанию
def fill_notes():
    new_note = {"id": "1", "name": "Антон", "titles": "Список для чтения",
                "content": "Достоевский, Тургенев, Маркс, Энгельс", "status": "В процессе", "created": "01-09-2024",
                "deadline": "31-05-2025"}
    l_notes= [new_note]
    new_note = {"id": "2", "name": "Анна", "titles": "Купить билеты", "content": "Нижневартовск-Лима на 28.02.2025",
                "status": "В процессе", "created": "01-11-2024", "deadline": "31-01-2025"}
    l_notes.append(new_note)
    new_note = {"id": "3", "name": "Аннита", "titles": "Зарегистрироваться на конкурсе", "content": "Конкурс лучший по профессии среди тех, кому за 75",
                "status": "В процессе", "created": "01-01-2025", "deadline": "31-03-2025"}
    l_notes.append(new_note)
    new_note = {"id": "4", "name": "Антон", "titles": "Список покупок",
                "content": "Купить ананас и горошек к новому году",
                "status": "В процессе", "created": "01-12-2024", "deadline": "31-12-2024"}
    l_notes.append(new_note)
    return l_notes

# форматированный вывод на экран элементов словаря заметки
def print_note(l_note):
    print(l_note["id"], " Имя: ", l_note["name"])
    print("   Заголовок: ", l_note["titles"])
    print("   Описание: ", l_note["content"])
    print("   Статус: ", l_note["status"])
    print("   Дата создания: ", l_note["created"])
    print("   Дедлайн: ", l_note["deadline"])

# удаление в цикле всех заметок имеющих аналогичные имя пользователя или заголовок
def delete_note(name_or_title, in_notes):
    for l_note in in_notes:
        if l_note["name"].lower() == name_or_title or l_note["titles"].lower() == name_or_title:
            in_notes.remove(l_note)
    #return in_notes
# блок инициализации значений

notes = fill_notes() # вызов функции заполнения значений заметок

if len(notes) == 0:
    print ("Список заметок пуст, удалять нечего")
else:
    print("Вот ваш текущий список заметок:")
    for note in notes:
        print_note (note)

# блок удаления заметок
    delete_var = input("Введите имя пользователя или заголовок для удаления заметки (регистр не имеет значения): ")
    num_notes = len(notes) # запоминаем сколько заметок было до удаления
    delete_note(delete_var.lower(), notes)
    if len(notes) != num_notes: # если количество заметок не совпадает выводим информацию сколько удалено
        print(f"Успешно удалено заметок - {num_notes - len(notes)}. Остались следующие заметки:")
        for note in notes:
            print_note(note)
    else: # иначе информируем, что заметок по данным критериям не найдено
        print("Заметок с таким именем пользователя или заголовком не найдено.")
