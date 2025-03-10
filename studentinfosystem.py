#StudentInformationSystem.py
from studentmenu import menu
from studen1 import addstudent
from studdisp import viewallstudents,viewsinglestudent
from stud_search import  searchstudent
from stud_update import updatestudent
from stud_del import deletestudent
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                addstudent()
            case 2:
                deletestudent()
            case 3:
                updatestudent()
            case 4:
                searchstudent()
            case 5:
                viewsinglestudent()
            case 6:
                viewallstudents()
            case 7:
                print("Thx Program Using this Project")
                break
            case _:
                print("Ur Selection of Operation is Wrong--try again")
    except ValueError:
        print("\tDon't Enter NON-Ints for Choice--try again")