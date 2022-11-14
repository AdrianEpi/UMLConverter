# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               file.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:24:52
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-14 09:37:52
#   @Description:        This file describes a file and its functionality


class File:
	"""
	This class describes a file.
	"""

	filename: str
	data: str

	def __init__(self, file: str):
		"""
		Constructs a new instance.

		:param      file:  The file name
		:type       file:  str
		"""
		self.data = ""
		self.filename = file
		self.__read()


	def getFilename(self) -> str:
		"""
		Gets the filename.
		
		:returns:   The filename.
		:rtype:     str
		"""
		return self.filename


	def getData(self) -> str:
		"""
		Gets the data.

		:returns:   The data.
		:rtype:     str
		"""
		return self.data


	def __read(self):
		"""
		Reads a file or raises and error if there's a problem
		"""
		try:
			f = open(self.filename, 'r')
		except FileNotFoundError:
			print(f"File {self.filename} not found.  Aborting")
			sys.exit(1)
		except OSError:
			print(f"OS error occurred trying to open {self.filename}")
			sys.exit(1)
		except Exception as err:
			print(f"Unexpected error opening {self.filename} is",repr(err))
			sys.exit(1)  
		else:
			with f:
				lines = f.readlines()
			f.close()
			for i in lines:
				self.data += i


