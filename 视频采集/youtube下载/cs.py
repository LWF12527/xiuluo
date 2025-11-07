import requests
from lxml import html

html_text = requests.get('https://www.youtube.com/@channel_AIGIRL/videos').text
print(html_text)
tree = html.fromstring(html_text)
list_link = tree.xpath('//a[@id="thumbnail"]')
print(list_link)
for i in  list_link:
    print(i)