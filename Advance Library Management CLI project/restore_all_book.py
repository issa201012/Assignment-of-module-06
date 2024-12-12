import json

def restore_all_book(all_books):
    with open('all_books.json','r') as fp:
        # for book in all_books:
            # line = f'{book['Title']},{book['Author']},{book['ISBN']},{book['Price']},{book['Year']},{book['Addtime']}'
            all_books =json.load(fp)
            return all_books