from wikipedia import *
import requests


##This function is used for listing all images'name of a specific page

def show_image(pagename):
    newone = WikipediaPage(title=pagename)
    i = 0
    p1 = r"https://*/'"
    pattern = []
    result = []
    pattern1 = re.compile(r'https://upload.wikimedia.org/wikipedia/.*/.*/.*/')
    for i in range(len(newone.images)):
        matcher1 = re.search(pattern1, newone.images[i])
        size = len(matcher1.group(0))
        result.append(newone.images[i][size:])

    return result