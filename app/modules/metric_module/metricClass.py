# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricClass.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-02 13:43:16
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 11:47:31
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
	cc: int 					# Class coupling (ACO)
	ccd: float 					# Code comments density

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
		self.cc = 0 
		self.ccd = 0.0 
		

	
	def getClassID(self) -> int:
		return 	self.classID

	
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

	
	def getCc(self) -> int:
		return 	self.cc

	
	def getCcd(self) -> float:
		return 	self.ccd

	
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
		
	
	def setCc(self, newCc:int):
		self.cc = newCc
		
	
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


	def calculateCCD(self) -> int:
		self.ccd = self.commentLines / self.codeLines
		return self.ccd


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
		s += "\n\t\tCCD (Code Comments Density): " + str(self.calculateCCD())
		s += "\n\t\tCC (Class Coupling): " + str(self.cc)
		print(s)