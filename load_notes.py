def load_notes_from_file(filename):
    try:
        notes = []
        with open(filename,"r",encoding="utf-8") as file:
            while True:
                str = file.readline()
                if not str:
                    break
                s1 = str.find(":")
                s2 = str.find("n")
                if s1 > 0 and s2 != 0:
                    if str[0:s1:] == "Имя пользователя":
                        username = str[s1 + 2:s2:]
                    elif str[0:s1:] == "Заголовок":
                        title = str[s1 + 2:s2:]
                    elif str[0:s1:] == "Описание":
                        content = str[s1 + 2:s2:]
                    elif str[0:s1:] == "Статус":
                        status = str[s1 + 2:s2:]
                    elif str[0:s1:] == "Дата создания":
                        created_date = str[s1 + 2:s2:]
                    elif str[0:s1:] == "Дедлайн":
                        issue_date = str[s1 + 2:s2:]
                        note = {"username":username,"title":title,"content":content,"status":status,"created_date":created_date,"issue_date":issue_date}
                        notes.append(note)
    except FileNotFoundError:
        new_file = open(filename, "w")
        new_file.close()
        print(f"Файл {filename} не найден. Создан новый файл.")
    except UnicodeDecodeError:
        print(f"Ошибка декодировки файла {filename}.")
    except PermissionError:
        print(f"Ошибка доступа к файлу {filename}.")
    if len(notes) == 0:
        print(f"В файле {filename} заметок не найдено.")
    return notes

if __name__ == '__main__':
    print(load_notes_from_file("example.txt"))