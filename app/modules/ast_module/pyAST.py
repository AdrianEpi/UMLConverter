# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-17 13:08:56
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-17 22:29:56
#   @Description:        ...

from modules.ast_module.pyAST.py import PythonNode

NODETYPES = [
	"Module(",
	"ClassDef(",
	"Import(",
	"ImportFrom(",
	"Assign(",
	"AnnAssign(",
	"AsyncFunctionDef(",
	"FunctionDef(",
	"Return("
]


class PyAST:

	tree: PythonNode()
	dataList: list

	def __init__(self, data: list)
		self.tree .setNodeType("root")
		self.dataList = data


	def generateTree(self, l: list):



	def generateModule(self, pos: int):
		node = PythonNode()
		node.setNodeType("Module")


	def generateClassDef(self, pos: int):
		node = PythonNode()
		node.setNodeType("ClassDef")


	def generateImport(self, pos: int):
		imports = []
		for i in range(pos + 2, len(dataList), 1):
			if "alias(name='" in dataList[i]:
				node = PythonNode()
				node.setNodeType("Import")
				node.setName(self.findName(dataList[i]))
				imports.append(node)
				if ("])," in dataList[i]):
					break
			else:
				raise "Error in PyAST.generateImport() not import name found"
		return imports


	def generateImportFrom(self, pos: int):
		node = PythonNode()
		node.setNodeType("ImportFrom")
		imports = []
		l = dataList[i + 1].split("'")
		#TRY NAMES
		node.setName(l[1]) # Will always be the second format:"  module='XXXXX',"
		for i in range(pos + 3, len(dataList), 1):
			if "alias(name='" in dataList[i]:
				imports.append(self.findName(dataList[i]))
				if ("])," in dataList[i]):
					break
			else:
				raise "Error in PyAST.generateImport() not import name found"
		node.setValue(imports)
		return node


	def generateAssign(self, pos: int):
		assings = []
		for i in range(pos + 2, len(dataList), 1):
			if ("Name(id='" in dataList[i]) and ("', ctx=Store()" in dataList[i]):
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.findName(dataList[i]))
				assings.append(node)
			elif ("value=Constant" in dataList[i]):
				for j in assings:
					j.setValue(self.findValue(dataList[i]))
				break
			else:
				raise "Error in PyAST.generateAssign() not defined structure"
		return assings


	def generateAnnAssign(self, pos: int):
		node = PythonNode()
		node.setNodeType("AnnAssign")
		if "Name(id='" in dataList[pos + 1]:
			node.setName(findName(dataList[pos + 1]))
		else:
			raise "Error in PyAST.generateAnnAssign(), not name found."
		if "annotation=name'" in dataList[pos + 2]:
			node.setValue(findName(dataList[pos + 2]))
		elif "annotation=BoolOp" in dataList[pos + 2]:
			l = []
			for i in range(pos + 2, len(dataList), 1):
				if ("Name(id='" in dataList[i]) and ("', ctx=Store()" in dataList[i]):
					l.append(self.findName(dataList[i]))
				elif ("simple=" in dataList[i]):
					break
				else:
					raise "Error in PyAST.generateAssign() not defined structure"
		else:
			raise "Error in PyAST.generateAnnAssign(), not value found."


	def generateAsyncFunctionDef(self, pos: int):
		node = PythonNode()
		node.setNodeType("AsyncFunctionDef")


	def generateFunctionDef(self, pos: int):
		node = PythonNode()
		node.setNodeType("FunctionDef")


	def generateReturn(self, pos: int):
		node = PythonNode()
		node.setNodeType("Return")


	def generateNode(self, pos: int, ntype: str) -> PythonNode or list:
		if ntype == "Module(":
			return self.generateModule(pos)
		elif ntype == "ClassDef(":
			return self.generateClassDef(pos)
		elif ntype == "Import(":
			return self.generateImport(pos)
		elif ntype == "ImportFrom(":
			return self.generateImportFrom(pos)
		elif ntype == "Assign(":
			return self.generateAssign(pos)
		elif ntype == "AnnAssign(":
			return self.generateAnnAssign(pos)
		elif ntype == "AsyncFunctionDef(":
			return self.generateAsyncFunctionDef(pos)
		elif ntype == "FunctionDef(":
			return self.generateFunctionDef(pos)
		elif ntype == "Return(":
			return self.generateReturn(pos)
		else:
			raise "Error in PyAST.generateNode(), not valid node type."


	def findName (self, line: str):
		name = ""
		reading = False
		for i in line:
			if (i == "'"):
				if reading:
					break
				else:
					reading = True
			elif reading:
				name += i
		if name == ""
			raise "Error in PyAST.findName(), no name found" 
		return name


	def findValue (self, line: str):
		value = ""
		isString = False
		for i in range(len(line), -1, -1):
			if isString == False:
				if line[i] == "'":
					value += "'"
					isString = True
				elif line[i] != ")" and line[i] != ",":
					value += str(line[i])
				elif line[i] == "=":
					break
				else:
					continue

			else:
				value += line[i]
				if line[i] == "'":
					isString = False

		if value == ""
			raise "Error in PyAST.findValue(), no value found"
		return value