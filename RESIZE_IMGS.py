#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-06 14:19:59
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-12-10 09:19:04

import Image
import imghdr
import os
import argparse

DEFAULT_SIZE = (400, 250)
DEFUALT_DIR = os.getcwd()

parser = argparse.ArgumentParser(
    description="Resize images to specified size in directory you specified")
parser.add_argument(
    "-d", "--directory", help="the directory, default current directory", default=DEFUALT_DIR)
parser.add_argument("-W", "--width", type=int,
                    help="the width you want to resize to", default=DEFAULT_SIZE[0])
parser.add_argument("-H", "--height", type=int,
                    help="the height you want to resize to", default=DEFAULT_SIZE[1])
args = parser.parse_args()

RESULT_FOLDER = r'RESIZED_TO_({}_{})_PICs'.format(args.width, args.height)


def resize_img(img_name):
    splited_img_name = os.path.splitext(img_name)

    img = Image.open(img_name)
    print 'imgname', img.filename
    if img.size == (args.width, args.height):
        return

    resized_img = img.resize((args.width, args.height), Image.ANTIALIAS)

    resized_name = splited_img_name[0]+"_resized" + splited_img_name[1]
    resized_img.save(
        RESULT_FOLDER + os.path.sep + resized_name)

    print("Resize {} ====> {}".format(
        img.filename, RESULT_FOLDER + os.path.sep + resized_name))

if not os.path.exists(args.directory):
    sys.exit("Path {} does not exists".format(args.directory))

abs_resulted_dir = os.path.join(args.directory, RESULT_FOLDER)

if not os.path.exists(abs_resulted_dir):
    os.mkdir(abs_resulted_dir)

os.chdir(args.directory)
imgs = filter(lambda it: os.path.isfile(
    it) and imghdr.what(it), os.listdir(args.directory))
for img in imgs:
    resize_img(img)
