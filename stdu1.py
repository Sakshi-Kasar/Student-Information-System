#read all
import pickle
while(True):
    with open("stud.pick", "ab") as fp:
        lst=[]
        print("enter stud info")
        sno=input("enter sno ")
        name=input("enter name")
        per=input("per")
        lst.append(sno)
        lst.append(name)
        lst.append(per)
        pickle.dump(lst,fp)
        print("you want to add another record:: yes/no")
        ch=input()
        if(ch=='no'):
            break
        break


