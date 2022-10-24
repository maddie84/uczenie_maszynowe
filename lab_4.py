# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:26:27 2022

@author: jazwi
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks)/len(self.marks) > 50:
            return True
        else:
            return False

    def __str__(self):
        return f'Student  {self.name}, with marks {self.marks}'
    
class Library:
    
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        
    def __str__(self):
        return f'Library in  {self.city},{self.street} {self.zip_code}, ' \
               f'open on {self.open_hours}, phone number {self.phone}'
       
class Employee:
    
     def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
         self.first_name = first_name
         self.last_name = last_name
         self.hire_date = hire_date
         self.birth_date = birth_date
         self.city = city
         self.street = street
         self.zip_code = zip_code
         self.phone = phone
         
     def __str__(self):
        return f'Employee {self.first_name} {self.last_name}, ' \
               f'date of birth {self.birth_date} ' \
               f'hired on {self.hire_date}, ' \
               f'lives in {self.city} {self.street} {self.zip_code}, ' \
               f'phone number {self.phone}'
         
class Book:
    
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        
        
    def __str__(self):
        return f'Book from {self.library}, ' \
               f'by {self.author_name} {self.author_surname},' \
               f'publication date {self.publication_date}, ' \
               f'number of pages {self.number_of_pages}'
        
class Order:
    
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
    def books_description(self):
        all = ""
        for book in self.books:
            all += '\n'+Book.__str__(book)
        return all

    def __str__(self):
        return f'Order by {self.employee}, \nfor {self.student}, ' \
               f'\ncontains: {self.books_description()} ,' \
               f' \nmade on {self.order_date}'
               
library1 = Library('Warszawa', 'Kwiatowa', '10-200', '8-20', '123456789')
library2 = Library('Krakow', 'Kotlarska', '40-200', '7-16', '188888889')

book1 = Book(library1, '20.09.2010', 'James', 'Mcgill', '321')
book2 = Book(library1, '11.11.2010', 'Arthur', 'Fresh', '366')
book3 = Book(library2, '02.02.2010', 'Agatha', 'Esd', '491')
book4 = Book(library2, '15.09.2020', 'Jules', 'Bin', '78')
book5 = Book(library1, '20.09.2002', 'Coss', 'Sin', '100')

employee1 = Employee('Ala', 'Kowalska', '20.01.2021', '01.01.1999',
                     'Bytom', 'Kwaka', '42-600', '098765432')
employee2 = Employee('Robert', 'Kowal', '20.11.2021', '12.12.1999',
                     'Chorzow', 'Lipowa', '42-600', '088323432')
employee3 = Employee('Macej', 'Polska', '21.01.2021', '09.09.1999',
                     'T.Gory', 'Lipna', '42-600', '1424162')

student3 = Student('Magda', [99, 23, 290])
student4 = Student('Hubert', [87, 19, 78])
student5 = Student('Karolina', [56, 29, 54])

order1 = Order(employee1, student5, [book5, book1], '20.09.2022')
order2 = Order(employee2, student3, [book2, book4, book1], '12.10.2022')

print(order1)
print(order2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        