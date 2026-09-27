# Student Management System

A simple **Student Management System built with Python** to practice and demonstrate the core concepts of **Object-Oriented Programming (OOP)**.

This project was created as part of the **Django Batch-13, Module-3 assignment**.

## About the Project

The system manages basic information about different types of students.

There is a main `Student` class, which is inherited by two specialized classes:

* `UndergraduateStudent`
* `GraduateStudent`

Each student has common information such as name, student ID, email, age, department, and marks. The child classes add their own information, such as semester or research topic.

The project is kept intentionally simple so that the OOP concepts can be easily understood.

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

## Classes

### 1. Student

`Student` is the parent class.

It contains common student information:

* Name
* Student ID
* Email
* Age
* Department
* Marks

It also contains methods to:

* Display student information
* Calculate result and grade
* Get the type of student

### 2. UndergraduateStudent

`UndergraduateStudent` inherits from the `Student` class.

It adds:

* Semester

It also overrides the `get_student_type()` method to identify the student as an undergraduate student.

### 3. GraduateStudent

`GraduateStudent` also inherits from the `Student` class.

It adds:

* Research topic

It overrides the `get_student_type()` method to identify the student as a graduate student.

## OOP Concepts Demonstrated

This project covers the main OOP concepts required for the assignment.

### Class & Object

Classes are created for different types of students, and objects are created from those classes.

```python
student1 = UndergraduateStudent(...)
student2 = GraduateStudent(...)
```

### Attributes

Student-related information is stored using attributes such as:

```python
self.name
self.student_id
self.age
self.department
```

### Methods

The classes contain methods for different student operations, such as:

```python
display_info()
calculate_result()
get_student_type()
```

### Inheritance

`UndergraduateStudent` and `GraduateStudent` inherit from the `Student` class.

```python
class UndergraduateStudent(Student):
```

```python
class GraduateStudent(Student):
```

### Method Overriding

Both child classes override the `get_student_type()` method from the parent class.

This allows each type of student to return different information.

### Polymorphism

Different student objects can use the same method:

```python
student.get_student_type()
```

but the result depends on which type of student the object represents.

### Method Overloading

A default argument is used in the `calculate_result()` method:

```python
def calculate_result(self, bonus=0):
```

This allows the method to work both with and without an additional bonus mark.

### Encapsulation

Private attributes are used for sensitive student information:

```python
self.__email
self.__marks
```

This demonstrates encapsulation in Python.

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Open the project folder

```bash
cd Student-Management-System
```

### 3. Run the Python file

```bash
python student_management.py
```

The program will display the student information, student type, calculated result, and a simple polymorphism example.

## Example

The program creates an undergraduate student and a graduate student and displays their information.

```text
Student Information
Name: Radia
ID: CSE101
Email: radia@gmail.com
Age: 23
Department: CSE
Semester: 6

Type: Undergraduate Student
Marks: 85
Grade: A+
```

## Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**

## Assignment

This project was created for practicing:

* Classes and Objects
* Attributes and Methods
* Inheritance
* Polymorphism
* Method Overriding
* Method Overloading
* Encapsulation

---

**Created as part of Django Batch-13 — Module 3**
