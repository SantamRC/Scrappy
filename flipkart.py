from bs4 import BeautifulSoup
import requests,cgi,cgitb

cgitb.enable(display=0)
form=cgi.FieldStorage()
url=form.getvalue("url")
page=requests.get(url)


