import save_all_books

def remove_book(all_books):
    title =input("Enter Book Title : ")
    for book in all_books:
        if book['Title'] == title:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print('Book Removed successfully')
            return all_books
        else:
            print('This Book is not Founded ')



