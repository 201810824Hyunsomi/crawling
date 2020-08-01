from collections import Counter
file = open('C:/Users/KDG/Downloads/okja1.txt','r',encoding='utf-8')
lines = file.readlines()
okja = []
for line in lines:
    okja.append(line)
file.close()
from konlpy.tag import Twitter
twitter = Twitter()
sentences_tag = []
for sentence in okja:
    morph = twitter.pos(sentence)
    sentences_tag.append(morph)
    print(morph)
    print('-'*30)
print(sentences_tag)
print(len(sentences_tag))
print('\n'*3)
noun_adj_list = []
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun','Adjective']:
            noun_adj_list.append(word)
counts = Counter(noun_adj_list)
print(counts.most_common(10))


