import csv

#creating function which will create a file
def student_detail(std_list):
    std_file = open('student_file','a',newline='')
    writer = csv.writer(std_file)
    if std_file.tell()==0:
        writer.writerow(["Name ","Class ","Roll number ","Age "])

    writer.writerow(std_list)


while True:
    details = str(input("Enter student info in the order [name,class,roll no.,age] with a space: "))
    student_list = details.split(' ')

    student_detail(student_list)

    print("the student details are: ")
    print("name: ",student_list[0],"\nclass: ",student_list[1],"\nroll no.: ",student_list[2],"\nage: ",student_list[3])


    choice = str(input("are the details entered correct? [yes/no]: "))
    if choice=="yes":
        choice2 = str(input("do you want to enter more details? [yes/no]: "))
        if choice2=="yes":
             continue
        elif choice2 =="no":
             print("thank you")
             break
        else:
            print("invalid input")
    elif choice=="no":
        print("enter them again")
        continue
    else:
        print("invalid input")
        continue