# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               AST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:20:25
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-02 12:12:15
#   @Description:        This file describes an abstract ast class and all the node types that are going to be stored in data


from abc import ABC, abstractmethod
from app.modules.ast_module.pythonNode import PythonNode


class AST(ABC):
	"""
	This class describes a python abstract class for ast.
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
		"""
		Generates the tree

		:param      l:    list with nodes or lines 
		:type       l:    list

		:returns:   True if the tree was generated correctly, false otherwise
		:rtype:     bool
		"""
		pass


	@abstractmethod
	def __generateModule(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a module

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		pass


	@abstractmethod
	def __generateClassDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generate a class

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		pass


	@abstractmethod
	def __generateImport(self, pos = None, node = None) -> list or PythonNode:
		"""
		Generate an import

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   list with pythonNodes or a single pythonNode
		:rtype:     list or PythonNode
		"""
		pass


	@abstractmethod
	def __generateImportFrom(self, pos = None, node = None) -> PythonNode:
		"""
		Generates an importFrom

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		pass


	@abstractmethod
	def __generateAssign(self, pos = None, node = None) -> list:
		"""
		Generates an assign

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   list with assigns
		:rtype:     list
		"""
		pass


	@abstractmethod
	def __generateAnnAssign(self, pos = None, node = None) -> PythonNode:
		"""
		Generates an annassign

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		pass


	@abstractmethod
	def __generateAsyncFunctionDef(self, pos = None, node = None):
		"""
		Generates am asyncFunction

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node
		"""
		pass


	@abstractmethod
	def __generateFunctionDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a function

		:param      pos:   The position
		:type       pos:   integer
		:param      node:  The node
		:type       node:  node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		pass


	@abstractmethod
	def __generateNode(self, pos = None, ntype = None, node = None) -> PythonNode or list:
		"""
		Generates a pythonnode

		:param      pos:    The position
		:type       pos:    integer
		:param      ntype:  The ntype
		:type       ntype:  string
		:param      node:   The node
		:type       node:   node

		:returns:   list of pythonnodes or pythonnode
		:rtype:     PythonNode or list
		"""
		pass


	def printTree(self):
		"""
	 	Prints the PythonNode tree from the root.
	 	""" 
		print(self.tree.toString())