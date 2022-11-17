# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pythonNode.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-14 21:07:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-17 22:38:07
#   @Description:        ...



NODETYPES = [
	"Module",
	"ClassDef",
	"Import",
	"ImportFrom",
	"Assign",
	"AnnAssign",
	"AsyncFunctionDef",
	"FunctionDef",
	"Return"
]

class PythonNode:

	nodeType: str 
	name: str or None
	value: str or int or list or None #returns for functions
	args: list or None
	body: list or None

	def __init__(self):
		self.nodeType = ""
		self.name = None
		self.value = None
		self.args = []
		self.body = []


		  	 
	def getNodeType(self) -> str:
		return self.nodeType


	def getName(self) -> str or None:
		return self.name


	def getValue(self) -> str or int or list or None:
		return self.value


	def getArgs(self) -> list or None:
		return self.args

	
	def getBody(self) -> list or None:
		return self.body


	def setNodeType(self, newNodeType: str):
		self.nodeType = newNodeType


	def setName(self, newName: str):
		self.name = newName


	def setValue(self, newValue: str or int):
		self.value = newValue


	def setArgs(self, newArgs: list):
		self.args = newArgs


	def setBody(self, newBody: list):
		self.body = newBody


	def addArg(self, node: PythonNode):
		self.args.append(node)


	def toString(self, indent = 1) -> str:
		output = ""
		tab = str(indent * "\t")
		output += tab + "Node:\n" + tab + "Type: " + self.nodeType
		if(self.name):
			output += "\n" + tab + "Name: " + self.name
		if(self.value):
			output += "\n" + tab + "Value: " + self.value
		if(self.args):
			output += "\n" + tab + "Args: ["
			for i in self.args:
				output += "\n" + i.toString(indent + 1)
			output += "]"

		return output


