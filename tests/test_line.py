# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_line.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-08 13:10:12
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-09 08:55:04
#   @Description:        Tests for app/ast_module/line.py

from app.modules.ast_module.line import Line

testString = "    This is an example test"
testString2 = "        This is another example test"
line = Line(testString)
line2 = Line(testString2)

def test_getIndentation():
	assert(line.getIndentation() == 4)
	assert(line2.getIndentation() == 8)

def test_getData():
	assert(line.getData() == "This is an example test")
	assert(line2.getData() == "This is another example test")

def test_getRawData():
	assert(line.getRawData() == "    This is an example test")
	assert(line2.getRawData() == "        This is another example test")

def test_getIndentationLevel():
	assert(line.getIndentationLevel() == 1)
	assert(line2.getIndentationLevel() == 2)