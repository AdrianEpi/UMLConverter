# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-09 10:11:04
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-09 08:48:33
#   @Description:        Tests for app/file_module/file.py

from app.modules.file_module.file import File
import pytest
import os
import sys

fileName = ""

if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
	fileName = "tests\\testFiles\\example1.py"
else:	# Linux or MacOS
	fileName = "tests/testFiles/example1.py"

f = File(fileName)
f.read()

def test_getSetFileName():
	assert(f.getFileName() == fileName)
	f.setFileName("NewFileName")
	assert(f.getFileName() == "NewFileName")


def test_getSetData():
	data = "class Student:\n\tdef say_hello(self, firstName: str, lastName: str):\n\t\tpass"
	assert(f.getData() == data)
	f.setData("NewData")
	assert(f.getData() == "NewData")


def test_readFileNotFoundError():
	with pytest.raises(FileNotFoundError) as exception_info:
		f = File("AA.txt")
		f.read()
	assert str(exception_info.value) == 'Error, AA.txt file not found.'


def test_readAndAnalyze():
	f = File('tests/testFiles/example1.py')
	f.readAndAnalyze(language = 'Python')
	d = {
		'codeLines': 2,
		'commentLines': 0,
		'nLines': 3
	}
	assert(f.getLinesInfo() == d)
	str

def test_write():
	fName = ""
	if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
		fName = "tests\\testFiles2\\example2.txt"
	else:	# Linux or MacOS
		fName = "tests/testFiles2/example2.txt"
	
	data = "la la la"
	file = File(fName)
	file.write(data)
	assert(file.getData() == data)
	os.remove(fName)
	os.rmdir("tests/testFiles2/")
