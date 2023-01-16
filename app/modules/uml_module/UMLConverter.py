# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               UMLConverter.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-20 09:51:11
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 11:15:00
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
	"""
	This class describes an uml converter, generates the AST of a given code,
	then extracts the relevant information, translates into mermaid code and
	generates an image of the result.
	"""

	fileList: list
	code: str
	output: str
	language: str
	extension: str
	classList: list
	imports: list

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		self.fileList = []
		self.code = ""
		self.output = ""
		self.language = None
		self.extension = None
		self.classList = []
		self.imports = []


	def getFileList(self) -> list:
		"""
		Gets the file list.

		:returns:   The file list.
		:rtype:     list
		"""
		return self.fileList


	def getCode(self) -> str:
		"""
		Gets the code.

		:returns:   The code.
		:rtype:     str
		"""
		return self.code


	def getOutput(self) -> str:
		"""
		Gets the output.

		:returns:   The output.
		:rtype:     str
		"""
		return self.output


	def getLanguage(self) -> str:
		"""
		Gets the language.

		:returns:   The language.
		:rtype:     str
		"""
		return self.language


	def getExtension(self) -> str:
		"""
		Gets the extension.

		:returns:   The extension.
		:rtype:     str
		"""
		return self.extension


	def getClassList(self) -> list:
		"""
		Gets the class list.

		:returns:   The class list.
		:rtype:     list
		"""
		return self.classList


	def getImports(self) -> list:
		"""
		Gets the imports.

		:returns:   The imports.
		:rtype:     list
		"""
		return self.imports


	def setFileList(self, newFileList: list):
		"""
		Sets the file list.

		:param      newFileList:  The new file list
		:type       newFileList:  list
		"""
		self.fileList = newFileList


	def setCode(self, newCode: str):
		"""
		Sets the code.

		:param      newCode:  The new code
		:type       newCode:  str
		"""
		self.code = newCode


	def setOutput(self, newOutput: str):
		"""
		Sets the output.

		:param      newOutput:  The new output
		:type       newOutput:  str
		"""
		self.output = newOutput	


	def setLanguage(self, newLanguage: str) -> bool:
		"""
		Sets the language.

		:param      newLanguage:  The new language
		:type       newLanguage:  str

		:returns:   True if language exist and could be added, false otherwise
		:rtype:     bool
		"""
		if newLanguage in LANGUAGES:
			self.language = newLanguage	
			self.__generateExtention()
			return True
		return False


	def setExtension(self, newExtension: str):
		"""
		Sets the extension.

		:param      newExtension:  The new extension
		:type       newExtension:  str
		"""
		self.extension = newExtension	


	def setClassList(self, newClassList: list):
		"""
		Sets the class list.

		:param      newClassList:  The new class list
		:type       newClassList:  list
		"""
		self.classList = newClassList	


	def setImports(self, newImports: list):
		"""
		Sets the imports.

		:param      newImports:  The new imports
		:type       newImports:  list
		"""
		self.imports = newImports	


	def __generateExtention(self):
		"""
		Generates the extention of the files in function of the project language

		:raises     Exception:  Error if trying to generate extention of a non defined language
		"""
		if self.language == "Python":
			self.extension = ".py"
		# elif ...
		else:
			raise Exception("Error in UMLConverter:generateExtention(), not valid language")


	def __askFiles(self):
		"""
		Ask the user for the language, the project folder and where to store the output.
		"""
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


	def run(self):
		"""
		Executes UMLCovnerter
		"""
		self.__askFiles()
		self.generateUML()
		self.writeToFile()
		self.convertToPng()


	def generateUML(self):
		"""
		Generates the AST, and converts to mermaid
		"""
		self.code = ""
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
		

	def __addClasses(self, classes: list):
		"""
		Adds classes.

		:param      classes:    The classes
		:type       classes:    list

		:raises     Exception:  Error if the class name is already defined
		"""
		for i in classes:
			if (i not in self.classList):
				self.classList.append(i)
			else:
				raise Exception("Error in Translator:__translateClass(), class {} already exists.".format(i))


	def __addImports(self, imports: list, moduleClassList: list):
		"""
		Adds imports.

		:param      imports:          The imports
		:type       imports:          list
		:param      moduleClassList:  The module class list
		:type       moduleClassList:  list
		"""
		for i in moduleClassList:
			for j in imports:
				self.imports.append([i, j])


	def __generateDependences(self) -> str:
		"""
		Generate the relationships between classes

		:returns:   String representation of the relationships in mermaid
		:rtype:     str
		"""
		dependences = ""
		for i in self.imports: # i = [className, importedModule]
			className = i[0]
			importedModule = i[1]
			if (className in self.classList) and (importedModule in self.classList):
				dependences += className + " --> " + importedModule + " #red;line.dashed\n"
		return dependences


	def __getModuleName(self, filePath: str) -> str:
		"""
		Gets the module name.

		:param      filePath:  The file path
		:type       filePath:  str

		:returns:   The module name.
		:rtype:     str
		"""
		l = []
		if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
			l = filePath.split("\\")
		else:	# Linux or MacOS
			l = filePath.split("/")
		if (len(l) >= 2):
			return l[len(l) - 2] # Is in folder
		return l[len(l) - 1]
				

	def writeToFile(self) -> bool:
		"""
		Writes to file.

		:returns:   True if code could be written and exists, false otherwise
		:rtype:     bool
		"""
		if self.code != "\n":
			f = File(self.output)
			f.write(self.code)
			return True
		else:
			return False


	def convertToPng(self) -> bool:
		"""
		Transforms the mermaid code into png image

		:returns:   True if the image could be generated, false otherwise
		:rtype:     bool
		"""
		if self.code != "\n":
			system("python -m plantuml " + self.output)
			return True
		return False






