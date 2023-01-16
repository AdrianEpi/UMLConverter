# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               interface.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-24 19:15:15
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-16 11:17:02
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
		path = easygui.diropenbox("Select project folder")	
		if path == None:
			sys.exit(0)

		easygui.msgbox("\n\n\tYou chose: " + str(path) + "\n\n\tSelect directory to save the output", title)
		output = easygui.diropenbox("Select output folder")	
		if output == None:
			sys.exit(0)
			
		return[language, path, output]
