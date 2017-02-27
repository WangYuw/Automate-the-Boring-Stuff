#! python3
# SearchGoogle.py: open several Google search results

'''
    This is what your program does:
        Gets search keywords from the command line arguments.
        Retrieves the search results page.
        Opens a browser tab for each result.

    This means your code will need to do the following:
        Read the command line arguments from sys.argv.
        Fetch the search result page with the requests module.
        Find the links to each search result.
        Call the webbrowser.open() function to open the web browser.
'''

import sys, requests, webbrowser, bs4

# 1. Get the command line arguments and request the search page
#  the result page has a URL like https://www.google.com/search?q=SEARCH_TERM_HERE
print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 2. Find all resultats
# you must inspect the search result page with the browser’s developer tools to 
# try to find a selector that will pick out only the links you want.
soup = bs4.BeautifulSoup(res.text)
# find all <a> elements that are within an element that has the r CSS class.
linkElems = soup.select('.r a')

# Open web browsers for each result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

'''
    Automatically opens several links at once:
        Open all the product pages after searching a shopping site such as Amazon
        Open all the links to reviews for a single product    
'''