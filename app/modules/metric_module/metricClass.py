# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricClass.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-02 13:43:16
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 19:34:22
#   @Description:        ...


class MetricClass:

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
		return 	self.classID


	def getName(self) -> str:
		return self.name
	

	def getChildren(self) -> list:
		return 	self.children

	
	def getNoc(self) -> list:
		return 	self.noc

	
	def getInheritance(self) -> list:
		return 	self.inheritance

	
	def getInclude(self) -> list:
		return 	self.include


	def getInclusion(self) -> list:
		return 	self.inclusion

	
	def getNLines(self) -> int:
		return self.nLines


	def getCodeLines(self) -> int:
		return 	self.codeLines

	
	def getCommentLines(self) -> int:
		return 	self.commentLines

	
	def getPackageID(self) -> int:
		return 	self.packageID

	
	def getCBO(self) -> int:
		return 	self.cbo

	
	def getCcd(self) -> float:
		return 	self.ccd


	def getEval(self) -> float:
		return self.ev

	
	def setClassID(self, newClassID:int):
		self.classID = newClassID
		
	
	def setChildren(self, newChildren:list):
		self.children = newChildren
		
	
	def setNoc(self, newNoc:list):
		self.noc = newNoc
		
	
	def setInheritance(self, newInheritance:list):
		self.inheritance = newInheritance
		
	
	def setInclude(self, newInclude:list):
		self.include = newInclude


	def setInclusion(self, newInclusion:list):
		self.inclusion = newInclusion
		
	
	def setNLines(self, newNLines:int):
		self.nLines = newNLines


	def setCodeLines(self, newCodeLines:int):
		self.codeLines = newCodeLines
		
	
	def setCommentLines(self, newCommentLines:int):
		self.commentLines = newCommentLines
		
	
	def setPackageID(self, newPackageID:int):
		self.packageID = newPackageID
		
	
	def setCBO(self, newCBO:int):
		self.cbo = newCBO
		
	
	def setCcd(self, newCcd:float):
		self.ccd = newCcd


	def addChild(self, id: int):
		if id not in self.children:
			self.children.append(id)


	def addInheritance(self, id: int):
		if id not in self.inheritance:
			self.inheritance.append(id)


	def addInclude(self, id: int):
		if id not in self.include:
			self.include.append(id)


	def addInclusion(self, id: int):
		if id not in self.inclusion:
			self.inclusion.append(id)


	def calculateCCD(self):
		self.ccd = round((self.commentLines / self.codeLines), 2)


	def evaluate(self):
		ev = 0.0
		# CC = 42.5%
		if self.cbo < 39: # 30 + Optimum, 30 is the max it can go over or lower the optimum
			OPTIMUM = 9
			ev += ((30 - abs(self.cbo - OPTIMUM)) / 30) * 0.425

		# NOC = 15%
		if len(self.noc) < 13: # 10 + Optimum, 10 is the max it can go over or lower the optimum
			OPTIMUM = 3
			ev += ((10 - abs(len(self.noc) - OPTIMUM)) / 10) * 0.15

		# CCD = 42.5%
		if self.ccd > 1: 
			ev += 0.425
		else :
			ev += self.ccd * 0.425

		self.ev = round(ev * 100, 2)


	def print(self):
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