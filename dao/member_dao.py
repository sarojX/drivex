from drivex.models.member import Member

class MemberService:
    memberDetails = {}

    def add_member(self, id, name):
        member = Member(id=id, name=name)
        self.__class__.memberDetails[id] = member
        return member

    def isEligible(self, member_id):
        return self.__class__.memberDetails[member_id].dues < 500

    def assign_book(self, member_id, book_id, amount):
        self.__class__.memberDetails[member_id].books.add(book_id)
        self.__class__.memberDetails[member_id].dues += amount

    def deassign_book(self, member_id, book_id, amount):
        self.__class__.memberDetails[member_id].books.remove(book_id)
        self.__class__.memberDetails[member_id].dues -= amount
    