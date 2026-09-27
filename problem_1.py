class Student:
    def __init__(self, name, student_id, email, age, department, marks):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.__marks = marks

    def display_info(self):
        print("\nStudent Information")
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    # default argument = method overloading
    def calculate_result(self, bonus=0):
        total_marks = self.__marks + bonus

        if total_marks >= 80:
            grade = "A+"
        elif total_marks >= 70:
            grade = "A"
        elif total_marks >= 60:
            grade = "B"
        elif total_marks >= 50:
            grade = "C"
        elif total_marks >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Marks:", total_marks)
        print("Grade:", grade)

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, marks, semester):
        super().__init__(name, student_id, email, age, department, marks)
        self.semester = semester

    # overriding parent method
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)


class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        marks,
        research_topic
    ):
        super().__init__(name, student_id, email, age, department, marks)
        self.research_topic = research_topic

    # overriding parent method
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print("Research Topic:", self.research_topic)


# Creating students

student1 = UndergraduateStudent(
    "Radia",
    "CSE101",
    "radia@gmail.com",
    23,
    "CSE",
    85,
    6
)

student2 = GraduateStudent(
    "Nadia",
    "CSE201",
    "nadia@gmail.com",
    25,
    "CSE",
    72,
    "Artificial Intelligence"
)


# Display information

student1.display_info()
print("Type:", student1.get_student_type())
student1.calculate_result()

print("\n-------------------")

student2.display_info()
print("Type:", student2.get_student_type())
student2.calculate_result(3)


# Polymorphism

print("\nStudent Types:")

students = [student1, student2]

for student in students:
    print(student.get_student_type())