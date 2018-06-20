from html.parser import HTMLParser
from html.entities import name2codepoint

file = 'C:/Users/KRISHNA/Classavo/OpenStax Books/astronomy-14.3/col11992_1.14_complete/m59743/index.cnxml.html'
HtmlFile = open(file, 'w', encoding='utf-8')
# source_code = HtmlFile.read()
# print(len(source_code))

for line in HtmlFile.readlines():
        if '</cnx-pi>' in line:
                pass