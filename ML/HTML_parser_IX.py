from html.parser import HTMLParser
from html.entities import name2codepoint


file = '/home/krishna/Classavo/OpenStaxBooks/col11992_1.14_complete/m59743/index.cnxml.html'
HtmlFile = open(file, 'w', encoding='utf-8')
# source_code = HtmlFile.read()
# print(len(source_code))

for line in HtmlFile.readlines():
    if 'src="' in line:
        start = line.index('src="')+4

        # substr = line[]