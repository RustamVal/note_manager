titles = []
i = 1
title = ""
while True:
    title = input(f"Введите {i} заголовок: ")
    if title != "":
        titles.append(title)
    else:
        break
    i += 1
print(f"Введено заголовков {i-1}:\n",titles)