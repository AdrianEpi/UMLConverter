# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               node.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:18
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-13 18:58:42
#   @Description:        This file describes a node and its functionality

import math


INDENTATION_SIZE = 4

class Node:
	"""
	This class describes a node.
	"""
	indentation = int
	data = str
	indentationLevel = int

	def __init__(self, line: str):
		"""
		Constructs a new instance.
		
		:param      line:  The ast line
		:type       line:  str
		"""
		self.indentation = 0
		self.data = ""
		self.indentationLevel = 0
		self.__generateNode(line)

	
	def getIndentation(self)  -> int:
		"""
		Gets the indentation.
		
		:returns:   The indentation.
		:rtype:     int
		"""
		return self.indentation


	def getData(self) -> str:
		"""
		Gets the data.

		:returns:   The data.
		:rtype:     str
		"""
		return self.data 


	def getRawData(self) -> str:
		"""
		Gets the raw data.

		:returns:   The raw data.
		:rtype:     str
		"""
		return (str(" " * self.indentation) + self.data)


	def getIndentationLevel(self) -> int:
		"""
		Gets the indentation level.

		:returns:   The indentation level.
		:rtype:     int
		"""
		return self.indentationLevel


	def __generateNode(self, line: str):
		"""
		Generates the node by reading the data from line

		:param      line:  The line
		:type       line:  str
		"""
		for i in line:
			if i == " ":
				self.indentation += 1
			else:
				self.indentationLevel = math.floor(self.indentation / INDENTATION_SIZE)
				self.indentation = self.indentationLevel * INDENTATION_SIZE # To fix some invisible characters from AST

		for i in range(self.indentation, len(line), 1):
			self.data += line[i]
