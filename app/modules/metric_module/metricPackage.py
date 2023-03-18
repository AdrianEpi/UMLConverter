# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metricPackage.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:10:05
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:20:35
#   @Description:        This file describes the metrics for a package


class MetricPackage:
	"""
	This class describes a metric package.
	"""

	packageID: int 		# Package ID
	classList: list 	# List of classes IDs contained by the package
	name: str 			# Package name
	maxDIT: int 		# Maximum Depth of Inheritance Tree
	lcom: float			# Lack of cohesion in methods
	ev: float 			# Evaluation of the package (0-100)%
	cas: float 			# Evaluation of the class average


	def __init__(self, id: int, pname: str):
		"""
		Constructs a new instance.

		:param      id:     The identifier
		:type       id:     int
		:param      pname:  The pname
		:type       pname:  str
		"""
		self.packageID = id
		self.classList = []
		self.name = pname
		self.maxDIT = 0
		self.lcom = 0.0
		self.ev = 0.0
		self.cas = 0.0


	def getPackageID(self) -> int:
		"""
		Gets the package id.

		:returns:   The package id.
		:rtype:     int
		"""
		return self.packageID


	def getClassList(self) -> list:
		"""
		Gets the class list.

		:returns:   The class list.
		:rtype:     list
		"""
		return self.classList


	def getName(self) -> str:
		"""
		Gets the name.

		:returns:   The name.
		:rtype:     str
		"""
		return self.name


	def getMaxDIT(self) -> str:
		"""
		Gets the maximum dit.

		:returns:   The maximum dit.
		:rtype:     str
		"""
		return self.maxDIT


	def getLcom(self) -> float:
		"""
		Gets the lcom.

		:returns:   The lcom.
		:rtype:     float
		"""
		return 	self.lcom


	def getEval(self) -> float:
		"""
		Gets the eval.

		:returns:   The eval.
		:rtype:     float
		"""
		return self.ev


	def getCas (self) -> float:
		"""
		Gets the cas.

		:returns:   The cas.
		:rtype:     float
		"""
		return self.cas
		
	def setPackageID(self, newPackageID: int):
		"""
		Sets the package id.

		:param      newPackageID:  The new package id
		:type       newPackageID:  int
		"""
		self.packageID = newPackageID


	def setClassList(self, newClassList: list):
		"""
		Sets the class list.

		:param      newClassList:  The new class list
		:type       newClassList:  list
		"""
		self.classList = newClassList


	def setLcom(self, newLcom:float):
		"""
		Sets the lcom.

		:param      newLcom:  The new lcom
		:type       newLcom:  float
		"""
		self.lcom = newLcom


	def addClass(self, classID: int):
		"""
		Adds a class.

		:param      classID:  The class id
		:type       classID:  int
		"""
		if self.containClass(classID) == False:
			self.classList.append(classID)


	def containClass(self, classID: int) -> bool:
		"""
		Check if the package contains a class

		:param      classID:  The class id
		:type       classID:  int

		:returns:   True if the class is contained by the package, false otherwise
		:rtype:     bool
		"""
		if (classID in self.classList):
			return True
		return False


	def updateMaxDIT(self, itd: int):
		"""
		Updates maxDIT

		:param      itd:  The itd
		:type       itd:  int
		"""
		if itd > self.maxDIT:
			self.maxDIT = itd


	def evaluate(self, cList: list, dic: dict):
		"""
		Evaluates the package metrics with the percentages given in dic

		:param      cList:  The list
		:type       cList:  list
		:param      dic:    The dic
		:type       dic:    dict
		"""
		ev = 0.0
		self.__calculateCas(cList)

		# CAS
		ev += self.cas * (dic['CAS'] / 100)

		# LCOM
		LIMIT_LCMO = 0.5
		if self.lcom < LIMIT_LCMO: # Stable package
			ev += 0.35
		else: 
			ev += ((LIMIT_LCMO - (self.lcom - LIMIT_LCMO)) / LIMIT_LCMO) * (dic['LCOM'] / 100)

		# MaxDIT
		LIMIT_DIT = 5
		if self.maxDIT < LIMIT_DIT:
			ev += (dic['DIT'] / 100)
	
		self.ev = round(ev * 100, 2)


	def __calculateCas (self, cList: list):
		"""
		Calculates the cas.

		:param      cList:  The list
		:type       cList:  list
		"""
		self.cas = 0.0
		for i in self.getClassList():
			self.cas += (cList[i].getEval() / 100)

		self.cas /= len(self.classList)
		self.cas = round(self.cas, 2)


	def print(self):
		"""
		Prints the metric class information
		"""
		s = ""
		s += "\n\n\n\t PackageID " + str(self.packageID)
		s += "\n\t\tName: " + self.name
		s += "\n\t\tClass List: " + str(self.classList)
		s += "\n\t\tMaximum DIT (Inheritance Tree Depth): " + str(self.maxDIT)
		s += "\n\t\tLCOM (Lack of Cohesion): " + str(self.lcom)
		print(s)

