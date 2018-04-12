import re
import requests
import random
import string
import time

def start():
    dataPath = r'E:\PITT\2018Spring\Algorithm\Project\books2.txt'
    outpath = r'E:\PITT\2018Spring\Algorithm\Project\booksout.txt'
    out = open(outpath, 'w')

    with open(dataPath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            l = line.split("\t")
            isbn = l[4]
            genre = getGenre(isbn)
            outs = isbn+'\t'+genre+'\n'
            print(outs)
            out.write(outs)
    out.close()

def getGenre(ISBN):
    urlpre = r'https://www.alibris.com/booksearch?keyword='
    pattern = re.compile(r'red\/home.gif.+?<li>.+?<li>\s+?<a.+?>(.+?)<\/a>')
    psub1 = re.compile(r'red.+">')
    psub2 = re.compile(r'</a>')
    highvolpattern = re.compile(r'due to the high volume of visitors')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'From': ''  # This is another valid field
    }

    headersfrom = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    headers['From'] = headersfrom + "@alibris.com"
    url = urlpre + ISBN + r'&mtype=B'
    html = requests.get(url, headers=headers)
    text = html.text

    match = pattern.search(text)
    if match:
        m = match.group()
        m = psub1.sub('', m)
        m = psub2.sub('', m)
        return m
    else:
        highvol = highvolpattern.search(text)
        if highvol:
            print('wait 1 second\n')
            time.sleep(1)
            getGenre(ISBN)
        else:
            return 'NA'


if __name__ == "__main__":
    start()
    #print(getGenre('9780140283330'))


