# coding: utf8
# Copyright (c) 2017 rhspang.
# Author: Rhy Pang (rhyspang@qq.com)

import argparse
import codecs
import os


parser = argparse.ArgumentParser(
    description="convert file coding format from `gbk` to `utf-8`"
)
parser.add_argument(
    "-d", "--directory", help="convert all files in the directory"
)
parser.add_argument(
    "-f", "--filename", help="file to convert"
)
parser.add_argument(
    '-o', "--output", help="output filename or directory, "
                           "is output filename when `-f` argument be used, "
                           "otherwise, directory name",
)
args = parser.parse_args()


def convert_file(filename, output_filename):
    with codecs.open(filename, 'r', 'gbk') as fr,\
            codecs.open(output_filename, 'w', 'utf8') as fw:
        fw.write(fr.read())


def main():
    if args.filename:
        convert_file(args.filename, args.output)
    else:
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        for filename in os.listdir(args.directory):
            convert_file(
                os.path.join(args.directory, filename),
                os.path.join(args.output, filename)
            )


if __name__ == '__main__':
    main()
