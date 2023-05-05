import csv
import json

from files_hm import JSON_USERS_PATH, CSV_BOOKS_PATH



users_list = []
# Открытие файла с пользователя users.json через константу JSON_USERS_PATH
with open(JSON_USERS_PATH) as f:
    users = json.load(f)
# Обработка и запись в новый список пользователей с атрибутами
for user in users:
    user_dict = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    users_list.append(user_dict)

# Открытие файла с книгами books.json через константу CSV_BOOKS_PATH и запись с атрибутами, аналогично как в reference.json
books_list = []
with open(CSV_BOOKS_PATH) as f:
    books = csv.DictReader(f)
    for book in books:
        books_dict = {
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        }
        books_list.append(books_dict)


# Подсчет количества книг на пользователя из расчета кол-во книг/кол-во юзеров через divmod
total_users = len(users_list)
total_books = len(books_list)
books_per_user, extra_books = divmod(total_users, total_books)


id = 0
for user in users_list: #перебор пользователей

    for i in range(books_per_user): #распределение книг между пользователями
        user['books'].append(books_list[id])
        id += 1
    # распределение оставшихся книг
    if extra_books > 0:
        user['books'].append(books_list[id])
        id += 1
        extra_books -= 1

#распеределеные книги записываю в result.json с отступами в 4ре проблема
with open("result.json", "w")as f:
    result = json.dumps(users_list, indent=4)
    f.write(result)