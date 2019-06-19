from bs4 import BeautifulSoup  # BeautifulSoup is in bs4 package
import requests

URL = 'https://nolp.dhl.de/nextt-online-public/en/set_identcodes.do?idc=CC478224571DE'
content = requests.get(URL)

soup = BeautifulSoup(content.text, 'html.parser')
text = soup.find("noscript")

text = str(text)


textGroup = text.split('<div>' and '</div>')
number = textGroup[1]
number = number.split('>')
number = number[1:len(number)]


for i in range(2):
    textGroup.pop(0)


status = textGroup[0]
status = status.split('<div>')


next = textGroup[1]
next = next.split('\n')
for i in range(2):
    next.pop(0)
else:
    for i in range(4):
        next.pop()



number = " ".join(str(x) for x in number)
status = " ".join(str(x) for x in status)
next = " ".join(str(x) for x in next)


shipping_info = []
shipping_info.append(number)
shipping_info.append(status[2:len(status)])
shipping_info.append(next[10:len(next)])

print(shipping_info)
