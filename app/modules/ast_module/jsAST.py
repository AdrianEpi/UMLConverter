# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               jsAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:19:59
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 21:15:35
#   @Description:        This file describes a javaScript ast class 

from app.modules.ast_module.pythonNode import PythonNode
from app.modules.ast_module.AST import AST

import esprima

class JsAST(AST):

	root

	def __init__(self):
		self.root = None

	def generateTree(self, l: list) -> bool:
		# must receive the program.body
		self.root = l
		if self.root.type == "Program":
			self.tree = self._AST__generateModule(node = dataList[0])
			return True
		else:
			return False


	def _AST__generateModule(self, pos = None, node = None) -> PythonNode:
		n = PythonNode()
		node.setNodeType("Module")


	def _AST__generateClassDef(self, pos = None, node = None) -> PythonNode:
		pass


	def _AST__generateImport(self, pos = None, node = None) -> list:
		pass


	def _AST__generateImportFrom(self, pos = None, node = None) -> PythonNode:
		pass


	def _AST__generateAssign(self, pos = None, node = None) -> list:
		pass


	def _AST__generateAnnAssign(self, pos = None, node = None) -> PythonNode:
		pass


	def _AST__generateAsyncFunctionDef(self, pos = None, node = None):
		pass


	def _AST__generateFunctionDef(self, pos = None, node = None) -> PythonNode:
		pass
