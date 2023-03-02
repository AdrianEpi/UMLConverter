# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricPackage.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:10:05
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-02 12:52:21
#   @Description:        ...


class MetricPackage:

	packageID: int
	classList: list
	name: str
	maxDIT: int 		# Maximum Depth of Inheritance Tree
	lcom: float			# Lack of cohesion in methods
	ev: float 			# Evaluation of the package (0-100)%
	cas: float 			# Evaluation of the class average


	def __init__(self, id: int, pname: str):
		self.packageID = id
		self.classList = []
		self.name = pname
		self.maxDIT = 0
		self.lcom = 0.0
		self.ev = 0.0
		self.cas = 0.0


	def getPackageID(self) -> int:
		return self.packageID


	def getClassList(self) -> list:
		return self.classList


	def getName(self) -> str:
		return self.name


	def getMaxDIT(self) -> str:
		return self.maxDIT


	def getLcom(self) -> float:
		return 	self.lcom


	def getEval(self) -> float:
		return self.ev


	def getCas (self) -> float:
		return self.cas
		
	def setPackageID(self, newPackageID: int):
		self.packageID = newPackageID


	def setClassList(self, newClassList: list):
		self.classList = newClassList


	def setLcom(self, newLcom:float):
		self.lcom = newLcom


	def addClass(self, classID: int):
		if self.containClass(classID) == False:
			self.classList.append(classID)


	def containClass(self, classID: int) -> bool:
		if (classID in self.classList):
			return True
		return False


	def updateMaxDIT(self, itd: int):
		if itd > self.maxDIT:
			self.maxDIT = itd


	def evaluate(self, cList: list):
		ev = 0.0
		self.__calculateCas(cList)

		# Class evaluation average = 50%
		ev += self.cas * 0.5

		# LCOM = 35%
		LIMIT_LCMO = 0.5
		if self.lcom < LIMIT_LCMO: # Stable package
			ev += 0.35
		else: 
			ev += ((LIMIT_LCMO - (self.lcom - LIMIT_LCMO)) / LIMIT_LCMO) * 0.35

		# MaxDIT = 15%
		LIMIT_DIT = 5
		if self.maxDIT < LIMIT_DIT:
			ev += 0.15
	
		self.ev = round(ev * 100, 2)


	def __calculateCas (self, cList: list):
		self.cas = 0.0
		for i in self.getClassList():
			self.cas += (cList[i].getEval() / 100)

		self.cas /= len(self.classList)
		self.cas = round(self.cas, 2)

	def print(self):
		s = ""
		s += "\n\n\n\t PackageID " + str(self.packageID)
		s += "\n\t\tName: " + self.name
		s += "\n\t\tClass List: " + str(self.classList)
		s += "\n\t\tMaximum DIT (Inheritance Tree Depth): " + str(self.maxDIT)
		s += "\n\t\tLCOM (Lack of Cohesion): " + str(self.lcom)
		print(s)

