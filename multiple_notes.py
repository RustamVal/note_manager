import datetime
from datetime import date

# функция проверки корректности введенного ключа статуса, True - если такой ключ есть в словаре, False - если нет
def isstatuscorrect(in_key, in_statuses):
    l_result = False
    for key_dict, f_status in in_statuses.items():
        if in_key==key_dict:
            l_result = True
    return l_result
# функция проверки корректности ввода даты
def isdatecorrect(ldate):
    flag_correct = True
    try:
        format_date = '%d-%m-%Y'
        convert_date=datetime.datetime.strptime(ldate,format_date)  # попытка конвертации строки в дату, если формат неверный, сработает исключение
        flag_correct = True
    except:
        print("Введен некорректный формат даты, Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024, повторите ввод")
        flag_correct = False
    return flag_correct
# функция проверки не пустого значения
def isstrcorrect(l_str,l_field_name):
    l_flag=True
    if l_str=="":
        l_flag=False
        print(f"Значение поля ''{l_field_name}'' не может быть пустым")
    return l_flag
print("Добро пожаловать в '"'Менеджер заметок'"'! Вы можете добавить новую заметку")
notes=[]

#создаем словарь со статусами
statuses = {"1":"новая","2":"в процессе","3":"выполнено"}

status_str = ""
#собираем все статусы из словаря в строку
for key, status in statuses.items():
    status_str =status_str + str(key) + " " + status + ","
flag_add_new_note=True
#блок ввода новых заметок
note_id=0 #идентификатор заметки
while flag_add_new_note:
    note_id+=1 #увеличение счетчика идентификатора
# ввод и проверка на непустое значение Имени пользователя
    flag_correct_input = False
    while not flag_correct_input:
        user_name=input("Введите имя пользователя: ")
        flag_correct_input = isstrcorrect(user_name, "Имя пользователя")
# ввод и проверка на непустое значение Заголовка заметки
    flag_correct_input = False
    while not flag_correct_input:
        title=input("Введите заголовок заметки: ")
        flag_correct_input = isstrcorrect(title,"Заголовок")
# ввод и проверка на непустое значение Описания заметки
    flag_correct_input = False
    while not flag_correct_input:
        content=input("Введите описание заметки: ")
        flag_correct_input = isstrcorrect(content, "Описание заметки")
# ввод и проверка на корректное значение Статуса заметки
    flag_correct_input = False
    while not flag_correct_input:
        status_num=input(f"Выберите цифру статуса заметки ({status_str[:len(status_str)-1:]}): ")# берем строку без последней запятой
        flag_correct_input = isstatuscorrect(status_num, statuses)
        if flag_correct_input:  # проверка корректности введенного значения (наличия в словаре), если все нормально меняем статус
            status = statuses[status_num]
        else:
            print("Введено некорректное значение цифры статуса, проверьте вводимое значение на соответствие словарю статусов")
# ввод и проверка на правильность ввода значение Даты создания Заметки
    flag_correct_input = False
    while not flag_correct_input:
        create_date=input("Введите дату создания (день-месяц-год): ")
        flag_correct_input = isdatecorrect(create_date)
# ввод и проверка на правильность ввода значение Даты дедлайна Заметки
    flag_correct_input = False
    while not flag_correct_input:
        deadline_date=input("Введите дедлайн (день-месяц-год): ")
        flag_correct_input = isdatecorrect(deadline_date)
#внесение введенных значений в словарь
    new_note={}
    new_note["id"]=note_id
    new_note["name"]=user_name
    new_note["titles"]=title
    new_note["content"]=content
    new_note["status"]=status
    new_note["created"]=create_date
    new_note["deadline"]=deadline_date
    notes.append(new_note)
    wanna_new=input("Хотите добавить ещё одну заметку? (да/нет)")
    if wanna_new!="да":
        flag_add_new_note=False
#блок вывода заметок на экран
print("Список заметок:")
for note in notes:
    print(note["id"]," Имя: ",note["name"])
    print("   Заголовок: ",note["titles"])
    print("   Описание: ", note["content"])
    print("   Статус: ", note["status"])
    print("   Дата создания: ", note["created"])
    print("   Дедлайн: ", note["deadline"])