# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               metric.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-03 22:27:34
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 13:43:41
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


	def __generateNOC(self):
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
						self.packageList[j].updateMaxITD(itd)

			self.classList[i].setNoc(noc)


	def __generateInclusionAndCC(self):
		for i in self.classList:
			tmpCC = 0
			id = i.getClassID()
			for j in self.classList:
				if (id != j.getClassID()) and (id in j.getInclude()):
					tmpCC += 1
					self.classList[id].addInclusion(j.getClassID())
			self.classList[id].setCc(tmpCC)


	def __generateLCOM(self):
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
			lcom = float(ce / (ca + ce))
			self.packageList[i.getPackageID()].setLcom(lcom)


