from idlelib.run import Executive


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise InvalidStudentAdd()
        if isinstance(student, Student):
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'

class InvalidStudentAdd(Exception):
    pass

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 21, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 22, 'Lizaa', 'Taylorr', 'AN145')
st4 = Student('Female', 23, 'Lizaaa', 'Taylorrr', 'AN145')
st5 = Student('Female', 24, 'Lizaaaa', 'Taylorrrr', 'AN145')
st6 = Student('Female', 25, 'Lizaaaaa', 'Taylorrrrr', 'AN145')
st7 = Student('Female', 26, 'Lizaaaaaa', 'Taylorrrrrr', 'AN145')
st8 = Student('Female', 27, 'Lizaaaaaaa', 'Taylora', 'AN145')
st9 = Student('Female', 28, 'Lizaaaaaaaa', 'Taylorw', 'AN145')
st10 = Student('Female', 29, 'Lizaaaaaaaaa', 'Taylort', 'AN145')
st11 = Student('Male', 31, 'Petia', 'Vacul', 'AN148')
gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except InvalidStudentAdd as e:
    print("Студентов в группе не может быть больше 10")
print(gr)


print('-' * 100)

print(gr)
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!