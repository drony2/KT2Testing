from csv import DictReader
import json

books = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        book = {
            "title": row.get("Title"),
            "author": row.get("Author"),
            "pages": row.get("Pages"),
            "genre": row.get("Genre")
        }
        books.append(book)

with open('users.json', "r") as j:
    users = json.loads(j.read())
    col_user = len(users)
    col_books = len(books)
    one_user_book = col_books
    one_user_remaining_books = col_books % col_user

result = []
for user in users:
    user_books = []
    for i in range(one_user_book):
        if books:
            book = books.pop(0)
            user_books.append(book)
    if one_user_remaining_books > 0 and books:
        book = books.pop(0)
        user_books.append(book)
        one_user_remaining_books -= 1

    result.append({
        "name": user.get("name"),
        "gender": user.get("gender"),
        "address": user.get("address"),
        "age": user.get("age"),
        "books": user_books
    })


with open("ress.json", 'w') as f:
    json.dump(result, f, indent=4)


