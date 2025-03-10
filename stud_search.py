#StudentSearch.py<---File Name and Module Name
import pickle
def  searchstudent():
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
        rec1=[]
        for rec in studrecords:
            if(sno==rec[0]):
                res=True
                rec1=rec
                break
        #Display the Student Record
        if(res):
            print("\t{} Number Exist:".format(sno))
            print("\t data is={}".format(rec1))
        else:
            print("\t{} Number Does Exist:".format(sno))
    except FileNotFoundError:
        print("File Does not Exist")

