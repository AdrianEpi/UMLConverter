# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricClass.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-02 13:43:16
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-06 12:07:11
#   @Description:        ...


class MetricClass:

	classID: int 				# Class identifier
	name: str 					# Class name
	children: list 				# List of children classIDs inherited from this class
	noc: list 					# List of children  grandchildren... classIDs
	inheritance: list 			# List o classes classIDs of which this class is inherited of
	include: list 				# List of classIDs from another class where this class is included
	codeLines: int 				# Ammount of code lines (no empty ones or {})
	commentLines: int 			# Ammount of commented lines
	packageID: int 				# Package name
	cc: int 					# Class coupling (ACO)
	lcom: float					# Lack of cohesion in methods
	ccd: float 					# Code comments density

	def __init__(self, id: int, cname: str):
		self.classID = id 
		self.children = [] 
		self.noc = [] 
		self.inheritance = [] 
		self.include = [] 
		self.codeLines = 0 
		self.commentLines = 0 
		self.packageID = 0 
		self.cc = 0 
		self.lcom = 0.0 
		self.ccd = 0.0 
		self.name = cname

	
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

	
	def getCodeLines(self) -> int:
		return 	self.codeLines

	
	def getCommentLines(self) -> int:
		return 	self.commentLines

	
	def getPackageID(self) -> int:
		return 	self.packageID

	
	def getCc(self) -> int:
		return 	self.cc

	
	def getLcom(self) -> float:
		return 	self.lcom

	
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
		
	
	def setCodeLines(self, newCodeLines:int):
		self.codeLines = newCodeLines
		
	
	def setCommentLines(self, newCommentLines:int):
		self.commentLines = newCommentLines
		
	
	def setPackageID(self, newPackageID:int):
		self.packageID = newPackageID
		
	
	def setCc(self, newCc:int):
		self.cc = newCc
		
	
	def setLcom(self, newLcom:float):
		self.lcom = newLcom
		
	
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


	# def generateNOC(self, metricClass: MetricClass):
	# 	# self.noc = self.children
	# 	# for i in classList:
	# 	# 	if self.getClassID in i.getInheritance():
	# 	# 		self.noc.append(i.getClassID())



	def calculateCCD(self):
		self.ccd = self.commentLines / self.codeLines


	def print(self):
		s = ""
		s += "\n\n\n\t Class " + str(self.classID)
		s += "\n\t\tName: " + self.name
		s += "\n\t\tChildren: " + str(self.children)
		s += "\n\t\tInheritance: " + str(self.inheritance)
		s += "\n\t\tIncluded in: " + str(self.include)
		s += "\n\t\tPackageID: " + str(self.packageID)
		print(s)