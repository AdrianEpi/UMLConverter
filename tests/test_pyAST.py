# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-12 08:56:58
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-09 06:56:16
#   @Description:        Tests for app/ast_module/pyAST.py


from app.modules.ast_module.pyAST import PyAST
from app.modules.ast_module.pythonNode import PythonNode
from tests.utils import generateTree, readExpected, getFileNames

import pytest
import ast

path = "samples/testAST/"


@pytest.mark.parametrize(
	"pythonFile, expectedFile",
	getFileNames(path)
)
def test_AST(pythonFile, expectedFile):
	assert(generateTree(file = pythonFile, lang ='Python') == readExpected(expectedFile))

def test_setGetTree():
	ast = PyAST()
	newNode = PythonNode()
	ast.setTree(newNode)
	assert(ast.getTree() == newNode)

def test_setGetDataList():
	ast = PyAST()
	l = ["item1", "item2", "item3"]
	ast.setDataList(l)
	assert(ast.getDataList() == l)
