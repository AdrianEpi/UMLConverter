# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-14 09:43:46
#   @Description:        ...



import ast
import inspect
from modules.ast_module.node import Node
from modules.file_module.file import File
from modules.file_module.searcher import Searcher


filename = "../samples/Simple_Samples/AccessModifiers/Private/main.py"
file = File(filename)


myAst = ast.dump(ast.parse(file.getData()), annotate_fields=True, include_attributes=False, indent=4)
l = myAst.split("\n")

path = "./"
ext = ".py"
s = Searcher()
l = s.lookForFiles(path, ext)
#print(l)

for i in l:
	f = File(i)
	classAST = ast.dump(ast.parse(f.getData()), annotate_fields=True, include_attributes=False, indent=4)
	print("\n\n\n")
	print(classAST)
	
# for i in l:
# 	tmp = Node(i)
# 	#print(tmp.getIndentation())
# 	print(tmp.getData())
# 	#print(tmp.getRawData())
# 	#print("\n")

# #print(myAst)

