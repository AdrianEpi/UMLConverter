# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metric.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:27:34
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:15:21
#   @Description:        This file describes the metrics

from app.modules.metric_module.metricClass import MetricClass
from app.modules.metric_module.metricPackage import MetricPackage

class Metric:
	"""
	This class describes a metric object.
	"""

	classList: list
	packageList: list
	nodeList: list
	percentages: dict

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		self.classList = []
		self.packageList= []
		self.nodeList = []
		self.percentages = {}


	def getClassList(self) -> list:
		"""
		Gets the class list.

		:returns:   The class list.
		:rtype:     list
		"""
		return self.classList

	
	def getPackageList(self) -> list:
		"""
		Gets the package list.

		:returns:   The package list.
		:rtype:     list
		"""
		return self.packageList

	
	def getPercentajes(self) -> dict:
		"""
		Gets the percentajes.

		:returns:   The percentajes.
		:rtype:     dict
		"""
		return self.percentages


	def setClassList(self, l: list):
		"""
		Sets the class list.

		:param      l:    The new value
		:type       l:    list
		"""
		self.classList = l


	def setClassList(self, l: list):
		"""
		Sets the class list.

		:param      l:    The new value
		:type       l:    list
		"""
		self.classList = l


	def setPackageList(self, l: list):
		"""
		Sets the package list.

		:param      l:    The new value
		:type       l:    list
		"""
		self.packageList = l


	def setPercentages(self, d: dict):
		"""
		Sets the percentages.

		:param      d:    The new value
		:type       d:    dict
		"""
		self.percentages = d


	def addNode(self, node):
		"""
		Adds a node.

		:param      node:       The node
		:type       node:       PythonNode

		:raises     TypeError:  { exception_description }
		"""
		if ('name' in node) and ('package' in node) and ('inheritance' in node):
			self.nodeList.append(node)
		else:
			raise TypeError("Error in Metic.addNode(), not valid node.")

	
	def generateMetrics(self, dic: dict):
		"""
		Generates the metrics

		:param      dic:  The dic with imput data
		:type       dic:  dict
		"""
		self.percentages = dic
		packageName = []
		className = []
		includes = []
		for i in self.nodeList:
			if i['package'] not in packageName:
				newMetricPackage = MetricPackage(len(packageName), i['package'])
				packageName.append(i['package'])
				self.packageList.append(newMetricPackage)

			if i['name'] not in className:
				newMetricClass = MetricClass(len(className), i['name'])
				className.append(i['name'])
				includes.append(i['includes'])
				if len(i['inheritance']) > 0:
					newMetricClass.setInheritance(i['inheritance'])
				newMetricClass.setPackageID(packageName.index(i['package']))
				newMetricClass.setNLines(i['nLines'])
				newMetricClass.setCodeLines(i['codeLines'])
				newMetricClass.setCommentLines(i['commentLines'])
				self.classList.append(newMetricClass)
		

		# Class Inheritance and Children & Packages Classes 
		classID = 0
		for i in self.classList:
			# Add class to package
			self.packageList[i.getPackageID()].addClass(i.getClassID())
			
			# Change inheritance to classID instead of names
			inh = []
			for j in i.getInheritance():
				if (j in className):
					inh.append(className.index(j))
			self.classList[classID].setInheritance(inh)

			# Add this class as children of all the inherited ones
			for j in i.getInheritance():
				self.classList[j].addChild(classID)

			classID += 1

		# Includes
		for i in range(len(includes)):
			for j in includes[i]:
				if j in className:
					self.classList[className.index(j)].addInclude(i)

		self.__generateNOC()
		self.__generateInclusionAndCC()
		self.__generateLCOM()
		for i in range(len(self.classList)):
			self.classList[i].calculateCCD()
			self.classList[i].evaluate(dic = dic)
		for i in range(len(self.packageList)):
			self.packageList[i].evaluate(self.classList, dic = dic)


	def __generateNOC(self):
		"""
		Generates the NOC list
		"""
		for i in range(len(self.classList)):
			finish = False
			noc = self.classList[i].getChildren()
			start = 0
			itd = 1
			while finish == False:
				nocSize = len(noc)
				finish = True
				for j in range(start, nocSize, 1):
					for k in self.classList[j].getChildren():
						if k not in noc:
							finish = False
							noc.append(k)
				if finish == False:
					itd += 1
				start = nocSize
			if len(noc) > 0:
				for j in range(len(self.packageList)):
					if self.classList[i].getPackageID() == self.packageList[j].getPackageID():
						self.packageList[j].updateMaxDIT(itd)

			self.classList[i].setNoc(noc)


	def __generateInclusionAndCC(self):
		"""
		Generates the inclusion and class coupling lists
		"""
		for i in self.classList:
			tmpCBO = 0
			id = i.getClassID()
			for j in self.classList:
				if (id != j.getClassID()) and (id in j.getInclude()):
					tmpCBO += 1
					self.classList[id].addInclusion(j.getClassID())
			self.classList[id].setCBO(tmpCBO)


	def __generateLCOM(self):
		"""
		Generates the lack of cohesion in methods
		"""
		for i in self.packageList:
			lcom = 0.0
			ce = []
			ca = []
			for j in i.getClassList():
				for k in self.classList[j].getInclusion():
					if (self.classList[k].getClassID() not in i.getClassList()) and (self.classList[k].getClassID() not in ce):
						ce.append(self.classList[k].getClassID())
						
				for k in self.classList[j].getInclude():
					if (self.classList[k].getClassID() not in i.getClassList()) and (self.classList[k].getClassID() not in ca):
						ca.append(self.classList[k].getClassID())
						
			ca = len(ca)
			ce = len(ce)
			if ((ca + ce) != 0):
				lcom = float(ce / (ca + ce))
				self.packageList[i.getPackageID()].setLcom(lcom)


