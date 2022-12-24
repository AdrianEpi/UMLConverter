# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-24 09:22:08
#   @Description:        ...


# from app.modules.uml_module.UMLConverter import UMLConverter

# a = UMLConverter()
# a.generateUML()



import easygui
import sys


while 1:
	easygui.msgbox("Hello, world!")

	msg ="What is your favorite flavor?"
	title = "Ice Cream Survey"
	choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
	choice = easygui.choicebox(msg, title, choices)

	# note that we convert choice to string, in case
	# the user cancelled the choice, and we got None.
	easygui.msgbox("You chose: " + str(choice), "Survey Result")

	msg = "Do you want to continue?"
	title = "Please Confirm"
	if easygui.ccbox(msg, title):     # show a Continue/Cancel dialog
		pass  # user chose Continue
	else:
		sys.exit(0)           # user chose Cancel


# import tkinter
# import sys
# import os

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')


# #create main window
# master = tkinter.Tk()
# master.title("tester")
# master.geometry("300x100")


# #make a label for the window
# label1 = tkinter.Label(master, text='Hellooooo')
# # Lay out label
# label1.pack()

# # Run forever!
# master.mainloop()