from save_all_books import save_all_books
import datetime
def update_book(all_books):
    book_title = input("Enter Book Title : ")
    for book in all_books:
        if book['Title'] == book_title:
            print(f'Founded Book {book['Title']}')
            title = input('Enter Book`s Title : ')
            author = input('Enter Book`s Author : ')
            year = int(input('Enter Book Publication Year : '))
            price = input('Enter Book`s Price : ')

            uptime = datetime.datetime.now().strftime('%d/%m/%Y  %H:%M:%S')
            try:
                quantity = int(input('Enter Book Quantity : '))
            except ValueError:
                print("Invalid Input !!! Plz Input Integer")
            book['Title']= title
            book['Author']= author
            book['Price']= price
            book['Year']= year
            book['Uptime'] = uptime
            book['Quantity'] = quantity

            save_all_books(all_books)
            print('Book Updated successfully')
            return all_books
        else:
            print('This Book is not Founded ')
