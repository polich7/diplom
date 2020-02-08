import pymorphy2
morph = pymorphy2.MorphAnalyzer()
k=0
with open('vacancy.txt') as f:
    ls = list() # запишем весь текст разбитый на слова
    for line in f:
        lst = line.split()
        words = [] # слова из одной строки
        for word in lst:
            p = morph.parse(word)[0]  # делаем разбор
            words.append(p.normal_form)
        ls += words
