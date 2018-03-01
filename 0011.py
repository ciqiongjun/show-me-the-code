#coding=utf-8
#filtered_words.txt文件需要保存为UTF-8 without BOM 格式
def filter():
    with open(r'd:\gakki\filtered_words.txt') as f:
        words = []
        for line in f.readlines():
            words.append(line.strip('\n'))
    while 1:
        str = raw_input()
        if str in words:
            print 'Freedom'
        else:
            print 'Human Right'


if __name__ == '__main__':
    filter()



