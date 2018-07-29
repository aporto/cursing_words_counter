#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alex
#
# Created:     29/07/2018
# Copyright:   (c) alex 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import sys
import time
import unicodedata
import collections

def get_cursing_words(filename, cursing_words):
    cursings = []
    with open(filename) as f:
        plain_text = remove_accents(f.read())

    if len(plain_text) > 0:
        plain_text = plain_text.replace('\n', '')
        plain_text = plain_text.replace('\r', '')

        text_list = plain_text.split(' ')
        for word in text_list:
            if len(word) < 2:
                continue
            if word[1] == '*':
                cursings.append(word)
            else:
                if word in cursing_words:
                    cursings.append(word)

    return cursings

def remove_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")

    return str(text.upper())

if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    with open(os.path.join(path, 'data', 'cursing_dictionary.txt')) as f:
        plain_text = remove_accents(f.read())
        cursing_words = plain_text.split('\n')

    files = os.listdir(os.path.join(path, 'texts'))
    for f in files:
        filename = os.path.join(path, 'texts', f)
        cursings = get_cursing_words(filename, cursing_words)
        print len(cursings), cursings, f
