![Supported Python versions](https://img.shields.io/badge/python-2.7-blue.svg)

# script-tools
一些Python脚本工具

## CONTENT
- #### PIP_CONFIG_REWRITE

	##### Dcription: 
	when I use `pip install`,  for the poor connection, it always timeout in China.
	The script writen in python to write the configuration of pip, using mirror image 
	source in China(http://pypi.douban.com/simple) 

	##### Usage
	```
	python PIP_CONFIG_REWRITE.py
	```
	##### Online usage
	```
	curl -L https://raw.githubusercontent.com/rhyspang/script-tools/master/PIP_CONFIG_REWRITE.py | python
	```

- #### RESIZE_IMGS

	##### Description
	Resize images to specified size in directory you specified

	##### Usage
	```
	python RESIZE_IMGS.py [-h] [-d DIRECTORY] [-W WIDTH] [-H HEIGHT]

	optional arguments:
	-h, --help            show this help message and exit
	-d DIRECTORY, --directory DIRECTORY
	                    the directory, default current directory
	-W WIDTH, --width WIDTH
	                    the width you want to resize to, default 400
	-H HEIGHT, --height HEIGHT
	                    the height you want to resize to, default 250

	```
	
- #### COUNTING_CODE

	##### Description
	Counting code in specified directory

	##### Usage
	```
	python COUNTING_CODE.py [-h] [-d DIRECTORY] [-g]

	optional arguments:
	-h, --help            show this help message and exit
	-d DIRECTORY, --directory DIRECTORY
	                    the directory you specified
	-g, --graphic      	display by chart using matplotlib (if installed)
	```

- #### gbk2utf8

	##### Description
	convert file coding format from `gbk` to `utf-8`, like `enca`

	##### Usage
	```
	convert file coding format from `gbk` to `utf-8`

    optional arguments:
    -h, --help            show this help message and exit
      -d DIRECTORY, --directory DIRECTORY
                            convert all files in the directory
      -f FILENAME, --filename FILENAME
                            file to convert
      -o OUTPUT, --output OUTPUT
                        output filename or directory, is output filename when
                        `-f` argument be used, otherwise, directory name

	```
