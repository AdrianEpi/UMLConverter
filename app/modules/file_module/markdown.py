# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               markdown.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-08 12:10:41
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 13:53:26
#   @Description:        ...

from app.modules.metric_module.metric import Metric

import os
import sys


class Markdown():

	appPath: str
	banner: str
	data: str
	projectName: str
	classDiagram: str
	metrics: Metric


	def __init__(self, image: str, metrics, projectName = "UMLConverter Project"):
		self.appPath = os.path.realpath(__file__)
		if ((sys.platform == 'win32') or (sys.platform == 'cygwin')): # Windows
			self.banner = self.appPath + '\\img\\logo\\267x150.png'
		else:	# Linux or MacOS
			self.banner = self.appPath + '/img/logo/267x150.png'
		self.data = ''
		self.projectName = projectName
		self.image = image
		self.metrics = metrics

	def generateMarkdown(self) -> str:
		s = self.__header()
		s += self.__index()
		s += self.__metrics()
		return s

	def __index(self) -> str:
		s = '\n## **Index**'
		s += '\n---'
		s += '\n1. [Class Diagram](#id1)'
		s += '\n2. [Metrics](#id2)'
		s += '\n3. [Metrics Tables](#id3)'
		s += '\n4. [Metrics Evaluation](#id4)'
		s += '\n5. [Metrics Explanation](#id5)'
		s += '\n\n***\n\n'
		return s

	def __header(self) -> str:
		s = '<img align="middle" width="100%" height="300" src="' + self.banner + '">'
		s += "\n# " + self.projectName
		return s

	def __classDiagram(self) -> str:
		s = '\n## Class Diagram<a name="id1"></a>\n'
		s += '---'
		s += '<img align="middle" width="100%" src="' + self.classImage + '">'
		s += '\n\n***\n\n'
		return s

	def __metrics(self) -> str:
		s = '\n## Metrics<a name="id2"></a>\n'
		s += '---'
		s += self.__metricsTables()
		s += self.__metricsEvaluation()
		s += self.__metricsExplanation()
		s += '\n\n***\n\n'
		return s

	def __metricsTables(self) -> str:
		s += '\n\n## Metric Tabless<a name="id3"></a>\n'
		s += '\n#### Class Tables\n'
		s += '\n| Name | Package | Children | NOC | CodeLines | CommentLines | CCD | CC | Evaluation|'
		s += '\n| -- | -- | -- | -- | -- | -- | -- | -- | -- |'
		for i in self.metrics.getClassList():
			s += '\n| ' + str(i.getName())
			s += ' | ' + str(self.metrics.getPackageList()[i.getPackageID()].getName())
			s += ' | ' + str(len(i.getChildren()))
			s += ' | ' + str(len(i.getNoc()))
			s += ' | ' + str(i.getCodeLines())
			s += ' | ' + str(i.getCommentLines())
			s += ' | ' + str(i.getCcd())
			s += ' | ' + str(i.getCc())
			s += ' | ' + 'good' + ' |'
			#s += ' | ' + str(i.getEval()) + ' |'
		return s
		





	def __metricsEvaluation(self) -> str:
		return ""


	def __metricsExplanation(self) -> str:
		return ""