class student:
    def __inti__(self, name, student_id, grade):
        self.name=name
        self.student_id=student_id
        self.__grade=[]

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

    def display_info(self):
        print("student name:", self.name)
        print("student id:", self.student_id)
        print("student grade:", self.grade)
class undergraduatestudent(student):
     def __init__(self, name, student_id, major):
         super(). __init__(self, name, student_id)
         self.major=major 

     def display_info(self):
         print("undergraduate student")
         super().display_info()
         print("major:", self.major)

class graduatestudent(student):
      def __init__(self, name, student_id, program_title):
          super().__init__(self, name, student_id)
          self.program_title=program_title

      def display_info(self):
          print("graduate studet")
          super().display_info()
          print("program title:",  self.program_title)

        