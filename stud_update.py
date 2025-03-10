#StudentUpdate.py<---File Name and Module Name
import pickle
def updatestudent():
    try:
        studrecords=list() # For adding Individual Records
        with open("StudentInfo.pick","rb") as fp:
            while(True):
                try:
                    studrec=pickle.load(fp)
                    studrecords.append(studrec)
                except EOFError:
                    break
        #Accept the Student Number for Updating Student details
        res=False
        sno = int(input("Enter Student Number to Upate Student Details:"))
        for ind in range(0,len(studrecords)):
            if(studrecords[ind][0]==sno):
                recno=ind
                res=True
                break
        if(res):
            sname=input("Enter Student Name to update:")
            marks = input("Enter Student Marks to update:")
            studrecords[recno][1]=sname
            studrecords[recno][2] = marks
            with open("StudentInfo.pick","wb") as fp:
                for studrecord in studrecords:
                    pickle.dump(studrecord,fp)
            print("Student Record Upodated--verify")

        else:
            print("{} does not exist".format(sno))
    except FileNotFoundError:
        print("File Does not Exist")


