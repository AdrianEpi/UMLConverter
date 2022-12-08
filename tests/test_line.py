# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_line.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-08 13:10:12
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-08 13:42:48
#   @Description:        Tests for app/ast_module/line.py

from app.modules.ast_module.line import Line

testString = "    This is an example test"
line = Line(testString)

def test_getIndentation():
	assert(line.getIndentation() == 4)