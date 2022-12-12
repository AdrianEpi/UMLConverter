# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-17 13:08:56
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-12 10:09:49
#   @Description:        This file describes a python ast class and all the node types that are going to be stored in data

from app.modules.ast_module.pythonNode import PythonNode

NODETYPES = [
	"Module(",
	"ClassDef(",
	"Import(",
	"ImportFrom(",
	"Assign(",
	"AnnAssign(",
	"AsyncFunctionDef(",
	"FunctionDef("
]


class PyAST:

	tree: PythonNode()
	dataList: list


	def __init__ (self):
		self.tree = PythonNode()
		self.dataList = []


	def getDataList (self) -> list:
		return self.dataList


	def getTree (self) -> PythonNode:
		return self.tree


	def setDataList (self, l: list):
		self.dataList = l


	def setTree (self, t: PythonNode):
		self.tree = t


	def generateTree(self, l: list):
		self.dataList = l
		pos = 0
		indent = 9999
		self.tree.setName("root")
		self.tree.setNodeType("root")
		for i in range(0, len(self.dataList), 1):
			data = self.dataList[i].getData()
			newIndent = self.dataList[i].getIndentationLevel()
			if((indent >= newIndent) and (data in NODETYPES)):
				indent = newIndent
				self.tree.addBody(self.generateNode(i, data))
		if (len(self.tree.getBody()) == 1):
			self.tree = self.tree.getBody()[0]


	def generateModule(self, pos: int) -> PythonNode:
		node = PythonNode()
		node.setNodeType("Module")
		indent = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 2, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (indent + 2)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self.generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateModule() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= indent):
				break
		return node


	def generateClassDef(self, pos: int) -> PythonNode:
		node = PythonNode()
		node.setNodeType("ClassDef")
		node.setName(self.findName(pos + 1))
		if (self.dataList[pos + 2].getData() != "bases=[],"): # The class has inheritance
			inheritance = []
			for i in range(pos + 3, len(self.dataList), 1):
				if "keywords=[" in self.dataList[i].getData():
					break
				else:
					inheritance.append(self.findName(i))
			node.setArgs(inheritance)

		bodyPos = self.findBodyPos(pos)
		bodyIndent = self.dataList[bodyPos].getIndentationLevel()
		for i in range(bodyPos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (bodyIndent + 1)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self.generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateClassDef() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= bodyIndent):
				break

		return node


	def generateImport(self, pos: int) -> list:
		imports = []
		for i in range(pos + 2, len(self.dataList), 1):
			data = self.dataList[i].getData()
			if "alias(name='" in data:
				node = PythonNode()
				node.setNodeType("Import")
				node.setName(self.findName(i))
				imports.append(node)
				if ("])," in data or ")]," in data):
					break
			else:
				raise Exception("Error in PyAST.generateImport() (ast line {}), not import name found".format(pos))
		return imports


	def generateImportFrom(self, pos: int) -> PythonNode:
		node = PythonNode()
		node.setNodeType("ImportFrom")
		imports = []
		l = self.dataList[pos + 1].getData().split("'")
		node.setName(l[1]) # Will always be the second format:"  module='XXXXX',"
		for i in range(pos + 3, len(self.dataList), 1):
			data = self.dataList[i].getData()
			if "alias(name='" in data:
				imports.append(self.findName(i))
				if (")]," in data):
					break
			else:
				raise Exception("Error in PyAST.generateImport() (ast line {}), not import name found".format(pos))
		node.setValue(imports)
		return node


	def generateAssign(self, pos: int) -> list:
		assigns = []
		i = pos + 1
		expectedIndent = self.dataList[i].getIndentationLevel()
		while (i < len(self.dataList)):
			actualIndent = self.dataList[i].getIndentationLevel()
			data = self.dataList[i].getData()
			if (actualIndent < expectedIndent):
				raise Exception("Error in PyAST.generateAssign() (ast line {}), not assign found".format(pos))
			if data == "Attribute(":
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.generateAttribute(i))
				assigns.append(node)
				tmpIndent = actualIndent
				i += 1
				while actualIndent > tmpIndent:
					i += 1
				i -= 1
			if "Name(id='" in data: 
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.findName(i))
				assigns.append(node)
			if data == "elts=[": 
				i += 1
				while True:
					node = PythonNode()
					node.setNodeType("Assign")
					if ("Name(id='" in data):		
						node.setName(self.findName(i))
					elif ("Attribute(" == data):
						node.setName(self.generateAttribute(i))
						tmpIndent = actualIndent
						i += 1
						while actualIndent > tmpIndent:
							i += 1
						i -= 1
					elif "ctx=Store()" in data:
						i += 1
						break
					else:
						raise Exception("Error in PyAST.generateAssignTuple() (ast line {}), not valid var in tuple".format(pos))
					i += 1
					assigns.append(node)
			if ("value=Call(" == data): # No elif, already incremented
				tmp = self.generateFunctionCall(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=Constant" in data):
				tmp = self.findValue(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=List(" in data): # For de moment is not storing the list values, just an empty list
				for j in assigns:
					j.setValue("[]")
				break
			if ("value=Name(" in data): 
				tmp = self.findName(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=BinOp(" in data):
				for j in assigns:
					j.setValue("BinaryOperation")
				break
			i += 1
		return assigns

			
	def generateFunctionCall(self, pos: int) -> str: 
		i = pos + 1
		expectedIndent = self.dataList[i].getIndentationLevel()
		func = ""
		f = False
		if "func=Attribute(" in self.dataList[i].getData():
			func = self.generateAttribute(i)
		else:
			f = True
			func = self.findName(i) + "("
		if self.dataList[i + 1].getData() == "args=[":
			i += 2
			while True:
				data = self.dataList[i].getData()
				if "Name(id='" in data:
					func += self.findName(i) + ", "
				elif "BinOp(" in data:
					func += "BinaryOperation, "
					i = self.findNextIndentPos(i)
					i -= 1
				else: 
					break
				i += 1
			func = func[0:(len(func) - 2)]
		if f:
			func += ")"
		return func


	def generateAttribute(self, pos: int) -> str: # Generates class attributes ["self", "tree", "data"] = self.tree.data
		attrib = ""		
		data = self.dataList[pos].getData()
		data1 = self.dataList[pos + 1].getData()
		if "value=Name(" in data1:
			attrib = self.findName(pos + 1)

		elif "func=Attribute(" == data:
			attrib = self.generateAttribute(pos + 1)
		
		elif data == "value=Subscript(":
			return self.generateAttribute(pos + 1)
		
		elif "value=Attribute(" == data1:
			attrib = self.generateAttribute(pos + 1)
		
		elif data == "value=Call(":
			attrib = self.generateFunctionCall(pos)
			return attrib

		expectedIndent = self.dataList[pos].getIndentationLevel() + 1
		i = pos + 1
		while True:
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent < expectedIndent):
				raise Exception("Error in PyAST.generateAttribute(), not attr found.")
			elif (actualIndent == expectedIndent) and ("attr='" in self.dataList[i].getData()):
				attrib += "." + (self.findName(i))
				break
			i += 1
		return attrib


	def generateAnnAssign(self, pos: int) -> PythonNode:
		node = PythonNode()
		node.setNodeType("AnnAssign")
		data2 = self.dataList[pos + 2].getData()
		if "Name(id='" in self.dataList[pos + 1].getData():
			node.setName(self.findName(pos + 1))
		else:
			raise Exception("Error in PyAST.generateAnnAssign() (ast line {}), not name found.".format(pos))

		if "annotation=Name" in data2:
			node.setValue(self.findName(pos + 2))
		elif "annotation=Call" in data2:
			node.setValue(self.findName(pos + 3))

		elif ("annotation=BoolOp(" in data2):
			l = self.getBoolOp(pos + 4)
			node.setValue(l)
		else:
			raise Exception("Error in PyAST.generateAnnAssign() (ast line {}), not value found.".format(pos))
		return node


	def generateAsyncFunctionDef(self, pos: int): # To do
		node = PythonNode()
		node.setNodeType("AsyncFunctionDef")


	def generateFunctionDef(self, pos: int) -> PythonNode:
		node = PythonNode()
		node.setNodeType("FunctionDef")
		node.setName(self.findName(pos + 1))
		if ("arg(" in self.dataList[pos + 5].getData()):
			args = []
			i = pos + 5
			while (i < len(self.dataList)):
				data = self.dataList[i].getData()
				if "kwonlyargs=[" in data:
					break
				else:
					if "arg(arg=" in data: # Non typed param
						args.append(self.findName(i))
					else: # Typed param -> Generate param name with format "Name: type"
						param = ""
						data2 = self.dataList[i + 2].getData()
						if ("annotation=Name(" in data2):
							param = str(self.findName(i + 1)) + ": " + str(self.findName(i + 2))
						elif ("annotation=BoolOp(" in data2):
							param = str(self.getBoolOp(i + 2))

						else:
							raise Exception("Error in PyAST.generateFunctionDef() (ast line {}), not valid args type".format(i))	

						args.append(param)
						i = self.findNextIndentPos(i)
						if (i == -1):
							break
						i -= 1
				i += 1
			node.setArgs(args)

		bodyPos = self.findBodyPos(pos)
		bodyIndent = self.dataList[bodyPos].getIndentationLevel()
		for i in range(bodyPos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (bodyIndent + 1)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self.generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							if (j.getName() != j.getValue()):
								node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateFunctionDef() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= bodyIndent):
				break

		r = self.findReturn(pos)
		if r:
			node.setValue(r)
		return node


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
		else:
			raise Exception("Error in PyAST.generateNode() (ast line {}), not valid node type.".format(pos))


	def findName (self, pos: int) -> str:
		line = self.dataList[pos].getData()
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
		if name == "":
			raise Exception("Error in PyAST.findName(), no name found")
		return name


	def findValue (self, pos: int) -> str or int: # For AnnAssing and Assign nodes
		value = ""
		isString = False
		line = self.dataList[pos].getData()
		for i in range(len(line) - 1, -1, -1):
			if isString == False:
				if line[i] == "'":
					value += "'"
					isString = True
				elif line[i] != ")" and line[i] != "," and line[i] != "=" and line[i] != "]":
					value += str(line[i])
				elif line[i] == "=":
					break
				else:
					continue

			else:
				value += line[i]
				if line[i] == "'":
					isString = False



		if value == "":
			raise Exception("Error in PyAST.findValue(), no value found")
		return value[::-1] # [::-1] reverses python string


	def findBodyPos (self, pos: int) -> int:
		indent = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent <= indent):
				break
			elif (actualIndent == (indent + 1)):
				data = self.dataList[i].getData()
				if data == "body=[":
					return i
				elif data == "body=[],":
					return 0 # Empty body
		raise Exception("Error in PyAST.findBodyPos() (ast line {}), not body".format(pos))

	def findReturn (self, pos: int) -> str or list:
		expectedIndent = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent <= expectedIndent):
				return None
			elif (actualIndent == (expectedIndent + 1)):
				data = self.dataList[i].getData()
				if "returns=Name(" in data:
					return self.findName(i)
				elif "returns=BoolOp(" in data:
					return self.getBoolOp(i)

		raise Exception("Error in PyAST.findReturn() (ast line {}), no return found".format(pos))


	def findNextIndentPos (self, pos: int) -> int:
		ind = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (ind == actualIndent):
				return i
			elif ind > actualIndent:
				return -1
		raise Exception("Error in PyAST.findNextIndentPos() (ast line {}), not lower indent found".format(pos))


	def getBoolOp(self, pos: int) -> list:
		l = []
		expectedIndent = self.dataList[pos].getIndentationLevel() + 1
		i = pos + 1
		while True:
			if (self.dataList[i].getIndentationLevel() < expectedIndent):
				break
			else:
				data = self.dataList[i].getData()
				if ("Name" in data):
					l.append(self.findName(i))
				elif ("Constant" in data):
					l.append(self.findValue(i))
			i += 1
		return l


	def print (self):
		print(self.tree.toString())