import requests
from drivex.dao.book_dao import BookService

class Inventory:
    def __init__(self, bookservice):
        self.bookservice = bookservice

    def bulk_import_books(self, num_books=10):
        page_no = 1
        count = 0
        id, price = 0, 100
        while count < num_books:
            url = f'https://gutendex.com/books/?page={page_no}&search=and'
            response = requests.get(url)
            if response.status_code == 200:
                books_data = response.json()
                for book in books_data['results']:
                    title = book['title']
                    self.bookservice.add_book(id=id, title=title, price=price, stockcount=1)
                    id += 1
                    count += 1
            else:
                print("Failed to fetch books")

            page_no += 1

    def import_book_by_count(self, book_id, title, price, stockcount):
        self.bookservice.add_book(id=book_id, title=title, price=price, stockcount=stockcount)