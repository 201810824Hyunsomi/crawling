import pytagcloud
import random
import webbrowser
from konlpy.tag import Twitter
from collections import Counter
def get_tags(text, ntags=20, multiplier=2):
    t = Twitter()
    nouns = []
    for sentence in text:
        for noun in t.nouns(sentence):
            nouns.append(noun)
            count = Counter(nouns)
    return [{'color': color(),'tag':n,'size':2*c*multiplier} for n,c in count.most_common(ntags)]
def draw_cloud(tags, filename, fontname = 'Noto Sans CJK',size1 = (1300,800)):
    pytagcloud.create_tag_image(tags,filename,fontname=fontname,size=size1)
    webbrowser.open(filename)

r = lambda: random.randint(0, 255)
color = lambda: (r(), r(), r())

okjak = []
file = open('C:/Users/KDG/Downloads/okja1.txt', 'r', encoding ='UTF-8')
lines = file.readlines()

for line in lines:
    okjak.append(line)
file.close()

tags = get_tags(okjak)
print(tags)
draw_cloud(tags,'wc1.png')



