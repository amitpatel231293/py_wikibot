import time

def delete_in_text(Pagename,Pageedited,pageviewed):
    ISOTIMEFORMAT='%Y-%m-%d %X'
    deletetime= time.strftime( ISOTIMEFORMAT, time.localtime())
    if pageviewed == '0':
        Pageinformation="|Page name is: "+ Pagename +"| Deletion time is:"+deletetime + "| Page last edited/viewed:" + str(Pageedited)
    if Pageedited == '0':
        Pageinformation ="|Page name is: " + Pagename + "| Deletion time is:" + deletetime + "| Page viewed:" + str(pageviewed)

    with open("ListOf_DeletedPages.txt",'a') as newfile:
        newfile.write(Pageinformation+"\n")

