__author__ = 'nvishwakarma'

from collections import deque
FILENAME =r'C:\PersonalProjects\PythonSnippets\Files\Example.txt'


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open(FILENAME) as f:
        for line, previousLn in search(f, '=', 3):
            for pline in previousLn:
                print(pline, end='')
            print(line, end='')
            print('-'*len(line))
            '''this is test'''
