from save_all_books import save_all_books
from random import randint
from datetime import datetime
def add_books(all_books):
    title = input('Enter Book`s Title : ')
    author = input('Enter Book`s Author : ')
    year = int(input('Enter Book Publication Year : '))
    price = input('Enter Book`s Price : ')
    isbn = randint(99999,100000)
    addtime = datetime.now().strftime('%d/%m/%Y  %H:%M:%S')
    try:
        quantity = int(input('Enter Book Quantity : '))
    except ValueError:
        print("Invalid Input !!! Plz Input Integer")
    books = {
        'Title': title,
        'Author': author,
        'ISBN': isbn,
        'Price': price,
        'Year': year,
        'Addtime': addtime,
        'Uptime': "Data is not updated",
        'Quantity' : quantity,
    }

    all_books.append(books)
    save_all_books(all_books)
    print('Book Added successfully')
    return all_books