# Import syntax: from file_name import ClassName
from student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add(self, s):
        self.students.append(s)
        print(f'Student {s.name} added to {self.name} school.')

    def remove(self, s):
        # defensive programming: check if the student is in the school before removing
        if s not in self.students:
            print(f'Student {s.name} is not in {self.name} school.')
            return
        
        self.students.remove(s)
        print(f'Student {s.name} removed from {self.name} school.')

    def show(self):
        print(f'School: {self.name}, Number of students: {len(self.students)}')
        for s in self.students:
            s.show()

# Test some School objects
if __name__ == '__main__':
    john = Student('John Doe', 20, 80)
    paul = Student('Paul Smith', 22, 90)

    greenwich = School('Greenwich')
    greenwich.add(john)
    greenwich.add(paul)

    greenwich.show()