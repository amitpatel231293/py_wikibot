import time

def deletenotusedImages_in_text(Imagename,Imageuploaded):
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    deletetime = time.strftime(ISOTIMEFORMAT, time.localtime())
    Pageinformation = "|Image name is: " + Imagename + "| Deletion time:" + deletetime + "| Images Upload time:" + Imageuploaded

    with open("ListOf_DeletedImages_notused.txt",'a') as newfile:
        newfile.write(Pageinformation+"\n")

