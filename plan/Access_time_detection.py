from mwviews.api import PageviewsClient

###Provides the access time  for a wikipedia pages in between a specific time(with starting and endoing date specified), it gives a nomber of views###
p=PageviewsClient('Amit')
'''
def accessTime(page_name, s_time, e_time):
    test = False
    for daily in p.article_views('en.wikipedia', [page_name], granularity='daily', start=s_time, end=e_time).items():
        if daily[1].get(page_name) != 0:
            no_of_views = daily[1].get(page_name)
            return str(no_of_views)
    return "0"
'''

def accessTime(page_name, s_time, e_time):
    no_of_views = 0
    for daily in p.article_views('en.wikipedia', [page_name], granularity='daily', start=s_time, end=e_time).items():
        if daily[1].get(page_name) != None:
            no_of_views = no_of_views + daily[1].get(page_name)
        else:
            pass
        return no_of_views
