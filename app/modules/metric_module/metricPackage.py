# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricPackage.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:10:05
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-03 22:25:36
#   @Description:        ...


class MetricPackage:

	packageID: int
	classList: list


	def __init__(self, id):
		self.packageID = id
		self.classList = []


	def getPackageID(self) -> int:
		return self.packageID


	def getClassList(self) -> list:
		return self.classList


	def setPackageID(self, newPackageID: int):
		self.packageID = newPackageID


	def setClassList(self, newClassList: list):
		self.classList = newClassList


	def addClass(self, classID: int):
		if self.containClass(classID) == False:
			self.classList.append(classID)


	def containClass(self, classID: int) -> bool:
		if (classID in self.classList):
			return True
		return False
