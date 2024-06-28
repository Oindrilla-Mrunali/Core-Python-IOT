student_name = input("Enter name : ")
student_age = int(input("Enter age : "))
print("The name of stude is {0} and the age is {1}".format(student_name,student_age))
print("Student age is of type ",type(student_age))
print("Student name is of type ",type(student_name))
if student_age >= 18:
    if student_age >= 18 and student_age <= 30:
        if student_name == "Oindrilla":
            print(f"Hello {student_name}!! Welcome aboard!!")
        elif student_name == "Mrunali":
            print(f"Hello {student_name}!! Hope you are doing good!!!")
        else:
            pass