from uczenie_maszynowe.klasy import Book

class Order:

    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def books_description(self):
        all = ""
        for book in self.books:
            all += '\n' + Book.Book.__str__(book)
        return all

    def __str__(self):
        return f'Order by {self.employee}, \nfor {self.student}, ' \
               f'\ncontains: {self.books_description()} ,' \
               f' \nmade on {self.order_date}'
