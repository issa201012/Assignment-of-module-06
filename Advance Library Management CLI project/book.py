import  add_books
import  view_books
import restore_all_book
import update_book
import remove_book
all_books =[]
print("Welcome to our book library")
while True:

    print("\n1. Add Book")
    print("2. View Book")
    print('3. Update Book')
    print('4. Remove Book')
    print("5. Exit")

    op = input("\nEnter Your Options : ")
    print('\n')
    all_books = restore_all_book.restore_all_book(all_books)
    if op == '5':
        print("\nThanks for using our book library.")
        break
    elif op == '1':
        all_books = add_books.add_books(all_books)
    elif op == '2':
        view_books.view_books(all_books)
    elif op == '3':
        all_books = update_book.update_book(all_books)
    elif op == '4':
        all_books = remove_book.remove_book(all_books)
    else:
        print("Invalid Input !!!")

