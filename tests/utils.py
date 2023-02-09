# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               utils.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-09 06:35:59
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-09 06:59:30
#   @Description:        ...


from app.modules.ast_module.pyAST import PyAST
from app.modules.ast_module.jsAST import JsAST
from app.modules.ast_module.line import Line
from app.modules.file_module.file import File
from app.modules.file_module.searcher import Searcher

import pytest
import ast
import esprima

def generateTree(file: str, lang: str) -> str:
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
	f = File(expectedFile)
	f.read()
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