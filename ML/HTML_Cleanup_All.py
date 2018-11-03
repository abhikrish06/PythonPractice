import os
from bs4 import BeautifulSoup, Tag

pth = os.getcwd()
# pth = "/home/krishna/Classavo/OpenStaxBooks/OpenStaxBooks/test/"
# filenames = os.listdir(path)

for subdir, dirs, files in os.walk(pth):
    for file in files:
        if file.endswith('.html'):
            subdirectoryPath = os.path.relpath(subdir, pth)  # get the path to your subdirectory
            # print(subdirectoryPath)
            filePath = os.path.join(subdirectoryPath, file)  # get the path to your file
            # print(filePath)
            newFilePath = filePath.replace("index.cnxml", "medium-editor").lower()  # create the new name
            # print(newFilePath)
            os.rename(filePath, newFilePath)

for subdir, dirs, files in os.walk(pth):
    for file in files:
    	filepath = subdir + os.sep + file

        if filepath.endswith(".html"):
            with open(filepath) as fp:
                soup = BeautifulSoup(fp, 'html.parser')
                # print(soup)

            # Removing unwanted 'cnx-pi'tags
            h = soup.findAll('cnx-pi')
            for n in h:
                n.decompose()

            # Modifying the source of image
            for img in soup.findAll('img'):
                pth = "https://nyc3.digitaloceanspaces.com/classavotextbooks/Users/abhishek%40classavo.com/Courses/images/"
                img['src'] = str(img['src']).split('/')[-1]
                img['src'] = pth + img['src']

            # Changing the order of image caption and image
            for fig in soup.findAll('figure'):
                content = fig.contents
                # print(content)
                idx = []
                for i, item in enumerate(content):
                    if str(item).startswith('<figcaption'):
                        idx.append(i)
                    if str(item).startswith('<span'):
                        idx.append(i)
                # print(idx)
                if len(idx) >=  2:
                    content[idx[0]], content[idx[1]] = content[idx[1]], content[idx[0]]

            # Adding div for document-title
            for div_found in soup.findAll('div',{"data-type": "document-title"}):
                new_div = Tag(soup, name="div", attrs= {"class" : "head"})
                div_found.replaceWith(new_div)
                new_div.insert(0, div_found)

            # Adding 'indenter' div to entire html
            for html_found in soup.findAll('html'):
                new_div = Tag(soup, name="div", attrs= {"class" : "indenter"})
                html_found.replaceWith(new_div)
                new_div.insert(0, html_found)

            # Adding div for body
            for body_found in soup.findAll('body'):
                new_div = Tag(soup, name="div", attrs= {"class" : "body"})
                body_found.replaceWith(new_div)
                new_div.insert(0, body_found)

            p = soup.prettify('utf-8')
            # print(type(p))

            with open(filepath, 'wb') as fp:
                fp.write(p)