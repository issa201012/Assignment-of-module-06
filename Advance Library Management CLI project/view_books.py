import json


def view_books(all_books):
    with open('all_books.json','r')as fp:
        all_books = json.load(fp)
    if all_books != []:
        for book in all_books:
            print(f' {book['Title']} Book`s Details : "Book`s Title : "{book['Title']} | "Author : " {book['Author']} " | ISBN : "{book['ISBN']}" | Price : "{book['Price']} | Year : "{book['Year']}| Quantity of Book : {book['Quantity']} | Adding Time : "{book['Addtime']}| Last Updating  Time : {book['Uptime']}\n')
    else:
        print('No books found')

