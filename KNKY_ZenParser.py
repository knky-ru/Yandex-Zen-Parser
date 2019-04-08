from bs4 import BeautifulSoup
from urllib.request import urlopen
import string
import random
import os

SEEK_ATTRIBUTES = ['p', 'h2', 'h3', 'img']

def parseTitle(soup):
    tag = soup.find(class_='article__title')
    tag = removeAttr(tag, "class")
    tag = removeAttr(tag, "itemprop")
    return tag

def parseHtml(soup):
    html_body = soup.find(class_='article__body')
    html_p_list = html_body.find_all(SEEK_ATTRIBUTES)
    return html_p_list

def makeOutputDirectory():
    directory = "output"
    try:
        os.mkdir(directory)
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)
    return directory

def makeDirectory(alias):
    directory = "output/" + alias
    try:
        os.mkdir(directory)
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)
    return directory

def id_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def removeAttr(tag, attrName):
    del tag[attrName]
    return tag

def getImageSrc(tag):
    dataSet = ""
    if tag.has_attr("data-srcset"):
        dataSet = tag['data-srcset'].split(',')[1].strip().replace(" 2x", "")
    if tag.has_attr("srcset") and dataSet == "":
        dataSet = tag['srcset'].split(',')[1].strip().replace(" 2x", "")
    return dataSet

def downloadImage(url):
    name = url.split('/')[-1]
    f = open(url, 'wb')
    f.write(urlopen(name).read())
    f.close()
    return

def downloadImageStream(url, directory, alias, i):
    try:
        imgData = urlopen(url).read()
        # name = id_generator() + ".jpg"
        name = alias.split('-')
        name.pop()
        name = '-'.join(name)
        name = name + '-' + str(i) + '.jpg'
        output = open(directory + "/" + name, 'wb')
        output.write(imgData)
        output.close()
        return name
    except:
        print("Can't download img " + url)
        pass

def processParagraph(tag):
    tag = removeAttr(tag, "class")
    return tag

def processHeaderTwo(tag):
    tag = removeAttr(tag, "class")
    return tag

def processHeaderThree(tag):
    tag = removeAttr(tag, "class")
    return tag

def processHeaderImg(tag, directory, alias, i):
    tag = removeAttr(tag, "class")
    bigImgSrc = getImageSrc(tag)
    if tag.has_attr("data-src"):
        tag = removeAttr(tag, "data-src")
    if tag.has_attr("data-srcset"):
        tag = removeAttr(tag, "data-srcset")
    if tag.has_attr("srcset"):
        tag = removeAttr(tag, "srcset")
    new_name = downloadImageStream(bigImgSrc, directory, alias, i)
    tag["src"] = [new_name]
    return tag

def generateAlias(url):
    return url.split('/')[-1]

def makeSoup(url):
    return BeautifulSoup(urlopen(url), 'html.parser')

def parseToHtml(urls_array):
    if urls_array == []:
        print("Empty array received.")
        return
    makeOutputDirectory()
    for url in urls_array:
        print("Start processing URL: " + url)
        alias = generateAlias(url)
        directory = makeDirectory(alias)
        soup = makeSoup(url)
        html_p_list = parseHtml(soup)
        f = open(directory + "/" + alias + '.html', 'w')
        f.write(parseTitle(soup).prettify())
        i = 1
        for tag in html_p_list:
            el = tag.name
            if el == "p":
                tag = processParagraph(tag)
            if el == "h2":
                tag = processHeaderTwo(tag)
            if el == "h3":
                tag = processHeaderThree(tag)
            if el == "img":
                tag = processHeaderImg(tag, directory, alias, i)
                i += 1
            f.write(tag.prettify())
        print("Done")
        f.close()
    return
