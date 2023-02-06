# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metric.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:27:34
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-06 12:19:07
#   @Description:        ...

from app.modules.metric_module.metricClass import MetricClass
from app.modules.metric_module.metricPackage import MetricPackage

class Metric:

	classList: list
	packageList: list
	nodeList: list

	def __init__(self):
		self.classList = []
		self.packageList= []
		self.nodeList = []

	def getClassList(self) -> list:
		return self.classList

	def getPackageList(self) -> list:
		return self.packageList

	def addNode(self, node):
		if ('name' in node) and ('package' in node) and ('inheritance' in node):
			self.nodeList.append(node)
		else:
			raise TypeError("Error in Metic.addNode(), not valid node.")

	def generateMetrics(self):
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

		# generateClassNoc