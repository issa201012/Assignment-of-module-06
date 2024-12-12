import json
def save_all_books(all_books):
    with open('all_books.json','w') as fp:
        # for book in all_books:
            # line = f'{book['Title']},{book['Author']},{book['ISBN']},{book['Price']},{book['Year']},{book['Addtime']}'
            json.dump(all_books, fp ,indent=4)