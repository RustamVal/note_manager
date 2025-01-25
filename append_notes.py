def append_notes_to_file(notes, filename):
    try:
        file = open(filename,"a",encoding="utf-8")
    except FileNotFoundError:
        file = open(filename, "w", encoding="utf-8")
    for note in notes:
        file.write(f"Имя пользователя: {note["username"]}\n")
        file.write(f"Заголовок: {note["title"]}\n")
        file.write(f"Описание: {note["content"]}\n")
        file.write(f"Статус: {note["status"]}\n")
        file.write(f"Дата создания: {note["created_date"]}\n")
        file.write(f"Дедлайн: {note["issue_date"]}\n")
        file.write(f"---\n")
    file.close()

def fill_notes():
    new_note = {"username": "Антон", "title": "Список для чтения",
                "content": "Достоевский, Тургенев, Маркс, Энгельс", "status": "В процессе", "created_date": "01-09-2024",
                "issue_date": "31-05-2025"}
    l_notes= [new_note]
    new_note = {"username": "Анна", "title": "Купить билеты", "content": "Нижневартовск-Лима на 28.02.2025",
                "status": "В процессе", "created_date": "01-11-2024", "issue_date": "31-01-2025"}
    l_notes.append(new_note)
    new_note = {"username": "Аннита", "title": "Зарегистрироваться на конкурсе", "content": "Конкурс лучший по профессии среди тех, кому за 75",
                "status": "В процессе", "created_date": "01-01-2025", "issue_date": "31-03-2025"}
    l_notes.append(new_note)
    new_note = {"username": "Антон", "title": "Список покупок",
                "content": "Купить ананас и горошек к новому году",
                "status": "В процессе", "created_date": "01-12-2024", "issue_date": "31-12-2024"}
    l_notes.append(new_note)
    return l_notes

if __name__ == '__main__':
    notes = fill_notes()
    append_notes_to_file(notes,"example.txt")