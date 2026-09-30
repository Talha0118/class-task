# TASK 
class College:
    def __init__(self, name, student, teacher, address):
        self.name = name
        self.student = student
        self.teacher = teacher
        self.address = address
        
class Student:
    def __init__(self, roll, name, marks, address):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.address = address
        
class Teacher:
    def __init__(self, name, salary, department, address):
        self.name = name
        self.salary = salary
        self.department = department
        self.address = address
        
class Address:
    def __init__(self, city, pin):
        self.city = city
        self.pin = pin
        
address1 = Address("Pune",411038)
address_stu = Address("Pune",411007)
address_college = Address("Karve Nagar Pune",411411)
teacher1 = Teacher("Atul Sir",600000,"Python",address1)
student1 = Student("Talha",18,95,address_stu)
college1 = College("The Kiran Academy",student1,teacher1,address_college)

# Student details
print("Student Details")
print(college1.student.roll)
print(college1.student.name)
print(college1.student.marks)
print(college1.student.address.city)
print(college1.student.address.pin)


# Teacher details
print("Teacher Details")
print(college1.teacher.name)
print(college1.teacher.salary)
print(college1.teacher.department)
print(college1.teacher.address.city)
print(college1.teacher.address.pin)

# College details
print("College Details")
print(college1.name)
print(college1.address.city)
print(college1.address.pin)