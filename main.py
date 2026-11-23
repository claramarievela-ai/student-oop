class Student:
    # constructor to initialize the student's name, email, and grades
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades          # a list of integers

    def add_grade(self, grade):
        self.grades.append(grade) # adds a new grade to the student's list of grades

    def average_grade(self):
        if not self.grades:           # avoids dividing by zero if the list is empty
            return 0
        return sum(self.grades) / len(self.grades) # calculates the average of the student's grades

    # display the student's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

    # returns the student's grades as a tuple (which can't be changed)
    def grades_tuple(self):
        return tuple(self.grades)

# create three student objects with their respective names, emails, and grades
s1 = Student("Agatha", "agatha@gmail.com", [90, 85, 92]) #name, email, grades
s2 = Student("Alfred", "alfred@gmail.com", [88, 91, 89]) #name, email, grades
s3 = Student("Vivian", "vivian@gmail.com", [100, 99, 100]) #name, email, grades

# add two new grades for each student
s1.add_grade(93)
s1.add_grade(90)
s2.add_grade(90)
s2.add_grade(88)
s3.add_grade(100)
s3.add_grade(99)

# loop through the list of students and print their average grades
students = [s1, s2, s3] 
for student in students:
    student.display_info() # gives the student's name, email, and grades
    print(f"{student.name}'s Average Grade: {student.average_grade()}") # gives the student's average grade

# map out each email to its Student object
student_dict = {student.email: student for student in students} # creates a dictionary with email as key and Student object as value
print(list(student_dict.keys()))   # ['agatha@gmail.com', 'alfred@gmail.com', 'vivian@gmail.com']

# safely look up a student by email; returns None if the email is not found
def get_student_by_email(email):
    return student_dict.get(email) # returns the Student object if found, otherwise None    

# test the lookup with a real and a fake email

found = get_student_by_email("agatha@gmail.com")
print(found.name)

missing = get_student_by_email("nobody@gmail.com")
if missing is None:
    print("Student not found.")

# collect every grade from every student into a set (duplicates are removed automatically)
unique_grades = set()
for student in students:
    unique_grades.update(student.grades)
print(unique_grades)

# get one student's grades as a tuple and print it
t = s1.grades_tuple()
print(f"{s1.name}'s Grades as Tuple: {t}")

# try to change the first grade; tuples are immutable, so this raises a TypeError
try:
    t[0] = 100
except TypeError as e:
    print(f"Error: {e}")

# for each student: remove the last grade, then show the first grade, last grade and how many are left
for student in students:
    removed = student.grades.pop()                     # removes the last grade from the list
    print(f"{student.name}: removed {removed}")
    print(f"  First grade: {student.grades[0]}")
    print(f"  Last grade: {student.grades[-1]}")
    print(f"  Number of grades: {len(student.grades)}")