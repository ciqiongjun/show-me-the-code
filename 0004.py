import os
import re


def word_count(filename):
    with open(filename) as f:
        s = f.read()
        lis = s.split()
        for wd in lis[::-1]:
            if not re.match(r'[a-zA-Z]+$', wd):
                lis.remove(wd)
        print len(lis)


if __name__ == '__main__':
    word_count(r'd:\gakki\1.txt')