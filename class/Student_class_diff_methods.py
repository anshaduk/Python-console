class Student:
    school='abc school'
    def __init__(self,name,roll,study_class):
        self.name=name
        self.roll=roll
        self.study_class=study_class
    #object/instance method
    def display_student(self):
        print(f"name:{self.name}\nroll_no:{self.roll}\nclass:{self.study_class}")
    #class methods
    @classmethod
    def get_school_name(cls):
        print('school name:',cls.school)
    #static method
    @staticmethod
    def about_us():
        print("This is no one school")
    
s1=Student('Ram','001','9th')
s1.display_student()
Student.get_school_name()
Student.about_us()