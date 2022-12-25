# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               UMLConverter.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-20 09:51:11
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-25 11:14:02
#   @Description:        ...

from app.modules.uml_module.translator import Translator, LANGUAGES
from app.modules.file_module.file import File
from app.modules.file_module.searcher import Searcher
from app.modules.ast_module.line import Line
from app.modules.ast_module.pyAST import PyAST
from app.modules.interface_module.interface import Interface

import ast
import sys
from six.moves import input as raw_input
from os import system


class UMLConverter:

	fileList: list
	code: str
	output: str
	language: str
	extension: str
	classList: list

	def __init__(self):
		self.fileList = []
		self.code = ""
		self.output = ""
		self.language = None
		self.extension = None
		self.classList = []


	def getFileList(self) -> list:
		return self.fileList


	def getCode(self) -> str:
		return self.code


	def getOutput(self) -> str:
		return self.output


	def getLanguage(self) -> str:
		return self.language


	def getExtension(self) -> str:
		return self.extension


	def getClassList(self) -> list:
		return self.classList


	def setFileList(self, newFileList: list):
		self.fileList = newFileList


	def setCode(self, newCode: str):
		self.code = newCode


	def setOutput(self, newOutput: str):
		self.output = newOutput	


	def setLanguage(self, newLanguage: str) -> bool:
		if newLanguage in LANGUAGES:
			self.language = newLanguage	
			return True
		return False


	def __generateExtention(self):
		if self.language == "Python":
			self.extension = ".py"
		# elif ...
		else:
			raise Exception("Error in UMLConverter:generateExtention(), not valid language")


	def __askFiles(self):
		gui = Interface()
		result = gui.porjectInformationInterface() # [language, projectPath, outputPath]
		self.language = result[0]
		self.__generateExtention()
		self.output = result[2]
		searcher = Searcher()
		self.fileList = searcher.lookForFiles(result[1], self.extension)
		if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
			self.output += "\\"
		else:	# Linux or MacOS
			self.output += "/"
		self.output += "projectUML.txt"


	def generateUML(self):
		self.__askFiles()
		for i in self.fileList:
			f = File(i)
			f.read()
			fileAST = ast.dump(ast.parse(f.getData()), annotate_fields=True, include_attributes=False, indent=4)
			l = fileAST.split("\n")
			lines = []
			for j in l:
				lines.append(Line(j))
			tree = PyAST()
			tree.generateTree(lines)

			t = Translator(tree.getTree(), self.language)
			t.translate()
			self.code +=t.getCode()

		self.__writeToFile()
		self.__convertToPng()


	def __writeToFile(self):
		f = File(self.output)
		f.write(self.code)


	def __convertToPng(self):
		system("python -m plantuml " + self.output)



