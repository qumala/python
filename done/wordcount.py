#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# © 2016 Lev Maximov

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Задание wordcount

Функция main() уже реализована и не требует изменения. Она вызывает 
функции print_words() и print_top(), которые необходимо написать вам. 

1. Для запуска с флагом --count реализуйте функцию print_words(filename),
которая подсчитывала бы, как часто слово встречается в тексте, и выводила бы
на экран результат в таком виде:
word1 count1
word2 count2
...

Список этот должен быть отсортирован по словам в лексикографическом порядке 
(как в словаре). Пунктуация должна быть удалена (если вы не знаете регулярных 
выражений, пунктуацию можно оставить), различия между заглавными и 
строчными делать не надо (то есть «Однако» и «однако» считаются одним и тем 
же словом), слова длиной менее 4 символов нужно игнорировать.

2. Для флага --top реализуйте функцию print_top(filename), которая
делала бы практически то же, что и print_words(filename), но выводила бы только
20 самых часто употребляемых в тексте слов, отсортированных в порядке 
убывания частотности, так что слово, которое чаще всего встречается в тексте, 
шло бы первым, следующее по частоте - вторым и т.д. Слова с одинаковой частотностью
должны быть отсортированы по алфавиту.

Для обеспечения переиспользования кода (так проще отлаживать, поддерживать), 
выделите часть функций, общую для двух вариантов вызова скрипта, в отдельную функцию.

Не пишите всю программу сразу. Разбейте задачу на подзадачи и отлаживайте каждую
по отдельности (выводите промежуточный результат на экран; когда вы добились того,
что он соответствует вашим ожиданиям, переходите к следующей подзадаче).

"""

import sys
from pathlib import Path
from operator import itemgetter
import collections
# +++your code here+++
# Объявите функции print_words(filename), print_top(filename),
# а также вспомогательную функцию, использующуюся в обеих из них,
# которая принимала бы на вход имя файла и возвращала бы dict.


def print_words(filename):
    di = get_dict_from_file(filename)
    for word in sorted(di):
        print(word+"\t"+str(di[word]))


def print_top(filename):
    di=get_dict_from_file(filename)
    sorted_dict=collections.OrderedDict(sorted(di.items(),key=lambda t:-t[1]))
    n=0;
    for i in sorted_dict:
        if sorted_dict[i]>1 and n<20:
            print(str(i)+"\t"+str(sorted_dict[i]))
            n+=1
        else:
            break


def get_text_from_file(filenamestr):
    filename=Path(filenamestr)
    Text=''
    if not(filename.exists() and filename.is_file()):
        print('unknown or nonexistent file:"' + filenamestr + '\"')
    else:
        #print('existent file:"' + filenamestr + '\"')
        F=filename.open('r')
        Text=F.read()
    return Text


def get_dict_from_file(filenamestr):
    text = get_text_from_file(filenamestr)
    di = {}
    part_of_word=""
    for i in text:
        if i in [' ','\n','\'','!','?',',','.','\t',':',';','-','`','(',')','{','}','[',']','"',"'"]:
            if len(part_of_word)>=4:
                word=part_of_word.lower()
                #print(word)
                if di.get(word)is None:
                    di[word]=1
                else:
                    di[word]+=1
            part_of_word=""
        else:
            part_of_word+=i
    return di


####


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --top} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
