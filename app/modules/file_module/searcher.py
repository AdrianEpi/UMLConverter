# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               searcher.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-14 09:29:24
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-31 13:18:43
#   @Description:        This file describes a searcher of files and directories

from os import listdir
from os.path import isfile, join
from app.modules.utils import EXCLUDEPATHS


class Searcher:
	"""
	This class describes a searcher.
	"""

	fileList = list
	dirList = list

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		self.fileList = []
		self.dirList = []


	def getFileList(self) -> list:
		"""
		Gets the file list.

		:returns:   The file list.
		:rtype:     list
		"""
		return self.fileList


	def getDirList(self) -> list:
		"""
		Gets the dir list.

		:returns:   The dir list.
		:rtype:     list
		"""
		return self.dirList


	def lookForFiles(self, directory: str, ext: str) -> list:
		"""
		Looks for files and directories recursively

		:param      directory:  The directory
		:type       directory:  str
		:param      ext:        The extent
		:type       ext:        str

		:returns:   List of found files with the given extension
		:rtype:     list
		"""
		files = []
		self.dirList.append(directory)
		for f in listdir(directory):
			name = join(directory, f)
			if isfile(name):
				if name.endswith(ext):
					files.append(name)
			else:
				if (f not in EXCLUDEPATHS):
					tmp = self.lookForFiles(name, ext)
					files.extend(tmp)
		self.fileList = files
		return files

	