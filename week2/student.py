class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show(self):
        print(f'Student: {self.name}, Age: {self.age}, Grade: {self.grade}')


# Test some Student objects
if __name__ == '__main__':
    john = Student('John Doe', 20, 80)
    john.show()

    paul = Student('Paul Smith', 22, 90)
    paul.show()