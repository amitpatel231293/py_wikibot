import time
import texttable as tt
import os
import requests
import re
import pywikibot.family


# take out one of the comment from below
#p = PageviewsClient('Amit')
#p = PageviewsClient('Zac')

from Delete_page import *
from Access_time_detection import *
from Checking_edit_time_of_page import *
from Compare_edit_time import *
from Listing_deleted_pages import *
from Fetching_pages import *


no = 1
pages_no = 20
whole_program_run = 1
Token = False

def show_userpage(username):
    url='https://xtools.wmflabs.org/pages/en.wikipedia.org/'+username+'/0/noredirects/live?format=wikitext'
    result = requests.get(url).text
    pattern1 = re.findall('\[\[:(.*)]]',result)
    if len(pattern1)>0:
        return pattern1
    else:
        print("No page here")

#print(accessTime('Raja Chor Mantri Sipahi', '20180510', '20180515'))
print("--------------------------------------------------------------------------------------------")
print("------------------------------------- Starting WikiBot -------------------------------------")
print("--------------------------------------------------------------------------------------------")
os.system('python3 Make_database.py')
os.system('python3 pwb.py login')

# Put the whole function in loop keep asking do you want to continue to for next 50 pages and so on
while True:

    Not_edited_pages = []
    Timely_edited_pages = []
    Pages_not_viewed = []
    Pages_viewed = []
    image_links = []
    number1 = 0
    number = 0
    number2 = 0
    number3 = 0
    index=0
    total_index = []
    image_names = []
    positions = []
    start=0
    end = 0
    own_pages = []
    page_names = []
    own_all_pages = []
    Not_edited_realtime = []
    Timely_edited_realtime = []
    Pages_not_viewno = []
    Pages_viewed_viewno = []


    if whole_program_run == 1:
        username = open("login.txt", 'r')
        un = username.read()
        own_all_pages = show_userpage(un)
        print("--------------------------------- List of all Pages ----------------------------------------")
        #print(own_all_pages)
        tab1 = tt.Texttable()
        x1_p = [[]]
        intno = 0
        for i in own_all_pages:
            numbering = intno + 1
            x1_p.append([numbering, i])
            intno = intno + 1
        tab1.add_rows(x1_p)
        tab1.set_cols_align(['r', 'r'])
        tab1.header(["No", "Page name"])
        print(tab1.draw())
        print("----------------------------------------------------------------------------------------")
        print("------------------------- Choose the option from Below: ")
    else:
        print("----------------------------- Choose the option from Below -----------------------------")
    print("------------------------- 1) Run WikiBot to run edit time function on WikiPedia pages ") #Run wikibot to manage not recently edited pages
    print("------------------------- 2) Run WikiBot to run access time function on WikiPedia pages ")#Run wikibot to manage not recently accessed pages
    #if whole_program_run == 1:
    #    print("------------------------- 3) Just generate list of 1st 10 pages ")
    #else:
    #    print("------------------------- 3) Just generate list of next 10 pages ")
    print("---------------------------------- Running WikiBot ------------------------------------- ")

    # lHigh number of pages will cause more time
    choosen = 'false'
    wno = 0

    def fatch(numb,whoi):
        edj_no=0
        while edj_no < numb:
            own_pages.insert(edj_no,own_all_pages[edj_no+whoi])
            edj_no =edj_no+1

    option_choosen = input("Enter Your choice(1/2/3):")
    pagefinished = False
    noofpages = 5
    while True:

        own_pages = []
        fatch(noofpages,wno)
        wno = wno + noofpages

        if intno-(wno*2) < 0:
            noofpages = intno-wno
            print(noofpages)
            pagefinished = True


        '''
        if option_choosen == '5':
            current_page = input("Page name) :")
            wikipage = wikipedia.page(current_page)
            for indnum in range(len(wikipage.images)):
                image_links = str(wikipage.images[indnum])
                for i in find_indices_of('/', image_links):
                    positions = i
                for isec in find_indices_of('.', image_links):
                    total_index = isec
                start = int(positions)
                end = int(total_index)
                image_names.insert(index,image_links[start+1:])
                index = index+1
            print(image_names)
        '''

        if option_choosen == '3':
             choosen= 'True'
             page_names = own_pages
             print(page_names)

        if option_choosen == '1':

            Edit_time_till = input("Page edited before(Enter a date in YYYY-MM-DD) :")

            if choosen == 'false':
                page_names = own_pages

            print("---------------------------- Running the Edit time function ----------------------------")

            for index in page_names:
                #print(index)
                current_page = index
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, current_page)
                page_edit_time = editTime(page)
                #print(time_cal(page_edit_time, Edit_time_till))
                if time_cal(page_edit_time, Edit_time_till) == False:
                    Not_edited_pages.insert(number,current_page)
                    Not_edited_realtime.insert(number,page_edit_time)
                    number = number + 1
                else:
                    Timely_edited_pages.insert(number1,current_page)
                    Timely_edited_realtime.insert(number1,page_edit_time)
                    number1 = number1 + 1

            # put the actual dates for each print

            print("------------------  All Pages, those were not edited in specified time  ----------------")
            '''
            in9=0
            in8=0
            for i in Not_edited_pages:
                print(i," Edited at:",Not_edited_realtime[in9])
                in9=in9+1
            '''

            tab = tt.Texttable()

            x = [[]]  # The empty row will have the header

            in10 = 0
            for i in Not_edited_pages:
                indexing = in10 + 1
                x.append([indexing,i,Not_edited_realtime[in10]])
                in10 = in10 + 1

            tab.add_rows(x)
            tab.set_cols_align(['r', 'r', 'r'])
            tab.header(['No', 'Page names', 'Edited Time'])
            print(tab.draw())

            '''
            print("------------------  All Pages, those were edited in specified time  ------------------")
            for ind in Timely_edited_pages:
                print(ind," Edited at:",Timely_edited_realtime[in8])
                in8 = in8 + 1o
            '''

        if option_choosen == '2':

            Viewed_from = input("Enter a date to identify pages are accessed from that date or not (Enter a date in YYYYMMDD) :")
            Viewed_till = time.strftime("%Y%m%d")

            if choosen == 'false':
                page_names = own_pages
                print("--------------------------- Running the Access time function ---------------------------")

            for index in page_names:
                current_page = index
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, current_page)
                access_result = accessTime(index, Viewed_from, Viewed_till)

                if access_result == 0:
                    Pages_not_viewed.insert(number2, current_page)
                    Pages_not_viewno.insert(number2, access_result)
                    number2 = number2 + 1

                else:
                    Pages_viewed.insert(number3, current_page)
                    Pages_viewed_viewno.insert(number3, access_result)
                    number3 = number3 + 1

            '''
            inn = 0
            in7=0
            print("------------------  All Pages, those were not viewed after specified time  ------------------")
            for st in Pages_not_viewed:
                print(st,"The number of viewers in spefied time:",Pages_not_viewno[inn])
                inn = inn+1
            '''
            print("----------------  All Pages, those were not viewed after specified time  ---------------")
            tab1 = tt.Texttable()

            x1 = [[]]  # The empty row will have the header

            in11 = 0
            for i in Pages_not_viewed:
                numbering = in11 + 1
                x1.append([numbering,i,Pages_not_viewno[in11]])
                in11 = in11 + 1

            tab1.add_rows(x1)
            tab1.set_cols_align(['r', 'r', 'r'])
            tab1.header(["No","Page Names","No of viewers"])
            print(tab1.draw())

            '''
            print("------------------  All Pages, those were viewed after specified time  ------------------")
            for ink in Pages_viewed:
                print(ink,"The number of viewers in spesified time:",Pages_viewed_viewno[in7])
                in7=in7+1
            '''
        Delete_me = input("Do you want to delete any page from above list(Yes/No):")
        if Delete_me == 'Yes':
            if option_choosen == '1':
                Delete_index = input("Please select the index(1/2/3...):")
                pagename_delete = Not_edited_pages[int(Delete_index)-1]
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, pagename_delete)
                delete_in_text(pagename_delete,Not_edited_realtime[int(Delete_index)-1],'0')
                delete(page, reason=None, prompt=True, mark=False, quit=False)
            elif option_choosen == '2':
                Delete_index = input("Please select the index(1/2/3...):")
                pagename_delete = Pages_not_viewed[int(Delete_index)-1]
                site = pywikibot.Site("en", "wikipedia")
                page = pywikibot.Page(site, pagename_delete)
                delete_in_text(pagename_delete, Pages_not_viewno[int(Delete_index)-1],'0')
                delete(page, reason=None, prompt=True, mark=False, quit=False)


        if pagefinished== False:
            continuew = input("Do you want to see next 10 pages(Yes/No):")
            if continuew == 'No':
                break
            else:
                no=no+1
        elif pagefinished== True:
            if Token == False:
                continuew = input("Do you want to see left pages(Yes/No):")
                if continuew == 'No':
                    break
                else:
                    no = no + 1
                Token = True
            else:
                break


    continuew = input("Do you want to check another options or stop WikiBot(Continue/Stop):")
    if continuew == 'Stop':
        print("--------------------------------------------------------------------------------------------")
        print("-------------------------------------- Ending WikiBot --------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        break
    else:
        whole_program_run = whole_program_run + 1


## ----- Put Extra functions ----------
'''
def find_indices_of(char, in_string):
    index = -1
    while True:
        index = in_string.find(char, index + 1)
        if index == -1:
            break
        yield index
        

    Authoris = input("Do you have Administration account on Wikipedia to delete not viewed and edited pages? Ans(Yes/No):")
    if Authoris == "Yes":
        for i in Not_edited_pages:
            delete(Not_edited_pages[i], reasoßn=None, prompt=None, mark=False, quit=False)
        for i in Pages_not_viewed:
            delete(Pages_not_viewed[i], reason=None, prompt=None, mark=False, quit=False)
    elif Authoris == "No":
            Own_page_check = input("Do you want to check authorized page ? Ans(Yes/No):")

    Date_check = input("Has page been existing since above defined dates? Ans(Yes/No):")

    if Date_check == "No":
        print("------ Define all dates after your page's creation date -------")
        Edit_time_till = input("Upto when page should have edited(Enter a date in YYYY-MM-DD) :")
        Viewed_from = input("From When pages should have viewed(Enter a date in YYYY-MM-DD) :")
        Viewed_till = input("Till What time pages should have viewed(Enter a date in YYYY-MM-DD) :")
        Own_page_check = input("Yes/No")

    if Own_page_check == "Yes":
        page_name = input("what is a name of the page:")
        if option_choosen == '4':
            site = pywikibot.Site("en", "wikipedia")
            page = pywikibot.Page(site, page_name)
            # item = pywikibot.ItemPage.fromPage(page)
            time1 = editTime(page)

            if time_cal(time1, Edit_time_till) == False:
                print("start to delete the page")
                print("The page was edited on:", time1)
                delete_in_text(page_name)
                #delete(page, reason=None, prompt=True, mark=False, quit=False)
                print("Page is deleted and added in the list of deleted pages with its time in Deletedpage_list.txt")

            else:
                print('The page was edited:') # page was edited
                print(time1)
                delete_in_text(page_name)
                ##p.article_views('en.wikipedia', start=’20150801′, end=’20150831′)
    
        if option_choosen == '4':
            site = pywikibot.Site("en", "wikipedia")
            page = pywikibot.Page(site, page_name)
            access_result = accessTime(page_name, Viewed_from, Viewed_till)
            if access_result == 'None' :
                delete_in_text(page_name)
                print("start to delete the page")
                print("The page was viewed by: 0 users")
                #delete(page, reason=None, prompt=None, mark=False, quit=False)
                print("Page is deleted and added in the list of deleted pages with its time in Deletedpage_list.txt")
            else:
                delete_in_text(page_name)
                print("The page was viewed by:", access_result, "users")
                #delete(page, reason=None, prompt=None, mark=False, quit=False)
    
export PYTHONIOENCODING=xe8 
export PYTHONIOENCODING=utf8
python3 -c "import sys; print(sys.stdout.encoding)"


go through whole list and return the number of pages 2 or 10 based on limit mentioned


'''