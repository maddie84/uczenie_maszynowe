class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks) / len(self.marks) > 50:
            return True
        else:
            return False

    def __str__(self):
        return f'Student  {self.name}, with marks {self.marks}'
