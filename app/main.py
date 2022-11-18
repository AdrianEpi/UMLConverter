# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-18 18:30:20
#   @Description:        ...



import ast
import inspect
from modules.ast_module.line import Line
from modules.file_module.file import File
from modules.file_module.searcher import Searcher
from modules.ast_module.pyAST import PyAST



filename = "testclass.py"
file = File(filename)


myAst = ast.dump(ast.parse(file.getData()), annotate_fields=True, include_attributes=False, indent=4)
l = myAst.split("\n")
ns = []
for i in range(len(l)):
	ns.append(Line(l[i]))
	print(str(i) + "    " + l[i])

tree = PyAST()
tree.generateTree(ns)
tree.print()























# # filename = "../samples/Simple_Samples/AccessModifiers/Private/main.py"
# # file = File(filename)


# # myAst = ast.dump(ast.parse(file.getData()), annotate_fields=True, include_attributes=False, indent=4)
# # l = myAst.split("\n")

# #path = "./"
# path = "../samples/Simple_Samples/AccessModifiers/Private"
# ext = ".py"
# s = Searcher()
# files = s.lookForFiles(path, ext)
# #print(l)
# l = []
# for i in files:
# 	f = File(i)
# 	classAST = ast.dump(ast.parse(f.getData()), annotate_fields=True, include_attributes=False, indent=4)
# 	l = classAST.split("\n")
# 	print("\n\n\n")
# 	print(classAST)
# 	# parser = ast.parse(f.getData(), type_comments=False)
# 	# print(ast.iter_fields(parser))
# 	# for k in ast.walk(parser):
# 	# 	for j in ast.iter_fields(k):
# 	# 		print(j)

# # def generateTree(l:list) -> Line:
# # 	tmpTree = []
# # 	tree = []
# # 	for i in l:
# # 		tmpTree.append(Line(i))

# # 	tree.append(Line("root"))
# # 	for i in range(len(tmpTree)):
# # 		print(i)


# # generateTree(l)




# # for i in l:
# # 	tmp = Line(i)
# # 	#print(tmp.getIndentation())
# # 	print(tmp.getData())
# # 	#print(tmp.getRawData())
# # 	#print("\n")

# # #print(myAst)

