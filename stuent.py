class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []

    def get_grades(self):
        return self.__grades

    def add_grades(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def calculate_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def calculate_grade(self):
        if not self.__grades:
            return "N/A"
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grades:", self.__grades)
        print("Average:", self.calculate_average())
        print("Letter Grade:", self.calculate_grade())


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)
        self.major = major

    def display_info(self):
        print("undergraduate student")
        super().display_info()
        print("major:", self.major)


class GraduateStudent(Student):
    def __init__(self, name, student_id, program_title):
        super().__init__(name, student_id)
        self.program_title = program_title

    def display_info(self):
        print("graduate student")
        super().display_info()
        print("program title:", self.program_title)


def grades_sort(students):
    n = len(students)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if students[j].calculate_average() > students[j + 1].calculate_average():
                students[j], students[j + 1] = students[j + 1], students[j]
    return students


s1 = GraduateStudent("Alice", 1001, "Master of Computer Science")
s2 = UndergraduateStudent("Bob", 2001, "Business")
s3 = UndergraduateStudent("Carol", 2002, "Biology")
s4 = GraduateStudent("Dave", 1002, "Master of Data Science")

s1.add_grades(88)
s1.add_grades(92)
s1.add_grades(79)

s2.add_grades(70)
s2.add_grades(85)
s2.add_grades(90)

s3.add_grades(95)
s3.add_grades(91)
s3.add_grades(98)

s4.add_grades(80)
s4.add_grades(85)
s4.add_grades(80)

students = [s1, s2, s3, s4]

for s in grades_sort(students):
    s.display_info()
    print()

print("Empty list:", grades_sort([]))

print("One student:")
for s in grades_sort([s1]):
    print(s.name, round(s.calculate_average(), 2))

print("Equal averages:")
for s in grades_sort([s2, s4]):
    print(s.name, round(s.calculate_average(), 2))


def save_students(students, filename):
    file = open(filename, "w")
    for s in students:
        grades = ";".join(str(g) for g in s.get_grades())
        if isinstance(s, GraduateStudent):
            file.write(f"Graduate,{s.name},{s.student_id},{s.program_title},{grades}\n")
        else:
            file.write(f"Undergraduate,{s.name},{s.student_id},{s.major},{grades}\n")
    file.close()


def load_students(filename):
    students = []
    try:
        file = open(filename, "r")
        for line in file:
            kind, name, sid, extra, grades = line.strip().split(",")
            if kind == "Graduate":
                s = GraduateStudent(name, sid, extra)
            else:
                s = UndergraduateStudent(name, sid, extra)
            for g in grades.split(";"):
                s.add_grades(float(g))
            students.append(s)
        file.close()
    except FileNotFoundError:
        print("File not found")
    return students


save_students(students, "students.txt")
for s in load_students("students.txt"):
    s.display_info()
load_students("missing.txt")