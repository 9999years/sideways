import argparse
# table col
from os import environ
# output
import textwrap
# stdin
import sys

from block_map import block_map

def rotate(txt, reverse=True):
    ret = []
    lines = txt.splitlines()
    maxlen = len(max(lines, key=lambda line: len(line)))
    if reverse:
        colrange = range(maxlen - 1, -1, -1)
    else:
        colrange = range(maxlen)

    for col in colrange:
        for row in range(len(lines)):
            if len(lines[row]) > col:
                c = lines[row][col]
                if c in block_map:
                    ret.append(block_map[c])
                else:
                    ret.append(c)
            else:
                ret.append(' ')
        ret.append('\n')
    return ''.join(ret)

def main():
    prog = 'sideways'
    global cols

    argparser = argparse.ArgumentParser(
        description='Sideways texter',
        prog=prog,
        )

    argparser.add_argument('src_file', nargs='*',
        help='The filename of a file to rotate.')

    argparser.add_argument('-e', '--encoding', type=str, default='utf-8',
        help='The encoding to use')

    args = argparser.parse_args()

    if len(args.src_file) == 0:
        # use stdin
        # catenate stdinput, parse / render
        src = ''
        src = sys.stdin.buffer.read().decode(args.encoding)
        print(rotate(src))
        exit()

    # process each file, respecting encoding, although i really hope nobody
    # ever uses that argument and to be quite frank i haven't tested it

    # path manipulation
    from os import path
    for fname in args.src_file:
        with open(fname, 'r', encoding=args.encoding) as f:
            print(rotate(f.read()))

if __name__ == '__main__': main()
