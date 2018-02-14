#coding=utf-8
import glob,re,os


def code_count(filename):
    blank_lines = 0
    comment_lines = 0
    with open(filename) as f:
        lines = f.readlines()
        code_lines = len(lines)
        idx = 0
        while idx < code_lines:
            line = lines[idx]
            if line == '\n':
                blank_lines += 1
            elif line.startswith('#'):
                comment_lines += 1
            elif re.match(r"\s*'''", line):
                comment_lines += 1
                while not re.match(r".*'''$", line):
                    line = lines[idx]
                    idx += 1
                    comment_lines += 1
            idx += 1
        print os.path.split(filename)[1]+':'
        print '总行数:%d' % code_lines
        print '空白行数:%d' % blank_lines
        print '注释行数:%d' % comment_lines


def dir_code_count(dir):
    for pyfile in glob.glob(dir + r'\*.py'):
        code_count(pyfile)


if __name__ == '__main__':
    dir_code_count(r'd:\gakki')