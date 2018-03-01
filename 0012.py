#coding=utf-8
#filtered_words.txt文件需要保存为UTF-8 without BOM 格式
def filter():
    with open(r'd:\gakki\filtered_words.txt') as f:
        words = []
        for line in f.readlines():
            words.append(line.strip('\n'))
    while 1:
        str = raw_input()
        for wd in words:
            if wd in str:
                tmp = ''
                for ch in wd.decode('utf-8'):
                        tmp += '*'
                str = str.replace(wd, tmp)
        print str


if __name__ == '__main__':
    filter()




