# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_jsAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-09 06:34:37
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:25:19
#   @Description:        Tests for app/ast_module/jsAST.py

from app.modules.ast_module.jsAST import JsAST
from tests.utils import generateTree, readExpected, getFileNames
from app.modules.ast_module.pythonNode import PythonNode

import pytest

path = 'samples/JavaScript_Samples/'


@pytest.mark.parametrize(
	'file, expectedFile',
	getFileNames(directory = path, ext = '.js')
)
def test_AST(file, expectedFile):
	assert(generateTree(file = file, lang = 'JavaScript') == readExpected(expectedFile))


def test_setGetTree():
	ast = JsAST()
	newNode = PythonNode()
	ast.setTree(newNode)
	assert(ast.getTree() == newNode)


def test_setGetDataList():
	ast = JsAST()
	l = ['item1', 'item2', 'item3']
	ast.setDataList(l)
	assert(ast.getDataList() == l)
