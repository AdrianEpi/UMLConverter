# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               interface.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-24 19:15:15
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-02 08:53:01
#   @Description:        ...

from app.modules.utils import LANGUAGES, UMLTHEMES

import easygui
import sys

from tkinter import *
from PIL import ImageTk,Image



#root.image("./img/logo/267x150.png")
#root.iconbitmap(default = './img/icon/25x25.ico')


#root.mainloop()
#root.create_image(20,20, anchor=NW, image=PhotoImage(file="./img/logo/267x150.png"))  
#root.destroy()
#root.iconify()

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
		
		def close(item):
			root.destroy()
			return True

		root = Tk() 
		root.title("UMLConverter")
		root.iconbitmap(default = './img/icon/25x25.ico')
		root.geometry("500x220")
		img = ImageTk.PhotoImage(Image.open("./img/logo/267x150.png"))

		Button(root, image=img, text="AA", command =lambda: close(root)).pack()
		Button(root, text="Start ", command = lambda: close(root)).place(x=240, y=180)
		root.mainloop()

		


		#root.mainloop()
		#easygui.msgbox("\n\n\n\t\tWelcome to UMLCoverter!")


	def porjectInformationInterface(self) -> list:
		"""
		Promps an interface where ask the user for the esential data for the program, such as directory, output, language...

		:returns:   A list with the language, input path for files and path where the output is going to be stored.
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
		path = easygui.diropenbox(title)
		if path == None:
			sys.exit(0)
		return path


	def projectExcludedFiles(self, fileList: list) -> list:
		excluded = easygui.multchoicebox("Select files which you want to exclude in class diagram", "Exclude files", fileList)
		return excluded


	def selectFromList(self, l: list, msg: str, title: str) -> str:
		choice = easygui.choicebox(msg, "UMLConverter " + title, l)
		if (choice == None):
			sys.exit(0)
		return choice


	def yesNoQuestion(self, msg: str) -> str:
		choice = easygui.buttonbox(msg, choices = ["Yes", "No"])
		if (choice == None):
			sys.exit(0)
		return choice


	def advancedMenu(self, fileList: list, excludedFiles = [], output = "", theme = "_none_", packages = False) -> dict:
		image = "./img/logo/267x150.png"
		msg = "Do you want to finish config and start building?"
		choices = ["Build", "Exclude Files", "Choose Theme", "Packages", "Exit"]
		reply = easygui.buttonbox(msg, choices = choices, image = image)
		#reply = easygui.buttonbox(msg, choices = choices)


		if reply == "Build":
			result = {
				"ExcludedFiles": excludedFiles,
				"Theme": theme,
				"Packages": packages
			}
			return result

		elif reply == "Exclude Files":
			excludedFiles = self.projectExcludedFiles(fileList)

		elif reply == "Choose Theme":
			theme = self.selectFromList(msg = "Select a theme from the list:", title = "Themes", l = UMLTHEMES)

		elif reply == "Packages":
			packages = self.yesNoQuestion(msg = "Do you want to generate pacakges in the diagram?")

		elif reply == "Exit":
			sys.exit(0)
		
		return self.advancedMenu(fileList = fileList, excludedFiles = excludedFiles, output = output, theme = theme, packages = packages)
	
