# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               AST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:20:25
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 12:41:10
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
#   @Description:        This file describes a python ast class and all the node types that are going to be stored in data

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
	def __generateModule(self, pos: int) -> PythonNode:
		pass


	@abstractmethod
	def __generateClassDef(self, pos: int) -> PythonNode:
		pass


	@abstractmethod
	def __generateImport(self, pos: int) -> list:
		pass


	@abstractmethod
	def __generateImportFrom(self, pos: int) -> PythonNode:
		pass


	@abstractmethod
	def __generateAssign(self, pos: int) -> list:
		pass


	@abstractmethod
	def __generateAnnAssign(self, pos: int) -> PythonNode:
		pass


	@abstractmethod
	def __generateAsyncFunctionDef(self, pos: int):
		pass


	@abstractmethod
	def __generateFunctionDef(self, pos: int) -> PythonNode:
		pass


	def _generateNode(self, pos: int, ntype: str) -> PythonNode or list:
		"""
		Calls the __generateNode corresponded to the node type

		:param      pos:        The position
		:type       pos:        int
		:param      ntype:      The ntype
		:type       ntype:      str

		:returns:   PythonNode or list
		:rtype:     PythonNode or list

		:raises     TypeError:  Error if not valid node type
		"""
		if ntype == "Module(":
			return self.__generateModule(pos)
		elif ntype == "ClassDef(":
			return self.__generateClassDef(pos)
		elif ntype == "Import(":
			return self.__generateImport(pos)
		elif ntype == "ImportFrom(":
			return self.__generateImportFrom(pos)
		elif ntype == "Assign(":
			return self.__generateAssign(pos)
		elif ntype == "AnnAssign(":
			return self.__generateAnnAssign(pos)
		elif ntype == "AsyncFunctionDef(":
			return self.__generateAsyncFunctionDef(pos)
		elif ntype == "FunctionDef(":
			return self.__generateFunctionDef(pos)
		else:
			raise TypeError("Error in PyAST.__generateNode() (ast line {}), not valid node type.".format(pos))


	def printTree(self):
		"""
	 	Prints the PythonNode tree from the root.
	 	""" 
		print(self.tree.toString())