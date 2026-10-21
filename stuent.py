class student:
    def __inti__(self, name, student_id, grade):
        self.name=name
        self.student_id=student_id
        self.grade=[]

    def display_info(self):
        print("student name:", self.name)
        print("student id:", self.student_id)
        print("student grade:", self.grade)
class undergraduatestudent(student):
     def __init__(self, name, student_id, major):
         super __init__(self, name, student_id)
         self.major=major 

     def display_info(self):
         print("undergraduate student")
         super().display_info()
         print("major:", self.major)

class graduatestudent(student):
      def __init__(self, name, student_id, program_title):
          super __init__(self, name, student_id)
          self.program_title=program_title

      def display_info(self):
          print("graduate studet")
          super().display_info()
          print("program title:",  self.program_title)

        