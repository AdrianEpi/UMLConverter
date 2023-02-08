# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:24:52
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 10:56:53
#   @Description:        This file describes a file and its functionality

import sys
import os
from app.modules.utils import COMMENTS

class File:
	"""
	This class describes a file.
	"""

	fileName: str
	data: str
	nLines: int
	nCommentLines: int
	nCodeLines: int

	def __init__(self, file: str):
		"""
		Constructs a new instance.

		:param      file:  The file name
		:type       file:  str
		"""
		self.data = ""
		self.fileName = file
		self.nLines = 0
		self.nCodeLines = 0
		self.nCommentLines = 0

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


	def readAndAnalyze(self, language: str):
		try:
			f = open(self.fileName, 'r')
		except FileNotFoundError:
			raise FileNotFoundError("Error, {} file not found.".format(self.fileName))
		except OSError:
			raise OSError("OS error trying to open {} file.".format(self.fileName))
		except Exception as err:
			raise Exception("Unexpected error with {} file.".format(self.fileName))
		else:
			single = COMMENTS[language]['single']
			multiStart = COMMENTS[language]['multiStart']
			multiEnd = COMMENTS[language]['multiEnd']
			with f:
				lines = f.readlines()
			f.close()
			insideComment = False
			for i in lines:
				self.nLines += 1
				self.data += i
				if insideComment == True:
					self.nCommentLines += 1
					if multiEnd in i:
						insideComment = False
					
				elif multiStart in i:
					insideComment = True
					tmp = i.split(multiStart)
					self.nCommentLines += 1
					if len(tmp) > 1:
						self.nCodeLines += 1
					if (multiStart == multiEnd) and (i.count(multiStart) % 2 == 0):
						insideComment = False 
				elif single in i:
					tmp = i.split(single)
					self.nCommentLines += 1
					if len(tmp) > 1:
						self.nCodeLines += 1
				else:
					if len(i.split()) > 1:
						self.nCodeLines += 1



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


	def getLinesInfo(self) -> dict:
		return {
			'nLines': self.nLines,
			'commentLines': self.nCommentLines,
			'codeLines': self.nCodeLines
		}

