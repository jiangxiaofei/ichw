#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    # your code goes here
    for w in lines:
        if w.isalpha()==False :
            lines=lines.replace(w," ")
        
    s=lines.split()
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    for i,a in t[0:topn]:
        print(a.ljust(30),i)
        
    pass


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
