import pymorphy2
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
print(ls)

