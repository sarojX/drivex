from drivex.dao.book_dao import BookService
from drivex.dao.member_dao import MemberService

class IssueBook:
    def __init__(self, member_service, book_service):
        self.member = member_service
        self.book = book_service

    def issue_book(self, member_id, book_id):
        if self.book.isStock(book_id) and self.member.isEligible(member_id):
            self.book.decrease_book_count(book_id)
            book_amount = self.book.get_book_price(book_id)
            self.member.assign_book(member_id, book_id, book_amount)
            print("Success")
        else:
            print("Can't Issue")

    def return_book(self, member_id, book_id, amount_paid):
        self.book.increase_book_count(book_id)
        self.member.deassign_book(member_id, book_id, amount_paid)
