import os
import platform

global listStd
listStd = ["Ratul", "Mitul", "Bruno"]


def manageStudent():

    print("\t\t\t\t\t*********************************************")
    print("\t\t\t\t\t**********STUDENT MANAGEMENT SYSTEM**********")
    print("\t\t\t\t\t*********************************************")
    print("Enter 1 : To View Student's List")
    print("Enter 2 : To Add New Student")
    print("Enter 3 : To Search Student")
    print("Enter 4 : To Remove Student")

    try:
        userInput = int(input("Please Select An Option From Above: "))
    except ValueError:
        exit("Sorry! That's Not A Number")
    else:
        print("\n")

    if userInput == 1:
        print("Students List:")
        for students in listStd:
            print("- {}".format(students))

    elif userInput == 2:
        newStd = input("Enter New Student: ")
        if newStd in listStd:
            print("This Student {} Already In The Database".format(newStd))
        else:
            listStd.append(newStd)
            print("New Student {} Is Successfully Added".format(newStd))
            for students in listStd:
                print("- {}".format(students))

    elif userInput == 3:
        srcStd = input("Enter A Student Name To Search: ")
        if srcStd in listStd:
            print("Record Found Of Student {}".format(srcStd))
        else:
            print("No Record Found Of Student {}".format(srcStd))

    elif userInput == 4:
        rmStd = input("Enter A Student Name To Remove: ")
        if rmStd in listStd:
            listStd.remove(rmStd)
            print("Student {} Successfully Deleted".format(rmStd))
            for students in listStd:
                print("- {}".format(students))
        else:
            print("No Record Found Of This Student {}".format(rmStd))

    elif userInput < 1 or userInput > 4:
        print("Please Enter A Valid Option")


manageStudent()


def runAgain():
    runAgn = input("Want To Run Again y/n: ")
    if runAgn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        quit("Thanks For Using Student Management System")


runAgain()
