import re
import requests

def getGenre():
    dataPath = r'E:\PITT\2018Spring\Algorithm\Project\books2.txt'
    outpath = r'E:\PITT\2018Spring\Algorithm\Project\booksout.txt'
    out = open(outpath, 'w')
    out.write('Hello, world!')
    webpath = r'https://www.alibris.com/booksearch?keyword='
    pattern = re.compile(r'red\/home.gif.+?<li>.+?<li>\s+?<a.+?>(.+?)<\/a>')
    psub1 = re.compile(r'red.+">')
    psub2 = re.compile(r'</a>')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }

    with open(dataPath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            l = line.split("\t")
            isbn = l[4]
            print("ISBN: "+isbn)
            p = webpath+isbn+r'&mtype=B'
            h = requests.get(p,headers=headers)
            t = h.text

            match = pattern.search(t)
            if match:
                match = match.group()
                m = psub1.sub('',match)
                m = psub2.sub('',m)

                outs = isbn+'\t'+m
                print(outs)
                out.write(outs)
            else:
                outs = isbn + '\t' + "ERROR"
                print(outs)
                out.write(outs)

    out.close()

if __name__ == "__main__":
    getGenre()
