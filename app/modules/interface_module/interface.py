# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               interface.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-24 19:15:15
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-26 12:12:47
#   @Description:        ...

from app.modules.uml_module.translator import LANGUAGES

import easygui
import sys

class Interface:
	"""
	This class describes an interface, it handles the different interfaces of UMLConverter.
	"""

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		pass


	def greet(self):
		"""
		Shows a prompt where greets the user.
		""" 
		easygui.msgbox("\n\n\n\t\tWelcome to UMLCoverter!")


	def porjectInformationInterface(self) -> list:
		"""
		Promps an interface where ask the user for the esential data for the program, such as directory, output, language...

		:returns:   A list with the language, input path for files and path where the output is going to be stored.
		:rtype:     list
		"""
		self.greet()
		msg = "Please select you project language"
		title = "UMLCoverter"
		choices = LANGUAGES
		language = easygui.choicebox(msg, title, choices)
		if (language == None):
			sys.exit(0)

		easygui.msgbox("\n\n\tYou chose: " + str(language) + "\n\n\tSelect project folder", title)
		path = self.selectDirectory("Select project folder")	
		

		easygui.msgbox("\n\n\tYou chose: " + str(path) + "\n\n\tSelect directory to save the output", title)
		output = self.selectDirectory("Select output folder")


		result = {
			"Language": language,
			"ProjectPath": path,
			"OutputPath": output
		}
		return result

	def selectDirectory(self, title: str) -> str:
		path = easygui.diropenbox(title)
		if path == None:
			sys.exit(0)
		return path

	def projectExcludedFiles(self, fileList: list) -> list:
		excluded = easygui.multchoicebox("Select files which you want to exclude in class diagram", "Exclude files", fileList)
		return excluded


	def advancedMenu(self, fileList: list, excludedFiles = [], output = "", theme = "") -> dict:
		#image = "path"
		msg = "Do you want to finish config and start building?"
		choices = ["Build", "Exclude Files", "Choose Theme", "Exit"]
		#reply = buttonbox(msg, image=image, choices=choices)
		reply = easygui.buttonbox(msg, choices=choices)

		if reply == "Build":
			result = {
				"OutputPath": output,
				"ExcludedFiles": excludedFiles,
				"Theme": theme
			}
			return result

		elif reply == "Exclude Files":
			excludedFiles = self.projectExcludedFiles(fileList)

		elif reply == "Theme":
			pass

		elif reply == "Exit":
			sys.exit(0)
		
		return self.advancedMenu(fileList = fileList, excludedFiles = excludedFiles, output = output, theme = theme)
	
