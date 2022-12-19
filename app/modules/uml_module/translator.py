# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               translator.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-19 10:00:10
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-19 10:14:21
#   @Description:        ...


from app.modules.ast_module.pythonNode import PythonNode

class Translator:

	ast: PythonNode()
	code: str
	imports: list

	def __init__(self, module):
		self.code = ""
		self.imports = []
		self.setAst(module)
		

	def getAst(self) -> PythonNode:
		return self.ast


	def getCode(self) -> str:
		return self.code


	def getImports(self) -> list:
		return self.imports


	def setAst(self, module):
		if isinstance(module, PythonNode):
			self.ast = module
		else:
			raise TypeError("Error, module provided to setAst, data received has not valid type.")


	def setCode(self, newCode):
		self.code = newCode


	def setImports(self, newImports):
		if isinstance(newImports, list):
			for i in newImports:
				if isinstance(i, PythonNode) == False:
					TypeError("Error, imports provided to setImports, some import has not valid type.")
			self.imports = newImports
		else:
			raise TypeError("Error, imports provided to setImports, data received is not a list.")
