# Address Class
class Address:
    def __init__(self, street, city, zipCode):
        self.street = street
        self.city = city
        self.zipCode = zipCode

    def display(self):
        print("Address:", self.street, ",", self.city, "-", self.zipCode)


# Student Class
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self._age = 0   # protected
        self.set_age(age)   # using setter manually
        self.address = address   # HAS-A relationship
        self.courses = []

    # Setter for age (basic validation)
    def set_age(self, age):
        if age > 0 and age <= 120:
            self._age = age
        else:
            print("Invalid age! Setting default age = 18")
            self._age = 18

    # Getter for age
    def get_age(self):
        return self._age

    # Add course
    def add_course(self, course):
        self.courses.append(course)

    # Display details
    def display(self):
        print("\nName:", self.name)
        print("Age:", self.get_age())
        self.address.display()

        print("Courses:")
        if len(self.courses) == 0:
            print("No courses")
        else:
            for c in self.courses:
                print("-", c)


# ScholarshipStudent Class (Inheritance)
class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarshipAmount):
        Student.__init__(self, name, age, address)  # basic (no super shortcut)
        self.scholarshipAmount = scholarshipAmount

    def display(self):
        Student.display(self)   # calling parent method
        print("Scholarship Amount:", self.scholarshipAmount)


# ---------------- USER INPUT ----------------

# Address input
street = input("Enter street: ")
city = input("Enter city: ")
zipCode = input("Enter zip code: ")

addr = Address(street, city, zipCode)

# Student input
name = input("Enter student name: ")
age = int(input("Enter age: "))

# Ask type
choice = input("Is this a scholarship student? (yes/no): ")

if choice == "yes":
    amount = int(input("Enter scholarship amount: "))
    student = ScholarshipStudent(name, age, addr, amount)
else:
    student = Student(name, age, addr)

# Add courses
n = int(input("How many courses to add? "))

for i in range(n):
    course = input("Enter course: ")
    student.add_course(course)

# Mutable behavior demonstration
extra = student.courses
extra.append("Extra Course Added Automatically")

# Display
print("\n----- STUDENT DETAILS -----")
student.display()