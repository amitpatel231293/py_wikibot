import requests
import re

## This function is used for showing all pages of a specific user

def show_userpage(username):
    url='https://xtools.wmflabs.org/pages/en.wikipedia.org/'+username+'/0/noredirects/live?format=wikitext'
    result = requests.get(url).text
    pattern1 = re.findall('\[\[:(.*)]]',result)
    if len(pattern1)>0:
        return pattern1
    else:
        print("No page here")