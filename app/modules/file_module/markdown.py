# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               markdown.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-08 12:10:41
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-18 11:10:20
#   @Description:        This files generates the markdown version of the output

from app.modules.metric_module.metric import Metric

import os
import sys


class Markdown():
	"""
	This class describes a markdown for the project output.
	"""

	appPath: str
	banner: str
	data: str
	projectName: str
	imageUML: str
	metrics: Metric


	def __init__(self, path: str, metrics, theme = '_none_', projectName = 'UMLConverter Project'):
		"""
		Constructs a new instance.

		:param      path:         The path
		:type       path:         str
		:param      metrics:      The metrics
		:type       metrics:      Metric object
		:param      theme:        The theme
		:type       theme:        str
		:param      projectName:  The project name
		:type       projectName:  str
		"""
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
		"""
		Generates the markdown

		:returns:   String with the markdown code
		:rtype:     str
		"""
		s = self.__header()
		s += self.__index()
		s += self.__classDiagram()
		s += self.__packageInformation()
		s += self.__metrics()
		return s


	def __header(self) -> str:
		"""
		Generates the header

		:returns:   String with the markdown header code
		:rtype:     str
		"""
		s = '<img align="middle" width="100%" height="300" src="' + self.banner + '">'
		s += "\n\n# " + self.projectName
		return s


	def __index(self) -> str:
		"""
		Generates the index

		:returns:   String with the markdown index code
		:rtype:     str
		"""
		s = '\n\n## **Index**\n'
		s += '\n1. [Class Diagram](#id1)'
		s += '\n2. [Package Information](#id2)'
		s += '\n3. [Metrics](#id3)'
		s += '\n4. [Metrics Tables](#id4)'
		s += '\n5. [Metrics Explanation](#id5)'
		s += '\n\n***\n\n'
		return s

	
	def __packageInformation(self) -> str:
		"""
		Generates the packege information

		:returns:   String with the markdown packege information code
		:rtype:     str
		"""
		s = '\n## Package Information<a name="id2"></a>\n'
		for i in self.metrics.getPackageList():
			s += '\n#### *' + i.getName() + '*'
			for j in i.getClassList():
				s += '\n* ' + self.metrics.getClassList()[j].getName()
			s += '\n\n'

		s += '***\n\n'
		return s	


	def __classDiagram(self) -> str:
		"""
		Generates the UML class diagram code

		:returns:   String with the markdown UML class diagram code
		:rtype:     str
		"""
		s = '\n## Class Diagram<a name="id1"></a>\n'
		s += '\n<img align="middle" width="100%" src="' + self.imageUML + '">'
		s += '\n\n *Legend*\n'
		s += '\n<img align="middle" src="' + self.legend + '">'
		s += '\n\n***\n\n'
		return s


	def __metrics(self) -> str:
		"""
		Generates the metrics code

		:returns:   String with the markdown metrics code
		:rtype:     str
		"""
		s = '\n## Metrics<a name="id3"></a>\n'
		s += '---'
		s += self.__metricsTables()
		s += self.__metricsExplanation()
		s += '\n\n***\n\n'
		return s


	def __metricsTables(self) -> str:
		"""
		Generates the metrics table

		:returns:   String with the markdown metrics table code
		:rtype:     str
		"""
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
		s += '\n| Name | Class Ammount | DIT | LCOM | CAS | Score |'
		s += '\n| -- | -- | -- | -- | -- | -- |'
		for i in self.metrics.getPackageList():
			s += '\n| ' + str(i.getName())
			s += ' | ' + str(len(i.getClassList()))
			s += ' | ' + str(i.getMaxDIT())
			s += ' | ' + str(i.getLcom())
			s += ' | ' + str(i.getCas() * 100) + '%'
			s += ' | ' + str(i.getEval()) + '% |'

		s += '\n\n***\n\n'
		return s
		

	def __metricsExplanation(self) -> str:
		"""
		Generates the metrics explanation

		:returns:   String with the markdown metrics explanation code
		:rtype:     str
		"""
		s = '\n\n## Metrics Explanation<a name="id5"></a>\n'
		s += '\n### *Class Metrics*\n'
		s += '\n* **NOC**: A class\'s *number of children* (NOC) metric simply measures the number of immediate descendants of the class.'
		s += '\n* **CCD**: A class\'s *code comments density* (CCD) metric simply measures the ratio of comment lines per code lines.'
		s += '\n* **CBO**: The *coupling between object classes* (CBO) metric represents the number of classes coupled to a given class (efferent couplings, Ce). This coupling can occur through method calls, field accesses, inheritance, arguments, return types, and exceptions.'
		s += '\n* **Score**: The *score* of a class is calculated using ' + str(self.metrics.getPercentajes()['CBO']) + '% CBO + ' + str(self.metrics.getPercentajes()['CCD']) + '% CCD + ' + str(self.metrics.getPercentajes()['NOC']) + '% NOC making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.'

		s += '\n\n### *Package Metrics*\n'
		s += '\n* **DIT**: The *depth of inheritance tree* (DIT) metric provides for each class a measure of the inheritance levels from the object hierarchy top, excluding languages objects (Class, ABC, Object, BasicObject...).'
		s += '\n* **LCOM**: A class\'s *lack of cohesion in methods* (LCOM) metric counts the sets of methods in a class that are not related through the sharing of some of the class\'s fields.'
		s += '\n* **CAS**: The class average evaluation.'
		s += '\n* **Score**: The *score* of a package is calculated using ' + str(self.metrics.getPercentajes()['CAS']) + '% Average class score + ' + str(self.metrics.getPercentajes()['LCOM']) + '% LCOM + ' + str(self.metrics.getPercentajes()['DIT']) + '% DIT making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.'
		return s