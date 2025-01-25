import json

# функция записи заметки в файл в формате json
def save_notes_json(notes, filename):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            j_file = json.dump(notes, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f"Ошибка доступа к файлу {filename}. Попробуйте выбрать другой файл для записи" )
# заполнение Notes значениями по умолчанию
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
    notes = []
    notes = default_notes()
    save_notes_json(notes,"data.json")