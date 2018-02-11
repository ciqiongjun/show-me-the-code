import glob,re,os
from collections import OrderedDict


def get_word(dir):
    if os.path.exists(dir+r'\output.txt'):
        os.remove(dir+r'\output.txt')
    f1 = open(dir+r'\output', 'w')
    for article in glob.glob(dir+r'\*.txt'):
        drop = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an', 'at', 'he', 'she']
        with open(article) as f2:
            str = f2.read()
            lis = str.split()
            wdict = {}
            for wd in lis[:]:
                if re.match(r'[a-zA-Z]+$', wd) and wd not in drop:
                    if wd in wdict:
                        wdict[wd] += 1
                    else:
                        wdict[wd] = 1
            sort = sorted(wdict.items(), key=lambda item: item[1], reverse=True)
            f1.write(os.path.split(article)[1] + ' : ' + sort[0][0] + '\n')
    f1.close()
    os.rename(dir+r'\output', dir+r'\output.txt')


if __name__ == '__main__':
    get_word(r'd:\gakki')










