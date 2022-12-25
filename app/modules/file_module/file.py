# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:24:52
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-25 11:05:18
#   @Description:        This file describes a file and its functionality

import sys
import os

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


	def read(self):
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
			raise Exception("Unexpected error with {} file.".format(self.fileName))
		else:
			with f:
				lines = f.readlines()
			f.close()
			for i in lines:
				self.data += i


	def write(self, data: str):
		"""
		Writes the data into the file stored in self.fileName
		sys.platform
			'linux'	  for Linux
			'win32'   for Windows(Win32)
			'cygwin'  for Windows(cygwin)
			'darwin'  for macOS
			'aix'     for AIX

		:param      data:       The data
		:type       data:       str
		"""
		tmp = []
		dirName = ""
		if ((sys.platform == "win32") or (sys.platform == "cygwin")):
			tmp = self.fileName.split("\\")
			for i in range(len(tmp)):
				if i == (len(tmp) - 1):
					break
				else:
					dirName += tmp[i] + "\\"
		else:
			tmp = self.fileName.split("/")
			for i in range(len(tmp)):
				if i == (len(tmp) - 1):
					break
				else:
					dirName += tmp[i] + "/"

		os.makedirs(dirName, exist_ok=True)
		try:
			f = open(self.fileName, 'w+')
		except OSError:
			raise OSError("OS error trying to open {} file.".format(self.fileName))
		except Exception as err:
			raise Exception("Unexpected error with {} file.".format(self.fileName))
		else:
			with f:
				f.write(data)
			f.close()
		self.data = data


