import json
from wikipedia import *



def imagetime(imagename):
    url="https://www.mediawiki.org/w/api.php?action=query&titles=File%3A"+imagename+"&prop=imageinfo&iiprop=timestamp&format=json"
    result = json.loads(requests.get(url).text)
    try:
        image_time=result['query']['pages']['-1']['imageinfo'][0].get('timestamp')
    except:
        image_time="Missing"
    return image_time


def image_timelist(imagenamelist):
    timelist=[]
    for image in imagenamelist:
        time=imagetime(image)
        timelist.append(time)
    return timelist

