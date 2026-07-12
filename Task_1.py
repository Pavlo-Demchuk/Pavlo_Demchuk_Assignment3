book_profile = {
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info": {
        "name": "Наукова думка",
        "city": "Київ"
    }
}

name = book_profile.get("publisher_info").get("name")
year = book_profile.get("year") or "Рік видання невідомий"

print(f"Книга \"{book_profile.get("title")}\" автора {book_profile.get("author")} була видана у місті {book_profile.get("publisher_info").get("city")} в {year}")
