# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-12 08:56:58
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-13 12:39:52
#   @Description:        Tests for app/ast_module/pyAST.py


from app.modules.ast_module.pyAST import PyAST
from app.modules.ast_module.line import Line
from app.modules.file_module.file import File
from app.modules.file_module.searcher import Searcher

import pytest
import ast

path = "samples/testAST/"


def generateTree(pythonFile: str) -> str:
	f = File(pythonFile)	
	data = f.getData()
	myAst = ast.dump(ast.parse(data), annotate_fields=True, include_attributes=False, indent=4)	
	rawAST = myAst.split("\n")
	lines = []
	for i in rawAST:
		lines.append(Line(i))

	tree = PyAST()
	tree.generateTree(lines)
	return tree.getTree().toString()


def readExpected(expectedFile: str) -> str:
	f = File(expectedFile)
	return f.getData()


def getFileNames(directory: str, ext = ".py") -> list:
	s = Searcher()
	files = []
	l = []
	files = s.lookForFiles(directory, ext)
	for i in range(len(files)):
		files[i] = files[i].removesuffix(ext)
		l.append((files[i] + ext, files[i] + ".txt"))

	return l


@pytest.mark.parametrize(
	"pythonFile, expectedFile",
	getFileNames(path)
)
def test_AST(pythonFile, expectedFile):
	assert(generateTree(pythonFile) == readExpected(expectedFile))


# @pytest.mark.parametrize(
# 	"pythonFile, expectedFile",
# 	getFileNames(path + "Import")
# )
# def test_import(pythonFile, expectedFile):
# 	assert(generateTree(pythonFile) == readExpected(expectedFile))


# @pytest.mark.parametrize(
# 	"pythonFile, expectedFile",
# 	getFileNames(path + "ImportFrom")
# )
# def test_importFrom(pythonFile, expectedFile):
# 	assert(generateTree(pythonFile) == readExpected(expectedFile))


# @pytest.mark.parametrize(
# 	"pythonFile, expectedFile",
# 	getFileNames(path + "AnnAssign")
# )
# def test_annAssign(pythonFile, expectedFile):
# 	assert(generateTree(pythonFile) == readExpected(expectedFile))


# @pytest.mark.parametrize(
# 	"pythonFile, expectedFile",
# 	getFileNames(path + "Assign")
# )
# def test_assign(pythonFile, expectedFile):
# 	assert(generateTree(pythonFile) == readExpected(expectedFile))


