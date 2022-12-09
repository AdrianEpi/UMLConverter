# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-09 10:11:04
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-09 10:37:03
#   @Description:        Tests for app/file_module/file.py

from app.modules.file_module.file import File
import pytest

fileName = "tests/testFiles/example1.py"

f = File(fileName)

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
	assert str(exception_info.value) == 'Error, AA.txt file not found.'
