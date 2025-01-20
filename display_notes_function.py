def display_notes(in_notes):
    if len(in_notes)==0:
        print("У вас нет сохранённых заметок.")
    else:
        print("Список заметок:")
        print("------------------------------")
        note_num = 0
        for note in in_notes:
            note_num += 1
            print(f"Заметка №{note_num} ")
            print(f"Имя пользователя: {note["username"]}")
            print(f"Заголовок: {note["title"]}")
            print(f"Описание: {note["content"]}")
            print(f"Статус: {note["status"]}")
            print(f"Дата создания: {note["created_date"]}")
            print(f"Дедлайн: {note["issue_date"]}")
            print("------------------------------")

if __name__ == '__main__':
    display_notes([])
    notes = [
            {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
             'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]
    display_notes(notes)
    notes.append({'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
             'created_date': '25-11-2024', 'issue_date': '01-12-2024'})
    display_notes(notes)