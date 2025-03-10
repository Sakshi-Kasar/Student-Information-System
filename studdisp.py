#StudentSelect.py<---File and Module Name
import pickle
def viewsinglestudent():
    try:
        studrecords=list() # For adding Individual Records
        with open("StudentInfo.pick","rb") as fp:
            while(True):
                try:
                    studrec=pickle.load(fp)
                    studrecords.append(studrec)
                except EOFError:
                    break
        #Accept the Student Number for Viewing Student details
        res=False
        sno = int(input("Enter Student Number to view Student Details:"))
        for rec in studrecords:
            if(sno==rec[0]):
                res=True
                stdrec=rec
                break
        #Display the Student Record
        if(res):
            print("-" * 50)
            print("\tStudent Number:{}".format(stdrec[0]))
            print("\tStudent Name:{}".format(stdrec[1]))
            print("\tStudent Marks:{}".format(stdrec[2]))
            print("-"*50)
        else:
            print("\t{} Number Does Exist:".format(sno))
    except FileNotFoundError:
        print("File Does not Exist")

def viewallstudents():
    try:
        with open("StudentInfo.pick","rb") as fp:
            print("-"*50)
            print("\tSTNO\t\tNAME\tMARKS")
            print("-" * 50)
            while(True):
                try:
                    stdrecord = pickle.load(fp)
                    for val in stdrecord:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-" * 50)
                    break
    except FileNotFoundError:
        print("File Does not Exist")

