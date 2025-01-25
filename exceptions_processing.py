import save_notes
import load_notes

if __name__ == "__main__":
    notes = save_notes.default_notes()
    filename = "example.txt"
    try:
        save_notes.save_notes_to_file(notes,"example.txt")
    except PermissionError:
        print(f"Ошибка доступа к файлу {filename}. Проверьте корректность указания файла.")
    try:
        load_notes.load_notes_from_file(filename)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Проверьте наличие файла и корректность имени.")
    except UnicodeEncodeError:
        print(f"Ошибка кодировки файла {filename}. Проверьте корректность данных в файле.")
    except Exception as e:
        print(f"Ошибка: {e}")