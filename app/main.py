# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-13 16:57:42
#   @Description:        ...



import ast
import inspect
from modules.ast_module.node import Node

with open('../samples/Simple_Samples/AccessModifiers/Private/main.py', 'r') as f:
    lines = f.readlines()
f.close()

string = ""
for i in lines:
	string = string + i


myAst = ast.dump(ast.parse(string), annotate_fields=True, include_attributes=False, indent=4)
l = myAst.split("\n")

for i in l:
	tmp = Node(i)
	#print(tmp.getIndentation())
	print(tmp.getData())
	#print(tmp.getRawData())
	#print("\n")

#print(myAst)