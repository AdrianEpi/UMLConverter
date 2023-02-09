# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               markdown.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-08 12:10:41
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 21:32:40
#   @Description:        ...

from app.modules.metric_module.metric import Metric

import os
import sys


class Markdown():

	appPath: str
	banner: str
	data: str
	projectName: str
	imageUML: str
	metrics: Metric


	def __init__(self, path: str, metrics, theme = '_none_', projectName = 'UMLConverter Project'):
		self.appPath = os.path.realpath(__file__)
		self.appPath = self.appPath[0:(len(self.appPath) - 36)]
		if ((sys.platform == 'win32') or (sys.platform == 'cygwin')): # Windows
			self.banner = self.appPath + '\\img\\logo\\banner600x200.png'
			self.legend = self.appPath + '\\img\\legend\\' + theme + '-legend.png'
		else:	# Linux or MacOS
			self.banner = self.appPath + '/img/logo/banner600x200.png'
			self.legend = self.appPath + '/img/legend/' + theme + '-legend.png'
		self.data = ''
		self.projectName = projectName
		self.imageUML = path + 'projectUML.png'
		self.metrics = metrics

	def generateMarkdown(self) -> str:
		s = self.__header()
		s += self.__index()
		s += self.__classDiagram()
		s += self.__packageInformation()
		s += self.__metrics()
		return s


	def __header(self) -> str:
		s = '<img align="middle" width="100%" height="300" src="' + self.banner + '">'
		s += "\n\n# " + self.projectName
		return s


	def __index(self) -> str:
		s = '\n\n## **Index**\n'
		s += '\n1. [Class Diagram](#id1)'
		s += '\n2. [Package Information](#id2)'
		s += '\n3. [Metrics](#id3)'
		s += '\n4. [Metrics Tables](#id4)'
		s += '\n5. [Metrics Explanation](#id5)'
		s += '\n\n***\n\n'
		return s

	
	def __packageInformation(self) -> str:
		s = '\n## Package Information<a name="id2"></a>\n'
		for i in self.metrics.getPackageList():
			s += '\n#### *' + i.getName() + '*'
			for j in i.getClassList():
				s += '\n* ' + self.metrics.getClassList()[j].getName()
			s += '\n\n'

		s += '***\n\n'
		return s	

	def __classDiagram(self) -> str:
		s = '\n## Class Diagram<a name="id1"></a>\n'
		s += '\n<img align="middle" width="100%" src="' + self.imageUML + '">'
		s += '\n\n *Legend*\n'
		s += '\n<img align="middle" src="' + self.legend + '">'
		s += '\n\n***\n\n'
		return s

	def __metrics(self) -> str:
		s = '\n## Metrics<a name="id3"></a>\n'
		s += '---'
		s += self.__metricsTables()
		s += self.__metricsExplanation()
		s += '\n\n***\n\n'
		return s

	def __metricsTables(self) -> str:
		s = '\n\n## Metrics Tables<a name="id4"></a>\n'
		s += '\n### *Class Table*\n'
		s += '\n| Name | Package | NOC | CodeLines | CommentLines | CCD | CBO | Score |'
		s += '\n| -- | -- | -- | -- | -- | -- | -- | -- |'
		for i in self.metrics.getClassList():
			s += '\n| ' + str(i.getName())
			s += ' | ' + str(self.metrics.getPackageList()[i.getPackageID()].getName())
			s += ' | ' + str(len(i.getNoc()))
			s += ' | ' + str(i.getCodeLines())
			s += ' | ' + str(i.getCommentLines())
			s += ' | ' + str(i.getCcd())
			s += ' | ' + str(i.getCBO())
			s += ' | ' + str(i.getEval()) + '% |'

		s += '\n\n### *Package Table*\n'
		s += '\n| Name | Class Ammount | DIT | LCOM | Score |'
		s += '\n| -- | -- | -- | -- | -- |'
		for i in self.metrics.getPackageList():
			s += '\n| ' + str(i.getName())
			s += ' | ' + str(len(i.getClassList()))
			s += ' | ' + str(i.getMaxDIT())
			s += ' | ' + str(i.getLcom())
			s += ' | ' + str(i.getEval()) + '% |'

		s += '\n\n***\n\n'
		return s
		


	def __metricsExplanation(self) -> str:
		s = '\n\n## Metrics Explanation<a name="id5"></a>\n'
		s += '\n### *Class Metrics*\n'
		s += '\n* **NOC**: A class\'s *number of children* (NOC) metric simply measures the number of immediate descendants of the class.'
		s += '\n* **CCD**: A class\'s *code comments density* (CCD) metric simply measures the ratio of comment lines per code lines.'
		s += '\n* **CBO**: The *coupling between object classes* (CBO) metric represents the number of classes coupled to a given class (efferent couplings, Ce). This coupling can occur through method calls, field accesses, inheritance, arguments, return types, and exceptions.'
		s += '\n* **Score**: The *score* of a class is calculated using 42.5% CBO + 42.5% CCD + 15% NOC making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.'

		s += '\n\n### *Package Metrics*\n'
		s += '\n* **DIT**: The *depth of inheritance tree* (DIT) metric provides for each class a measure of the inheritance levels from the object hierarchy top, excluding languages objects (Class, ABC, Object, BasicObject...).'
		s += '\n* **LCOM**: A class\'s *lack of cohesion in methods* (LCOM) metric counts the sets of methods in a class that are not related through the sharing of some of the class\'s fields.'
		s += '\n* **Score**: The *score* of a package is calculated using 50% Average class score + 35% LCOM + 15% DIT making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.'
		return s