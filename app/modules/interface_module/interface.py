# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               interface.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-24 19:15:15
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-03-19 08:26:51
#   @Description:        This file describes the interface of the umlConverter and it's utilities

from app.modules.utils import LANGUAGES, UMLTHEMES

import easygui
import sys
import os

from tkinter import *
from PIL import ImageTk, Image


class Interface:
	"""
	This class describes an interface, it handles the different interfaces of
	UMLConverter.
	"""
	iconPath: str
	logoPath: str

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		path = os.path.realpath(__file__)
		path = path[:(len(path) - 42)]
		if ((sys.platform == "win32") or (sys.platform == "cygwin")): # Windows
			self.iconPath = path + "\\img\\icon\\25x25.ico"
			self.logoPath = path + "\\img\\logo\\267x150.png"
		else:	# Linux or MacOS
			self.iconPath = path + "/img/icon/25x25.ico"
			self.logoPath = path + "/img/logo/267x150.png"


	def greet(self):
		"""
		Shows a prompt where greets the user.
		""" 

		def close(item):
			"""
			Kills the greet process
			
			:param      item:  The item
			:type       item:  tkinter
			"""
			root.destroy()

		root = Tk() 
		root.title("UMLConverter")
		root.iconbitmap(default = self.iconPath)
		root.geometry("500x220")
		img = ImageTk.PhotoImage(Image.open(self.logoPath))
		Button(root, image=img, text="AA", command =lambda: close(root)).pack()
		Button(root, text="Start ", command = lambda: close(root)).place(x=240, y=180)
		root.mainloop()
		

	def porjectInformationInterface(self) -> list:
		"""
		Promps an interface where ask the user for the esential data for the
		program, such as directory, output, language...
		
		:returns:   A list with the language, input path for files and path
					where the output is going to be stored.
		:rtype:     list
		"""
		self.greet()
		language = self.selectFromList(msg = "Please select you project language", title = "Language", l = LANGUAGES)
		path = self.selectDirectory("Select project folder")	
		output = self.selectDirectory("Select output folder")

		result = {
			"Language": language,
			"ProjectPath": path,
			"OutputPath": output
		}
		return result


	def selectDirectory(self, title: str) -> str:
		"""
		Opens a selectionbox for choosing directory

		:param      title:  The title
		:type       title:  str

		:returns:   The directory path
		:rtype:     str
		"""
		path = easygui.diropenbox(title)
		if path == None:
			sys.exit(0)
		return path


	def multiChoiceSelection(self, title: str, text: str, l: list) -> list:
		"""
		Opens a choicebox for multiselection items from list
		
		:param      l:  The file list
		:type       l:  list
		
		:returns:   List with selected items
		:rtype:     list
		"""
		excluded = easygui.multchoicebox(text, title, l)
		return excluded


	def selectFromList(self, l: list, msg: str, title: str) -> str:
		"""
		Opens a list in which user must select an option

		:param      l:      list of options
		:type       l:      list
		:param      msg:    The message
		:type       msg:    str
		:param      title:  The title
		:type       title:  str

		:returns:   selected option
		:rtype:     str
		"""
		choice = easygui.choicebox(msg, "UMLConverter " + title, l)
		if (choice == None):
			sys.exit(0)
		return choice


	def yesNoQuestion(self, msg: str) -> str:
		"""
		Asks the user a yes or no question

		:param      msg:  The message
		:type       msg:  str

		:returns:   answer of the user
		:rtype:     str
		"""
		choice = easygui.buttonbox(msg, choices = ["Yes", "No"])
		if (choice == None):
			sys.exit(0)
		return choice


	def advancedMenu(self, fileList: list, excludedFiles = [], output = "", theme = "_none_", packages = False, metrics =  {}) -> dict:
		"""
		Shows the advanced menu for umlconverter

		:param      fileList:       The file list
		:type       fileList:       list
		:param      excludedFiles:  The excluded files
		:type       excludedFiles:  Array
		:param      output:         The output
		:type       output:         str
		:param      theme:          The theme
		:type       theme:          str
		:param      packages:       The packages
		:type       packages:       bool

		:returns:   object with advanced options
		:rtype:     dict
		"""
		msg = "Do you want to finish config and start building?"
		choices = ["Build", "Exclude Files", "Choose Theme", "Group in Packages", "Modify Metrics", "Exit"]
		reply = easygui.buttonbox(msg, choices = choices, image = self.logoPath)
		if reply == "Build":
			result = {
				"ExcludedFiles": excludedFiles,
				"Theme": theme,
				"Packages": packages,
				"Metrics": metrics
			}
			return result

		elif reply == "Exclude Files":
			excludedFiles = self.multiChoiceSelection("Select files which you want to exclude in class diagram", "Exclude files", fileList)

		elif reply == "Choose Theme":
			theme = self.selectFromList(msg = "Select a theme from the list:", title = "Themes", l = UMLTHEMES)

		elif reply == "Group in Packages":
			packages = self.yesNoQuestion(msg = "Do you want to generate pacakges in the diagram?")

		elif reply == "Modify Metrics":
			metrics = self.metricsMenu()

		elif reply == "Exit":
			sys.exit(0)
		
		return self.advancedMenu(fileList = fileList, excludedFiles = excludedFiles, output = output, theme = theme, packages = packages, metrics = metrics)
	

	def metricsMenu(self) -> dict:
		"""
		Prompts the metrics menu with the default values.

		:returns:   Dictionary with the metrics set
		:rtype:     dict
		"""
		msg = 'Enter the pertentaje you want to apply to each class metric, remember that NOC + CCD + CBO = 100%'
		fieldNames = ['NOC', 'CCD', 'CBO']
		defaultValues = [15, 42.5, 42.5]
		classMetrics = self.multipleEnterBox(msg = msg, fieldNames = fieldNames, defaultValues = defaultValues, title = "")
		msg = 'Enter the pertentaje you want to apply to each package metric, remember that DIT + LCOM + CAS = 100%'
		fieldNames = ['DIT', 'LCOM', 'CAS']
		defaultValues = [15, 35, 50]
		packageMetrics = self.multipleEnterBox(msg = msg, fieldNames = fieldNames, defaultValues = defaultValues, title = "")
		return {
			'NOC': classMetrics['NOC'],
			'CCD': classMetrics['CCD'],
			'CBO': classMetrics['CBO'],
			'DIT': packageMetrics['DIT'],
			'LCOM': packageMetrics['LCOM'],
			'CAS': packageMetrics['CAS']
		}


	def multipleEnterBox(self, msg: str, fieldNames: list, defaultValues: list, title: str) -> dict:
		"""
		Promps a multiple box interface

		:param      msg:            The message
		:type       msg:            str
		:param      fieldNames:     The field names
		:type       fieldNames:     list
		:param      defaultValues:  The default values
		:type       defaultValues:  list
		:param      title:          The title
		:type       title:          str

		:returns:   Dict with the results of the input data
		:rtype:     dict
		"""
		fieldValues = []
		while 1:
			value = 0
			err = False
			fieldValues = easygui.multenterbox("", title, fieldNames, defaultValues)
			for i, name in enumerate(fieldNames):
				data = fieldValues[i].strip()
				if data == "":
				  easygui.msgbox("{} is a required field.\n\n".format(name))
				  err = True
				else:
					try: 
						num = float(data)
						value += num 
					except ValueError:
						easygui.msgbox("{} must be a number or float.\n\n".format(name))
						err = True

			if value != 100 and err == False:
				easygui.msgbox("The sum of all the fields must be equal to 100%")
			
			if value == 100:
				break

		result = {}
		counter = 0
		for i in fieldNames:
			result[i] = float(fieldValues[counter])
			counter += 1

		return result

