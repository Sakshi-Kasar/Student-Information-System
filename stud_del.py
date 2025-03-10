import pickle
def deletestudent():
    try:
        studrecords=list() 
        with open("StudentInfo.pick","rb") as fp:
            while(True):
                try:
                    studrec=pickle.load(fp)
                    studrecords.append(studrec)
                except EOFError:
                    break
        #Accept the Student Number for Deleting Student details
        res=False
        sno = int(input("Enter Student Number to Delete Student Details:"))
        for ind in range(0,len(studrecords)):
            if(studrecords[ind][0]==sno):
                recno=ind
                res=True
                break
        if(res):
            studrecords.pop(recno)
            with open("StudentInfo.pick","wb") as fp:
                for studrecord in studrecords:
                    pickle.dump(studrecord,fp)
            print("Student Record Deleted--verify")
        else:
            print("{} does not exist".format(sno))
    except FileNotFoundError:
        print("File Does not Exist")