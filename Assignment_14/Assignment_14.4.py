class student :
    school_name= " sulakhe highschool "
    def __init__ (self,A,B):
        self.name=A
        self.rollno=B
    def student_details(self):
        print("in student detsils:")
        print("Name : ",self.name,", Roll no. : ",self.rollno)  

    def school_details(self):
        print("in school details : ")
        print("SCHOOL NAME : ",student.school_name)

    


def main():
    obj1=student("aniket",101)   
    obj2=student("chandu",102)     

    obj1.student_details()
    obj1.school_details()

    student.school_name= "shivaji mahavidyalaya"     # we can access class variable all over the program by using class name
    obj1.student_details()
    obj1.school_details()

    print()

    obj2.student_details()
    obj2.school_details()

    student.school_name= "COEP"
    obj2.student_details()
    obj2.school_details()

if __name__=="__main__":
    main()