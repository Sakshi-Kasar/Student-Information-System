#StudentAdd.py<---File Name and Module Name
import pickle

#Development of Programmer-Defined Exceptions
class ZeroLengthError(Exception):pass
class SpaceError(Exception):pass
class InvalidNameError(Exception):pass
#Hitting the Programmer -Defined Exceptions
def validation(name):
    if(name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        if(len(words)==0):
            raise ZeroLengthError
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(not res):
                raise InvalidNameError
            else:
                return name

def isduplicates(lst):
    studentrecs=[]
    with open("studentinfo.pick","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                studentrecs.append(record)
            except EOFError:
                break
    #studentrecs=[[1500, 'TR', 23.67], [1400, 'DR', 67.89], [1600, 'SS', 22.12],
    dup=False
    for i in range(len(studentrecs)):
        if(studentrecs[i][0]==lst[0]):
            dup=True
            break
    return dup

#Define the Function for adding the Student Data to the File
def addstudent():
        with open("StudentInfo.pick", "ab") as fp:
            while (True):
                try:
                    # Accept the Emp Values fom KBD
                    print("-" * 50)
                    sno = int(input("Enter Student Number:"))
                    sname = validation(input("Enter Student Name: "))
                    marks = float(input("Enter Student Marks:"))
                    print("-" * 50)
                    lst = []
                    lst.append(sno)
                    lst.append(sname)
                    lst.append(marks)
                    # save lst data to the File
                    if(not isduplicates(lst)):
                        pickle.dump(lst, fp)
                        print("\tStudent Record Saved into the File")
                    else:
                        print("Record already exist-try with New Number:")
                    print("-" * 50)
                    ch = input("Do u want to Insert Another Student Record(yes/no):")
                    if (ch.lower() == "no"):
                        break
                except ValueError:
                    print("Don't Enter Alnums,strs and Symbols for Empno and Salary")
                except ZeroLengthError:
                    print("\t U Must enter Ur Name-try again")
                except SpaceError:
                    print("\tDon't Enter Space to UR  Name-try again")
                except InvalidNameError:
                    print("\tUr Name is Invalid-try again ")

