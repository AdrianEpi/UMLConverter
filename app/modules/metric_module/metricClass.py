# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricClass.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-02 13:43:16
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:18:16
#   @Description:        This file describes the metrics for each class


class MetricClass:
	"""
	This class describes a metric class.
	"""

	classID: int 				# Class identifier
	name: str 					# Class name
	children: list 				# List of children classIDs inherited from this class
	noc: list 					# List of children  grandchildren... classIDs
	inheritance: list 			# List o classes classIDs of which this class is inherited of
	include: list 				# List of classIDs from another class where this class is included
	inclusion: list 			# List of classIDs included in this class
	nLines: int 				# Ammount of lines in the class file
	codeLines: int 				# Ammount of code lines (no empty ones or {})
	commentLines: int 			# Ammount of commented lines
	packageID: int 				# Package name
	cbo: int 					# Coupling between object classes
	ccd: float 					# Code comments density
	ev: float 					# Evaluation of the class (0-100)%

	def __init__(self, id: int, cname: str):
		"""
		Constructs a new instance.

		:param      id:     The identifier
		:type       id:     int
		:param      cname:  The cname
		:type       cname:  str
		"""
		self.classID = id 
		self.name = cname
		self.children = [] 
		self.noc = [] 
		self.inheritance = [] 
		self.include = [] 
		self.inclusion = []
		self.nLines = 0
		self.codeLines = 0 
		self.commentLines = 0 
		self.packageID = 0 
		self.cbo = 0 
		self.ccd = 0.0 
		self.ev = 0.0
		

	def getClassID(self) -> int:
		"""
		Gets the class id.

		:returns:   The class id.
		:rtype:     int
		"""
		return 	self.classID


	def getName(self) -> str:
		"""
		Gets the name.

		:returns:   The name.
		:rtype:     str
		"""
		return self.name
	

	def getChildren(self) -> list:
		"""
		Gets the children.

		:returns:   The children.
		:rtype:     list
		"""
		return 	self.children

	
	def getNoc(self) -> list:
		"""
		Gets the noc.

		:returns:   The noc.
		:rtype:     list
		"""
		return 	self.noc

	
	def getInheritance(self) -> list:
		"""
		Gets the inheritance.

		:returns:   The inheritance.
		:rtype:     list
		"""
		return 	self.inheritance

	
	def getInclude(self) -> list:
		"""
		Gets the include.

		:returns:   The include.
		:rtype:     list
		"""
		return 	self.include


	def getInclusion(self) -> list:
		"""
		Gets the inclusion.

		:returns:   The inclusion.
		:rtype:     list
		"""
		return 	self.inclusion

	
	def getNLines(self) -> int:
		"""
		Gets the n lines.

		:returns:   The n lines.
		:rtype:     int
		"""
		return self.nLines


	def getCodeLines(self) -> int:
		"""
		Gets the code lines.

		:returns:   The code lines.
		:rtype:     int
		"""
		return 	self.codeLines

	
	def getCommentLines(self) -> int:
		"""
		Gets the comment lines.

		:returns:   The comment lines.
		:rtype:     int
		"""
		return 	self.commentLines

	
	def getPackageID(self) -> int:
		"""
		Gets the package id.

		:returns:   The package id.
		:rtype:     int
		"""
		return 	self.packageID

	
	def getCBO(self) -> int:
		"""
		Gets the cbo.

		:returns:   The cbo.
		:rtype:     int
		"""
		return 	self.cbo

	
	def getCcd(self) -> float:
		"""
		Gets the ccd.

		:returns:   The ccd.
		:rtype:     float
		"""
		return 	self.ccd


	def getEval(self) -> float:
		"""
		Gets the eval.

		:returns:   The eval.
		:rtype:     float
		"""
		return self.ev

	
	def setClassID(self, newClassID:int):
		"""
		Sets the class id.

		:param      newClassID:  The new class id
		:type       newClassID:  int
		"""
		self.classID = newClassID
		
	
	def setChildren(self, newChildren:list):
		"""
		Sets the children.

		:param      newChildren:  The new children
		:type       newChildren:  list
		"""
		self.children = newChildren
		
	
	def setNoc(self, newNoc:list):
		"""
		Sets the noc.

		:param      newNoc:  The new noc
		:type       newNoc:  list
		"""
		self.noc = newNoc
		
	
	def setInheritance(self, newInheritance:list):
		"""
		Sets the inheritance.

		:param      newInheritance:  The new inheritance
		:type       newInheritance:  list
		"""
		self.inheritance = newInheritance
		
	
	def setInclude(self, newInclude:list):
		"""
		Sets the include.

		:param      newInclude:  The new include
		:type       newInclude:  list
		"""
		self.include = newInclude


	def setInclusion(self, newInclusion:list):
		"""
		Sets the inclusion.

		:param      newInclusion:  The new inclusion
		:type       newInclusion:  list
		"""
		self.inclusion = newInclusion
		
	
	def setNLines(self, newNLines:int):
		"""
		Sets the n lines.

		:param      newNLines:  The new n lines
		:type       newNLines:  int
		"""
		self.nLines = newNLines


	def setCodeLines(self, newCodeLines:int):
		"""
		Sets the code lines.

		:param      newCodeLines:  The new code lines
		:type       newCodeLines:  int
		"""
		self.codeLines = newCodeLines
		
	
	def setCommentLines(self, newCommentLines:int):
		"""
		Sets the comment lines.

		:param      newCommentLines:  The new comment lines
		:type       newCommentLines:  int
		"""
		self.commentLines = newCommentLines
		
	
	def setPackageID(self, newPackageID:int):
		"""
		Sets the package id.

		:param      newPackageID:  The new package id
		:type       newPackageID:  int
		"""
		self.packageID = newPackageID
		
	
	def setCBO(self, newCBO:int):
		"""
		Sets the cbo.

		:param      newCBO:  The new cbo
		:type       newCBO:  int
		"""
		self.cbo = newCBO
		
	
	def setCcd(self, newCcd:float):
		"""
		Sets the ccd.

		:param      newCcd:  The new ccd
		:type       newCcd:  float
		"""
		self.ccd = newCcd


	def addChild(self, id: int):
		"""
		Adds a child.

		:param      id:   The identifier
		:type       id:   int
		"""
		if id not in self.children:
			self.children.append(id)


	def addInheritance(self, id: int):
		"""
		Adds an inheritance.

		:param      id:   The identifier
		:type       id:   int
		"""
		if id not in self.inheritance:
			self.inheritance.append(id)


	def addInclude(self, id: int):
		"""
		Adds an include.

		:param      id:   The identifier
		:type       id:   int
		"""
		if id not in self.include:
			self.include.append(id)


	def addInclusion(self, id: int):
		"""
		Adds an inclusion.

		:param      id:   The identifier
		:type       id:   int
		"""
		if id not in self.inclusion:
			self.inclusion.append(id)


	def calculateCCD(self):
		"""
		Calculates the ccd.
		"""
		self.ccd = round((self.commentLines / self.codeLines), 2)


	def evaluate(self, dic: dict):
		"""
		Evaluates the metrics with the pertentages given in dic

		:param      dic:  The dic
		:type       dic:  dict
		"""
		ev = 0.0
		# CBO
		if self.cbo < 39: # 30 + Optimum, 30 is the max it can go over or lower the optimum
			OPTIMUM = 9
			ev += ((30 - abs(self.cbo - OPTIMUM)) / 30) * (dic['CBO'] / 100)

		# NOC 
		if len(self.noc) < 13: # 10 + Optimum, 10 is the max it can go over or lower the optimum
			OPTIMUM = 3
			ev += ((10 - abs(len(self.noc) - OPTIMUM)) / 10) * (dic['NOC'] / 100)

		# CCD 
		if self.ccd > 1: 
			ev += (dic['CCD'] / 100)
		else :
			ev += self.ccd * (dic['CCD'] / 100)

		self.ev = round(ev * 100, 2)


	def print(self):
		"""
		Prints the metric class information
		"""
		s = ""
		s += "\n\n\n\t Class " + str(self.classID)
		s += "\n\t\tName: " + self.name
		s += "\n\t\tChildren: " + str(self.children)
		s += "\n\t\tInheritance: " + str(self.inheritance)
		s += "\n\t\tIncluded in: " + str(self.include)
		s += "\n\t\tPackageID: " + str(self.packageID)
		s += "\n\t\tNOC (Number of Children): " + str(self.noc)
		s += "\n\t\tNumber of Lines: " + str(self.nLines)
		s += "\n\t\tCode Lines: " + str(self.codeLines)
		s += "\n\t\tComment Lines: " + str(self.commentLines)
		s += "\n\t\tCCD (Code Comments Density): " + str(self.ccd)
		s += "\n\t\tCC (Class Coupling): " + str(self.cbo)
		print(s)