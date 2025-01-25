def save_notes_to_file(notes, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            if file.writable():
                for note in notes:
                    file.write(f"Имя пользователя: {note["username"]}\n")
                    file.write(f"Заголовок: {note["title"]}\n")
                    file.write(f"Описание: {note["content"]}\n")
                    file.write(f"Статус: {note["status"]}\n")
                    file.write(f"Дата создания: {note["created_date"]}\n")
                    file.write(f"Дедлайн: {note["issue_date"]}\n")
                    file.write(f"---\n")
            else:
                print(f"Ошибка сохранения. Файл {filename} не открыт для записи")
            file.close()
    except PermissionError:
        print(f"Ошибка доступа к файлу {filename}.")

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

if __name__ == '__main__':
    notes = default_notes()
    save_notes_to_file(notes,"example.txt")
