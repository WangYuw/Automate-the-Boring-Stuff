#Several modules scrape web

1. **webbrowser**: Comes with Python and opens a browser to a specific page.

	- `web.open(url)`: open url on the browser

2. **Requests**(install): Downloads files and web pages from the Internet.

	- `requests.get(url)`: takes a string of a URL to download. Return a `Response`object
	
		You can tell that the request for this web page succeeded by checking the `status_code` attribute of the Response object. If it is equal to the value of `requests.codes.ok`, then everything went fine 

		If the request succeeded, the downloaded web page is stored as a string in the `Response object’s text` variable.

	- `Response object.raise_for_status()`: this will raise an exception if there was an error downloading the file and will do nothing if the download succeeded.

	- you can save the web page to a file on your hard drive with the standard `open()` function and `write()` method by passing the string `'wb'` as the second argument to `open()`

	- downloading and saving a file:

		1. Call `requests.get()` to download the file.
		`res = requests.get(url)`

		2. Call `open()` with `'wb'` to create a new file in write binary mode.
		`playFile = open('RomeoAndJuliet.txt', 'wb')`

		3. Loop over the `Response object’s iter_content()` method.
		`for chunk in res.iter_content(100000):`

		4. Call `write()` on each iteration to write the content to the file.
		`playFile.write(chunk)`

		5. Call `close()` to close the file.
		`playFile.close()`

3. **Beautiful Soup**: Parses HTML, the format that web pages are written in.

    	>>> import bs4
    	>>> exampleFile = open('example.html')
    	>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
    	>>> elems = exampleSoup.select('#author')
    	>>> type(elems)
    	<class 'list'>
    	>>> len(elems)
    	1
    	>>> type(elems[0])
    	<class 'bs4.element.Tag'>
    	>>> elems[0].getText()
    	'Al Sweigart'
    	>>> str(elems[0])
    	'<span id="author">Al Sweigart</span>'
    	>>> elems[0].attrs
    	{'id': 'author'}

	- The `get() method for Tag `objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value. 

4. **Selenium**: Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.

