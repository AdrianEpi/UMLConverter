# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               translator.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-19 10:00:10
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-24 19:47:46
#   @Description:        Translates generated AST to mermaid language.


from app.modules.ast_module.pythonNode import PythonNode

LANGUAGES = [
	"Python",
	"Option2"
]

class Translator:

	ast: PythonNode()
	code: str
	imports: list
	classList: list
	language: str

	def __init__(self, module: PythonNode, lang: str):
		self.code = ""
		self.imports = []
		self.classList = []
		self.setAst(module)
		self.setLanguage(lang)
		

	def getAst(self) -> PythonNode:
		return self.ast


	def getCode(self) -> str:
		return self.code


	def getImports(self) -> list:
		return self.imports


	def getClassList(self) -> list:
		return self.classList


	def getLanguage(self) -> str:
		return self.language


	def setAst(self, module: PythonNode):
		if isinstance(module, PythonNode):
			self.ast = module
		else:
			raise TypeError("Error, module provided to Translator:setAst(), data received has not valid type.")


	def setCode(self, newCode: str):
		self.code = newCode


	def setImports(self, newImports: list):
		if isinstance(newImports, list):
			for i in newImports:
				if isinstance(i, PythonNode) == False:
					TypeError("Error, imports provided to Translator:setImports(), some import has not valid type.")
			self.imports = newImports
		else:
			raise TypeError("Error, imports provided to Translator:setImports(), data received is not a list.")


	def setClassList(self, newClassList: list):
		self.classList = newClassList


	def setLanguage(self, lang: str):
		if (lang in LANGUAGES):
			self.language = lang
		else:
			raise Exception("Error, not valid language in Translator:setLanguage().")


	def translate(self):
		tmp = ""
		for i in self.ast.getBody():
			if i.getNodeType() == "ClassDef":
				tmp += self.__translateClass(i)
			# elif i.getNodeType() == "Import":
			# 	# Metrics
			# elif i.getNodeType() == "ImportFrom":
			# 	# Metrics
		self.code = tmp		


	def __translateClass(self, node: PythonNode) -> str:
		data = "\n"
		internalClass = "" # How to represent
		if ((node.getName() == "") or (node.getName() == None)):
			raise Exception("Error in Translator:translateClass(), not name for class.")
		if node.getArgs():
			data += self.__translateInheritance(node.getName(), node.getArgs())
		data += "class " + node.getName() + " {\n"
		for i in node.getBody():
			ntype = i.getNodeType()
			if (ntype == "ClassDef"):
				internalClass += self.__translateClass(i)
			elif ((ntype == "Assign") or (ntype == "AnnAssign")):
				data += self.__translateAttrib(i) + "\n"
			elif (ntype == "FunctionDef"):
				data += self.__translateFunction(i) + "\n"
		data += "}\n"
		return data


	def getVisibility(self, line: str) -> str:
		# + -> public
		# - -> private
		# # -> protected
		if ((line == "") or (line == None)):
			raise Exception("Error in Translator:getVisibility(), not name for attribute or method.")
		if self.language == "Python":
			if (len(line) == 1):
				return "+"
			if (line[0] == "_"):
				if (line[1] == "_"):
					return "-"
				else:
					return "#"
			else: 
				return "+"
		# elif self.language == "otherlanguage":
		# 	# ...


	def __translateInheritance(self, className: str, l: list) -> str:
		string = ""
		for i in l:
			if isinstance(i, str):
				string += i + " <|-- " + className
			elif isinstance(i, PythonNode):
				string += i.getName() + " <|-- " + className
			else:
				raise TypeError("Error, not valid inheritance type in Translator:translateInheritance()")

			string += "\n"
		return string


	def __translateAttrib(self, node: PythonNode) -> str:
		if node.getNodeType() == "Assign":
			return "    " + self.getVisibility(node.getName()) + " " + node.getName()
		else: # AnnAssign
			types = ""
			if isinstance(node.getValue(), list):
				types = "["
				types += " or ".join(node.getValue())
				types += "]"
			else:
				types = node.getValue()
			return "    " + self.getVisibility(node.getName()) + " " + types + " " + node.getName()


	def __translateFunction(self, node: PythonNode) -> str:
		data = "    " + self.getVisibility(node.getName()) + " " + node.getName() + "("
		args = ""
		for i in node.getArgs():
			if isinstance(i, str):
				args += i + ", "
			elif isinstance(i, PythonNode):
				args += i.getName() + ", "
		args = args[:(len(args) - 2)]
		return data + args + ")"


