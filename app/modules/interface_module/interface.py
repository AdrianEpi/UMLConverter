# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               interface.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-24 19:15:15
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-25 15:02:34
#   @Description:        ...

from app.modules.uml_module.translator import LANGUAGES

import easygui
import sys

class Interface:

	def __init__(self):
		pass

	def greet(self):
		easygui.msgbox("\n\n\n\t\tWelcome to UMLCoverter!")

	def porjectInformationInterface(self) -> list:
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
