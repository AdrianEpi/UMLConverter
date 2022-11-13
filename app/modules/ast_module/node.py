# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               node.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:18
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-13 16:55:15
#   @Description:        This file describes a node and its functionality

import math


INDENTATION_SIZE = 4

class Node:
	"""
	This class describes a node.
	"""
	indentation = 0
	data = ""
	indentationLevel = 0

	def __init__(self, line):
		"""
		Constructs a new instance.

		:param      line:  The ast line
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

	
	def getIndentation(self):
		"""
		Gets the indentation.

		:returns:   The indentation.
		:rtype:     int
		"""
		return self.indentation


	def getData(self):
		"""
		Gets the data.

		:returns:   The data.
		:rtype:     str
		"""
		return self.data 


	def getRawData(self):
		"""
		Gets the raw data.

		:returns:   The raw data.
		:rtype:     str
		"""
		return (str(" " * self.indentation) + self.data)


	def getIndentationLevel(self):
		"""
		Gets the indentation level.

		:returns:   The indentation level.
		:rtype:     int
		"""
		return self.indentationLevel

