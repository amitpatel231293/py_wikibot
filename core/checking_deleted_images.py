def listingdeleted_pagename(pagename):
     with open("listingdeleted_pagename.txt",'a') as newfile:
        newfile.write(pagename+"\n")

def readingdeleted_pagename():
    deletedpagename=[]
    with open("listingdeleted_pagename.txt",'r') as newfile:
        
        if newfile == None:
            return 'empty'
        else:
            for line in newfile:
                deletedpagename.append(line.strip())
        return deletedpagename
        


