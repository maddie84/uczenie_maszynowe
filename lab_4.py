# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:26:27 2022

@author: jazwi
"""
from uczenie_maszynowe.klasy import Book, Employee, Library, Order, Student

library1 = Library.Library('Sosnowiec', 'Wyspianskiego', '10-200', '8-20', '123456789')
library2 = Library.Library('Katowice', 'Pilsudskiego', '40-200', '7-16', '635271899')

book1 = Book.Book(library1, '20.09.2010', 'Stephen', 'Shawn', '243')
book2 = Book.Book(library1, '11.11.2010', 'Kobe', 'King', '654')
book3 = Book.Book(library2, '02.02.2010', 'Christie', 'Anne', '112')
book4 = Book.Book(library2, '15.09.2020', 'Chandler', 'Sting', '209')
book5 = Book.Book(library1, '20.09.2002', 'Jim', 'Ring', '543')

employee1 = Employee.Employee('Kasia', 'Kowal', '20.01.2021', '01.01.1999',
                     'Chorzow', 'Rewolucjonistow', '42-600', '098765432')
employee2 = Employee.Employee('Robert', 'Kozak', '20.11.2021', '12.12.1999',
                     'Katowice', 'Lipowa', '42-600', '088323432')
employee3 = Employee.Employee('Macej', 'Niestoszewska', '21.01.2021', '09.09.1999',
                     'DG', 'Kwiatowa', '42-600', '1424162')

student3 = Student.Student('Magda', [99, 23, 290])
student4 = Student.Student('Hubert', [87, 19, 78])
student5 = Student.Student('Karolina', [56, 29, 54])

order1 = Order.Order(employee1, student5, [book5, book1], '20.09.2022')
order2 = Order.Order(employee2, student3, [book2, book4, book1], '12.10.2022')

print(order1)
print(order2)