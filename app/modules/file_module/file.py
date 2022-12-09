# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:24:52
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-09 10:38:08
#   @Description:        This file describes a file and its functionality

import sys

class File:
	"""
	This class describes a file.
	"""

	fileName: str
	data: str

	def __init__(self, file: str):
		"""
		Constructs a new instance.

		:param      file:  The file name
		:type       file:  str
		"""
		self.data = ""
		self.fileName = file
		self.__read()


	def getFileName(self) -> str:
		"""
		Gets the fileName.
		
		:returns:   The fileName.
		:rtype:     str
		"""
		return self.fileName


	def getData(self) -> str:
		"""
		Gets the data.

		:returns:   The data.
		:rtype:     str
		"""
		return self.data


	def setFileName(self, name: str):
		"""
		Sets the fileName.

		:param      name:  The name
		:type       name:  str
		"""
		self.fileName = name


	def setData(self, newData: str):
		"""
		Sets the data.

		:param      newData:  The new data
		:type       newData:  str
		"""
		self.data = newData


	def __read(self):
		"""
		Reads a file or raises and error if there's a problem
		"""
		try:
			f = open(self.fileName, 'r')
		except FileNotFoundError:
			raise FileNotFoundError("Error, {} file not found.".format(self.fileName))
		except OSError:
			raise OSError("OS error trying to open {} file.".format(self.fileName))
		except Exception as err:
			raise Exception("Unexpected error, {} file not found.".format(self.fileName))
		else:
			with f:
				lines = f.readlines()
			f.close()
			for i in lines:
				self.data += i


