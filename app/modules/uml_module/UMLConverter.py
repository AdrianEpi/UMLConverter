# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               UMLConverter.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-20 09:51:11
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-25 15:37:42
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
	imports: list

	def __init__(self):
		self.fileList = []
		self.code = ""
		self.output = ""
		self.language = None
		self.extension = None
		self.classList = []
		self.imports = []


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


	def setExtension(self, newExtension: str):
		self.extension = newExtension	


	def setClassList(self, newClassList: list):
		self.classList = newClassList	


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

			translator = Translator(tree.getTree(), self.language)
			translator.translate()
			moduleClassList = translator.getClassList()
			if (translator.getCode() != ""):
				self.__addClasses(moduleClassList)
				self.__addImports(translator.getImports(), moduleClassList)
				# self.code += "\npackage " + self.__getModuleName(i) + " #DDDDDD {\n" + translator.getCode() + "\n}\n"	# Package version
				self.code += translator.getCode()	# Non package name

		self.code += "\n" + self.__generateDependences()
		self.__writeToFile()
		self.__convertToPng()


	def __addClasses(self, classes: list):
		for i in classes:
			if (i not in self.classList):
				self.classList.append(i)
			else:
				raise Exception("Error in Translator:__translateClass(), class {} already exists.".format(i))


	def __addImports(self, imports: list, moduleClassList: list):
		for i in moduleClassList:
			for j in imports:
				self.imports.append([i, j])


	def __generateDependences(self) -> str:
		dependences = ""
		for i in self.imports: # i = [className, importedModule]
			className = i[0]
			importedModule = i[1]
			if (className in self.classList) and (importedModule in self.classList):
				dependences += className + " --> " + importedModule + " #red;line.dashed\n"
		return dependences


	def __getModuleName(self, filePath: str) -> str:
		l = []
		if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
			l = filePath.split("\\")
		else:	# Linux or MacOS
			l = filePath.split("/")
		if (len(l) >= 2):
			return l[len(l) - 2] # Is in folder
		return l[len(l) - 1]
				

	def __writeToFile(self):
		f = File(self.output)
		f.write(self.code)


	def __convertToPng(self):
		system("python -m plantuml " + self.output)





