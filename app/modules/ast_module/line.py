# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               line.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:18
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-20 10:52:11
#   @Description:        This file describes a line and its functionality

import math


INDENTATION_SIZE = 4

class Line:
	"""
	This class describes a string line.
	"""
	indentation: int
	data: str
	indentationLevel: int
	args: list

	def __init__(self, line: str):
		"""
		Constructs a new instance.
		
		:param      line:  The ast line
		:type       line:  str
		"""
		self.indentation = 0
		self.data = ""
		self.indentationLevel = 0
		self.args = []
		self.__generateLine(line)

	
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


	def __generateLine(self, line: str):
		"""
		Generates the line by reading the data from line

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
