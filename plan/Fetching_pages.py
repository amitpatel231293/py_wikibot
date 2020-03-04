
import wikipedia

def gethering_pages(no,pages_no):

    if no == 1:
        print("Fatching 1st 20 pages.")
    else:
        print("Fatching next 20 pages.")

    page_names = [wikipedia.random(1) for i in range(pages_no)]
    pages = page_names
    return pages
