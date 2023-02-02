# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               translator.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-19 10:00:10
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-02 11:59:13
#   @Description:        Translates generated AST to mermaid language.


from app.modules.ast_module.pythonNode import PythonNode
from app.modules.utils import LANGUAGES


class Translator:
	"""
	This class describes a translator, converts a pythonNode into mermaid code.
	"""

	ast: PythonNode()
	code: str
	imports: list
	classList: list
	classInheritance: list
	language: str

	def __init__(self, module: PythonNode, lang: str):
		"""
		Constructs a new instance.

		:param      module:  The module
		:type       module:  PythonNode
		:param      lang:    The language
		:type       lang:    str
		"""
		self.code = ""
		self.imports = []
		self.classList = []
		self.classInheritance = []
		self.setAst(module)
		self.setLanguage(lang)
		

	def getAst(self) -> PythonNode:
		"""
		Gets the ast.

		:returns:   The ast.
		:rtype:     PythonNode
		"""
		return self.ast


	def getCode(self) -> str:
		"""
		Gets the code.

		:returns:   The code.
		:rtype:     str
		"""
		return self.code


	def getImports(self) -> list:
		"""
		Gets the imports.

		:returns:   The imports.
		:rtype:     list
		"""
		return self.imports


	def getClassList(self) -> list:
		"""
		Gets the class list.

		:returns:   The class list.
		:rtype:     list
		"""
		return self.classList


	def getClassInheritance(self) -> list:
		"""
		Gets the class inheritance.

		:returns:   The class inheritance.
		:rtype:     list
		"""
		return self.classInheritance

	def getLanguage(self) -> str:
		"""
		Gets the language.

		:returns:   The language.
		:rtype:     str
		"""
		return self.language


	def setAst(self, module: PythonNode):
		"""
		Sets the ast.

		:param      module:     The module
		:type       module:     PythonNode

		:raises     TypeError:  AST must be pythonNode type
		"""
		if isinstance(module, PythonNode):
			self.ast = module
		else:
			raise TypeError("Error, module provided to Translator:setAst(), data received has not valid type.")


	def setCode(self, newCode: str):
		"""
		Sets the code.

		:param      newCode:  The new code
		:type       newCode:  str
		"""
		self.code = newCode


	def setImports(self, newImports: list):
		"""
		Sets the imports.

		:param      newImports:  The new imports
		:type       newImports:  list

		:raises     TypeError:   Error if not valid type for newImports, must be a list fo pythonNodes
		"""
		if isinstance(newImports, list):
			for i in newImports:
				if isinstance(i, PythonNode) == False:
					TypeError("Error, imports provided to Translator:setImports(), some import has not valid type.")
			self.imports = newImports
		else:
			raise TypeError("Error, imports provided to Translator:setImports(), data received is not a list.")


	def setClassList(self, newClassList: list):
		"""
		Sets the class list.

		:param      newClassList:  The new class list
		:type       newClassList:  list
		"""
		self.classList = newClassList


	def setClassInheritance(self, newClassInheritance: list):
		"""
		Sets the class inheritance.

		:param      newClassInheritance:  The new class inheritance
		:type       newClassInheritance:  list
		"""
		self.classInheritance = newClassInheritance


	def setLanguage(self, lang: str):
		"""
		Sets the language.

		:param      lang:       The language
		:type       lang:       str

		:raises     Exception:  Error if language not defined in program
		"""
		if (lang in LANGUAGES):
			self.language = lang
		else:
			raise Exception("Error, not valid language in Translator:setLanguage().")


	def translate(self):
		"""
		Translates each module of the AST's body into mermaid code
		"""
		tmp = ""
		for i in self.ast.getBody():
			if i.getNodeType() == "ClassDef":
				tmp += self.__translateClass(i)
			elif i.getNodeType() == "Import": # To do: Add metrics
			 	self.imports.append(i.getName())
			elif i.getNodeType() == "ImportFrom":
				for j in i.getValue():
					self.imports.append(j)
		self.code = tmp		


	def __translateClass(self, node: PythonNode) -> str:
		"""
		Translates a class module into mermaid code

		:param      node:       The node
		:type       node:       PythonNode

		:returns:   String with the mermaid representation of the node.
		:rtype:     str

		:raises     Exception:  Error if trying to translate a non class type node
		"""
		data = "\n"
		internalClass = "" # How to represent
		className = node.getName()
		self.classList.append(className)

		if ((className == "") or (className == None)):
			raise Exception("Error in Translator:translateClass(), not name for class.")
		if node.getArgs():
			data += self.__translateInheritance(className, node.getArgs())
		data += "class " + node.getName() + " {\n"
		for i in node.getBody():
			ntype = i.getNodeType()
			if (ntype == "ClassDef"):
				internalClass += self.__translateClass(i) + "\n" + node.getName() + " +-- " + i.getName() + "\n"
			elif ((ntype == "Assign") or (ntype == "AnnAssign")):
				data += self.__translateAttrib(i) + "\n"
			elif (ntype == "FunctionDef"):
				data += self.__translateFunction(i) + "\n"
		data += "}\n"
		data += internalClass
		return data


	def getVisibility(self, line: str) -> str:
		"""
		Gets the visibility.

		:param      line:       The line
		:type       line:       str

		:returns:   The visibility.
		:rtype:     str

		:raises     Exception:  Error if not well defined visibility
		"""
		# + -> public
		# - -> private
		# # -> protected
		if ((line == "") or (line == None)):
			raise Exception("Error in Translator:getVisibility(), not name for attribute or method.")
		if self.language == "Python" or self.language == "JavaScript":
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
		"""
		Translates inheritance (includes or requires) from AST to mermaid code

		:param      className:  The class name
		:type       className:  str
		:param      l:          list with all the inheritances
		:type       l:          list

		:returns:   String with the mermaid representation of the node.
		:rtype:     str

		:raises     TypeError:  Error in case not well defined inheritance
		"""
		string = ""
		inheritance = []
		inheritance.append(className)
		for i in l:
			if isinstance(i, str):
				if (i != "ABC") and self.language == "Python":
					inheritance.append(i)
					string += i + " <|-- " + className
			elif isinstance(i, PythonNode):
				inheritance.append(i.getName())
				string += i.getName() + " <|-- " + className
			else:
				raise TypeError("Error, not valid inheritance type in Translator:translateInheritance()")

			string += "\n"
		if (len(inheritance) > 1):
			self.classInheritance.append(inheritance)
		return string


	def __translateAttrib(self, node: PythonNode) -> str:
		"""
		Translates an attribute into mermaid code

		:param      node:  The node
		:type       node:  PythonNode

		:returns:   String with the mermaid representation of the node.
		:rtype:     str
		"""
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
				if types == None:
					types = ""
			return "    " + self.getVisibility(node.getName()) + " " + types + " " + node.getName()


	def __translateFunction(self, node: PythonNode) -> str:
		"""
		Translates a function into mermaid code

		:param      node:  The node
		:type       node:  PythonNode

		:returns:   String with the mermaid representation of the node.
		:rtype:     str
		"""
		data = "    " + self.getVisibility(node.getName()) + " " + node.getName() + "("
		args = ""
		for i in node.getArgs():
			if isinstance(i, str):
				args += i + ", "
			elif isinstance(i, PythonNode):
				args += i.getName() + ", "
		args = args[:(len(args) - 2)]
		return data + args + ")"