from drivex.models.book import Book

class BookService:
    bookDetails = {}

    def add_book(self, id, title, price, stockcount=1):
        book = Book(id=id, title=title, price=price, stockcount=stockcount)
        self.__class__.bookDetails[id] = book
        return book

    def isStock(self, id):
        return self.__class__.bookDetails[id].stockcount > 0

    def increase_book_count(self, id):
        self.__class__.bookDetails[id].stockcount += 1
    
    def decrease_book_count(self, id):
        self.__class__.bookDetails[id].stockcount -= 1

    def get_book_price(self, id):
        return self.__class__.bookDetails[id].price

    def search_book_by_name(self, name):
        for id, details in self.__class__.bookDetails:
            if details.title == name:
                return self.__class__.bookDetails[id]
    
    # def search_book_by_author(self, author):
    #     for id, details in self.__class__.bookDetails:
    #         if details.author == author:
    #             return self.__class__.bookDetails[id]

    def delete_book_by_id(self, id):
        pass

