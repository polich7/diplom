import pymorphy2
import sys
import string
frequency = {}
morph = pymorphy2.MorphAnalyzer()
with open("vacancy.txt", "r", encoding = 'utf-8') as f:
    ls = list()  # запишем весь текст разбитый на слова
    for line in f:
        lst = line.split()
        words = [] # слова из одной строки
        for word in lst:
            p = morph.parse(word)[0]  # делаем разбор
            words.append(p.normal_form)
        ls += words
ls = [word for word in ls if word.isalpha()]  # убираем знаки препинания
frequencies = {}
for word in ls:
    frequencies[word] = frequencies.get(word, 0) + 1
keys = sorted(frequencies.keys())
for word in keys:
    print(" %s, %d \n" % (word,frequencies[word]))


