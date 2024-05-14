import sys
sys.path.append('/Users/91977/Desktop/drivex')

from drivex.dao.book_dao import BookService
from drivex.dao.member_dao import MemberService
from drivex.app.inventory import Inventory
from drivex.app.issue_book import IssueBook

book = BookService()
member = MemberService()
inventory = Inventory(book)
issue_book = IssueBook(member, book)

mem1 = member.add_member(1, "John")
mem2 = member.add_member(2, "Alex")
mem3 = member.add_member(3, "Tom")
mem4 = member.add_member(4, "Harry")
mem5 = member.add_member(5, "Robin")

inventory.bulk_import_books(num_books=2)

issue_book.issue_book(1, 1) #sucess
issue_book.issue_book(1, 1) #Can't issue

