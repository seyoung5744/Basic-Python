import python_mini_project.booking.booingDao as bd

class BookingService:
    def __init__(self):
        self.dao = bd.BookingDao()

    def getBookedSeat(self, index):
        seat_info = self.dao.getBookedSeat(index)
        return seat_info