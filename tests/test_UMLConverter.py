# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_UMLConverter.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-29 13:16:29
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-29 14:20:16
#   @Description:        ...


from app.modules.file_module.searcher import Searcher
from app.modules.uml_module.UMLConverter import UMLConverter
from app.modules.file_module.file import File

import pytest


path = "samples/"



def readExpected(expectedFile: str) -> str:
	f = File(expectedFile)
	f.read()
	return f.getData()


def getFileNames(directory: str, ext = ".uml") -> list:
	s = Searcher()
	files = []
	l = []
	files = s.lookForFiles(directory, ext)
	for i in range(len(files)):
		files[i] = files[i].removesuffix(ext)
		l.append((files[i] + ".py", files[i] + ".uml"))

	return l


@pytest.mark.parametrize(
	"pythonFile, expectedFile",
	getFileNames(path)
)
def test_AST(pythonFile, expectedFile):
	umlConverter = UMLConverter()
	umlConverter.setLanguage("Python")
	umlConverter.setFileList([pythonFile])
	umlConverter.setOutput(expectedFile)
	umlConverter.generateUML()
	assert(umlConverter.getCode() == readExpected(expectedFile))


def test_getSetFileList():
	u = UMLConverter()
	assert(u.getFileList() == [])
	u.setFileList([1, 2, 3])
	assert(u.getFileList() == [1, 2, 3])


def test_getSetCode():
	u = UMLConverter()
	assert(u.getCode() == "")
	u.setCode("[1, 2, 3]")
	assert(u.getCode() == "[1, 2, 3]")


def test_getSetOutput():
	u = UMLConverter()
	assert(u.getOutput() == "")
	u.setOutput("f/output.txt")
	assert(u.getOutput() == "f/output.txt")


def test_getSetLanguage():
	u = UMLConverter()
	assert(u.getLanguage() == None)
	u.setLanguage("Python")
	assert(u.getLanguage() == "Python")


def test_getSetExtension():
	u = UMLConverter()
	assert(u.getExtension() == None)
	u.setExtension(".py")
	assert(u.getExtension() == ".py")


def test_getSetClassList():
	u = UMLConverter()
	assert(u.getClassList() == [])
	u.setClassList([1, 2, 3])
	assert(u.getClassList() == [1, 2, 3])


def test_getSetImports():
	u = UMLConverter()
	assert(u.getImports() == [])
	u.setImports([1, 2, 3])
	assert(u.getImports() == [1, 2, 3])