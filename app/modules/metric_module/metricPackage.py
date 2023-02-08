# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricPackage.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:10:05
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 11:43:42
#   @Description:        ...


class MetricPackage:

	packageID: int
	classList: list
	name: str
	maxITD: int 		# Maximum inheritance tree depth
	lcom: float			# Lack of cohesion in methods


	def __init__(self, id: int, pname: str):
		self.packageID = id
		self.classList = []
		self.name = pname
		self.maxITD = 0
		self.lcom = 0.0


	def getPackageID(self) -> int:
		return self.packageID


	def getClassList(self) -> list:
		return self.classList


	def getName(self) -> str:
		return self.name


	def getLcom(self) -> float:
		return 	self.lcom

		
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


	def updateMaxITD(self, itd: int):
		if itd > self.maxITD:
			self.maxITD = itd


	def print(self):
		s = ""
		s += "\n\n\n\t PackageID " + str(self.packageID)
		s += "\n\t\tName: " + self.name
		s += "\n\t\tClass List: " + str(self.classList)
		s += "\n\t\tMaximum ITD (Inheritance Tree Depth): " + str(self.maxITD)
		s += "\n\t\tLCOM (Lack of Cohesion): " + str(self.lcom)
		print(s)
