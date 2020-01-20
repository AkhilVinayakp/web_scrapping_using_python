import requests
from bs4  import BeautifulSoup
html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""
url = "https://www.flipkart.com/search?q=rog+phone+2&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_na&as-pos=0&as-type=RECENT&suggestionId=rog+phone+2|Mobiles&requestId=63fb7211-d586-4320-a000-52cf7a6464bd&as-backfill=on"
web=requests.get(url).text
page=BeautifulSoup(web,'lxml',from_encoding='UTF-8')
print(page.prettify())
