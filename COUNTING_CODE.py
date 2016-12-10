#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-12-10 09:54:24
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-12-10 12:50:41

import os
import argparse
import sys
import re

parser = argparse.ArgumentParser(
    description="Counting code in specified directory.")
parser.add_argument(
    "-d", "--directory", help="the directory you specified", default=os.getcwd())
parser.add_argument(
    "-g", '--graphic', help="display by chart using matplotlib (if installed)", action="store_true", default=False)
args = parser.parse_args()

sys.setrecursionlimit(10000)

CODE_FILE_SUFFIXES = ['.c', '.cpp', '.py', '.java', '.js', '.html', '.css']
detail = {}
for i in CODE_FILE_SUFFIXES:
    detail[i] = [0, 0]


def counting_code_in_file(filename):

    file_sufix = os.path.splitext(filename)[1].lower()
    if file_sufix not in CODE_FILE_SUFFIXES:
        return
    with open(filename, 'r') as f:
        for line in f:
            if re.search(r'\S', line):
                detail[file_sufix][0] += 1
            else:
                detail[file_sufix][1] += 1


def counting_code():
    for f in os.listdir('.'):
        if os.path.isdir(f) and f != 'mydir':
            os.chdir(f)

            counting_code()
            os.chdir('..')
        else:
            counting_code_in_file(f)


def paint_chart():
    fig, ax = plt.subplots()
    index = np.arange(len(CODE_FILE_SUFFIXES))
    bar_width = .35
    opacity = .4
    error_config = {'ecolor': '0.3'}

    code_line = []
    blank_line = []
    for i in CODE_FILE_SUFFIXES:
        code_line.append(detail[i][0])
        blank_line.append(detail[i][1])
    code_rect = plt.bar(index, code_line, bar_width,
                        alpha=opacity,
                        color='b',

                        error_kw=error_config,
                        label='Codelines')

    blank_rect = plt.bar(index + bar_width, blank_line, bar_width,
                         alpha=opacity,
                         color='r',

                         error_kw=error_config,
                         label='Blanklines')

    plt.xlabel('Language')
    plt.ylabel('Line')
    plt.title('COUNTING_CODE')
    plt.xticks(
        index + bar_width, tuple(map(lambda s: s[1:], CODE_FILE_SUFFIXES)))
    plt.legend()

    plt.tight_layout()
    plt.show()


os.chdir(args.directory)
counting_code()
if args.graphic:
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError:
        print "numpy or matplotlib may not be installed! cannot use -g argument"
        sys.exists()
    paint_chart()
else:
    print detail
