# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               utils.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-09 06:35:59
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:26:39
#   @Description:        This file describes funtion used in different tests


from app.modules.ast_module.pyAST import PyAST
from app.modules.ast_module.jsAST import JsAST
from app.modules.ast_module.line import Line
from app.modules.file_module.file import File
from app.modules.file_module.searcher import Searcher

import pytest
import ast
import esprima

def generateTree(file: str, lang: str) -> str:
	"""
	Generates the tree

	:param      file:  The file
	:type       file:  str
	:param      lang:  The language
	:type       lang:  str

	:returns:   String representation of the tree
	:rtype:     str
	"""
	f = File(file)	
	f.read()
	data = f.getData()
	tree = None
	if lang == 'Python':
		myAst = ast.dump(ast.parse(data), annotate_fields=True, include_attributes=False, indent=4)	
		rawAST = myAst.split("\n")
		lines = []
		for i in rawAST:
			lines.append(Line(i))

		tree = PyAST()
		tree.generateTree(lines)

	elif lang == 'JavaScript':
		tree = JsAST()
		fileAST = esprima.parseScript(f.getData())
		tree.generateTree(fileAST.body)

	
	return tree.getTree().toString()


def readExpected(expectedFile: str) -> str:
	"""
	Reads an expected.

	:param      expectedFile:  The expected file
	:type       expectedFile:  str

	:returns:   Data from the readed file
	:rtype:     str
	"""
	f = File(expectedFile)
	f.read()
	return f.getData()


def getFileNames(directory: str, ext = ".py") -> list:
	"""
	Gets the file names.

	:param      directory:  The directory
	:type       directory:  str
	:param      ext:        The extent
	:type       ext:        str

	:returns:   The file names.
	:rtype:     list
	"""
	s = Searcher()
	files = []
	l = []
	files = s.lookForFiles(directory, ext)
	for i in range(len(files)):
		files[i] = files[i].removesuffix(ext)
		l.append((files[i] + ext, files[i] + ".txt"))

	return l