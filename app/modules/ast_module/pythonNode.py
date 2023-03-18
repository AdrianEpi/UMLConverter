# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pythonNode.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-14 21:07:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:04:42
#   @Description:        Generic node for the ast


class PythonNode:
	"""
	This class describes a python node.
	"""

	nodeType: str 
	name: str or None 					# Node name
	value: str or int or list or None 	# Returns for functions
	args: list or None 					# Inheritance for classes
	body: list or None 					# List of nodes in functions and classes

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		self.nodeType = ""
		self.name = None
		self.value = None
		self.args = []
		self.body = []

		  	 
	def getNodeType(self) -> str:
		"""
		Gets the node type.

		:returns:   The node type.
		:rtype:     str
		"""
		return self.nodeType


	def getName(self) -> str or None:
		"""
		Gets the name.

		:returns:   The name.
		:rtype:     str or None
		"""
		return self.name


	def getValue(self) -> str or int or list or None:
		"""
		Gets the value.

		:returns:   The value.
		:rtype:     str or int or list or None
		"""
		return self.value


	def getArgs(self) -> list or None:
		"""
		Gets the arguments.

		:returns:   The arguments.
		:rtype:     list or None
		"""
		return self.args

	
	def getBody(self) -> list or None:
		"""
		Gets the body.

		:returns:   The body.
		:rtype:     list or None
		"""
		return self.body


	def setNodeType(self, newNodeType: str):
		"""
		Sets the node type.

		:param      newNodeType:  The new node type
		:type       newNodeType:  str
		"""
		self.nodeType = newNodeType


	def setName(self, newName: str):
		"""
		Sets the name.

		:param      newName:  The new name
		:type       newName:  str
		"""
		self.name = newName


	def setValue(self, newValue: str or int):
		"""
		Sets the value.

		:param      newValue:  The new value
		:type       newValue:  list or int
		"""
		self.value = newValue


	def setArgs(self, newArgs: list):
		"""
		Sets the arguments.

		:param      newArgs:  The new arguments
		:type       newArgs:  list
		"""
		self.args = newArgs


	def setBody(self, newBody: list):
		"""
		Sets the body.

		:param      newBody:  The new body
		:type       newBody:  list
		"""
		self.body = newBody


	def addArg(self, node):
		"""
		Adds an argument.

		:param      node:  The node
		:type       node:  PythonNode
		"""
		self.args.append(node)


	def addBody(self, node):
		"""
		Adds a body.

		:param      node:  The node
		:type       node:  PythonNode
		"""
		self.body.append(node)


	def toString(self, indent = 1) -> str:
		"""
		Returns a string representation of the object
		
		:param      indent:     The indent
		:type       indent:     int
		
		:returns:   str
		:rtype:     str
		
		:raises     TypeError:  Error if node type is not PythonNode
		"""
		output = "\n"
		tab = str(indent * "\t")
		output += tab + self.nodeType
		if(self.name):
			output += "\n" + tab + "    Name: " + self.name
		if(self.value):
			output += "\n" + tab + "    Value: " + str(self.value)
		if(self.args):
			output += "\n" + tab + "    Args: ["
			for i in self.args:
				if (isinstance(i, PythonNode)):
					output += "\n" + i.toString(indent + 1)
				else:
					output += "\n" + str((indent + 1) * "\t") + i
			output += "\n" + tab + "    ]"
		if(self.body):
			output += "\n" + tab + "    Body: ["
			for i in self.body:
				if (isinstance(i, PythonNode)):
					output += "\n" + i.toString(indent + 1)
				else:
					raise TypeError("Error PythonNode.toString(), body must be a node.")
			output += "\n" + tab + "    ]"

		return output


