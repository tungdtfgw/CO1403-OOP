from student import Student
from school import School

class SchoolProgram:
    def __init__(self):
        self.school = School('Greenwich')

    def run(self):
        running = True
        while running:
            self.show_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.school.show()
            elif choice == '4':
                running = False
            else:
                print('Invalid choice. Please try again.')

        print('Program ended. See you next time!')

    def show_menu(self):
        print('1. Add student')
        print('2. Remove student')
        print('3. Show school information')
        print('4. Exit')

    def add_student(self):
        # ask user to enter student information
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        grade = int(input('Enter student grade: '))
        # create a Student object and add it to the school
        student = Student(name, age, grade)
        self.school.add(student)

    def remove_student(self):
        # ask user to enter student information
        name = input('Enter student name: ')
        for s in self.school.students:
            if s.name == name:
                self.school.remove(s)
                return
        
        print('Student not found.')
    
    def school_show(self):
        self.school.show()


if __name__ == '__main__':
    program = SchoolProgram()
    program.run()