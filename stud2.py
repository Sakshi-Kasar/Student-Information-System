import pickle
studrecords=list() # For adding Individual Records
with open("stud.pick","rb") as fp:
    studrec=pickle.load(fp)
    studrecords.append(studrec)

print(studrecords)