# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               AST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:20:25
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 21:55:38
#   @Description:        ...

# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-17 13:08:56
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-21 19:01:39
#   @Description:        This file describes an abstract ast class and all the node types that are going to be stored in data

from abc import ABC, abstractmethod
from app.modules.ast_module.pythonNode import PythonNode

NODETYPES = [
	"Module(",
	"ClassDef(",
	"Import(",
	"ImportFrom(",
	"Assign(",
	"AnnAssign(",
	"AsyncFunctionDef(",
	"FunctionDef("
]


class AST(ABC):
	"""
	This class describes a python ast.
	"""

	tree: PythonNode()
	dataList: list


	def __init__ (self):
		"""
		Constructs a new instance.
		"""
		self.tree = PythonNode()
		self.dataList = []


	def getDataList (self) -> list:
		"""
		Gets the data list.

		:returns:   The data list.
		:rtype:     list
		"""
		return self.dataList


	def getTree (self) -> PythonNode:
		"""
		Gets the tree.

		:returns:   The tree.
		:rtype:     PythonNode
		"""
		return self.tree


	def setDataList (self, l: list):
		"""
		Sets the data list.

		:param      l:    The new value
		:type       l:    list
		"""
		self.dataList = l


	def setTree (self, t: PythonNode):
		"""
		Sets the tree.

		:param      t:    The new value
		:type       t:    PythonNode
		"""
		self.tree = t


	@abstractmethod
	def generateTree(self, l: list) -> bool:
		pass


	@abstractmethod
	def __generateModule(self, pos = None, node = None) -> PythonNode:
		pass


	@abstractmethod
	def __generateClassDef(self, pos = None, node = None) -> PythonNode:
		pass


	@abstractmethod
	def __generateImport(self, pos = None, node = None) -> list or PythonNode:
		pass


	@abstractmethod
	def __generateImportFrom(self, pos = None, node = None) -> PythonNode:
		pass


	@abstractmethod
	def __generateAssign(self, pos = None, node = None) -> list:
		pass


	@abstractmethod
	def __generateAnnAssign(self, pos = None, node = None) -> PythonNode:
		pass


	@abstractmethod
	def __generateAsyncFunctionDef(self, pos = None, node = None):
		pass


	@abstractmethod
	def __generateFunctionDef(self, pos = None, node = None) -> PythonNode:
		pass


	@abstractmethod
	def __generateNode(self, pos = None, ntype = None, node = None) -> PythonNode or list:
		pass


	def printTree(self):
		"""
	 	Prints the PythonNode tree from the root.
	 	""" 
		print(self.tree.toString())