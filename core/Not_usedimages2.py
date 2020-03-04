import requests
import re
import json

'''
This two functions are used for outputing the images uploaded by a specific user but not been used on any page
'''
def User_Allimages(Username):
    Alluploadedimages=[]
    ## is this username existing?
    #url='https://commons.wikimedia.org/w/api.php?action=query&list=allimages&aiuser='+Username+'&aisort=timestamp&format=json'
    url ='https://commons.wikimedia.org/w/api.php?action=query&list=usercontribs&ucuser='+Username+'&uclimit=50&ucdir=newer&format=json'
    result = json.loads(requests.get(url).text)
    Image=result['query']['usercontribs']
    for i in range(len(Image)):
        Alluploadedimages.append(Image[i].get('title'))
    return Alluploadedimages

def Not_usedimages(images1):
    Notusedimages=[]
    for imagename in images1:
        url='https://en.wikipedia.org/w/api.php?action=query&prop=fileusage&titles=File%3A'+imagename+'&format=json'
        result=json.loads(requests.get(url).text)    
        if result['query']['pages']['-1'].get('fileusage')==None:
            Notusedimages.append(imagename)
        else:
            pass
    return Notusedimages