import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import codecs
import sys
from PIL import Image
import numpy as np

alice_mask = np.array(Image.open("255fk.jpg"))

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
text_from_file_with_apath = open('test.txt', 'r', encoding='utf-8').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_mask).generate(wl_space_split)

my_wordcloud.to_file("alice.png")

plt.imshow(my_wordcloud)
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()