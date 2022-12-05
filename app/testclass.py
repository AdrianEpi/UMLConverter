# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               testclass.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-17 13:08:56
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-05 15:47:20
#   @Description:        This file describes a python ast class and all the node types that are going to be stored in data

from modules.ast_module.pythonNode import PythonNode

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
			if((indent >= self.dataList[i].getIndentationLevel()) and (self.dataList[i].getData() in NODETYPES)):
				indent = self.dataList[i].getIndentationLevel()
				self.tree.addBody(self.generateNode(i, self.dataList[i].getData()))


	def generateModule(self, pos: int):
		node = PythonNode()
		node.setNodeType("Module")
		for i in range(pos + 2, len(self.dataList), 1):
			if (self.dataList[i].getIndentationLevel() == (self.dataList[pos].getIndentationLevel() + 2)):
				if self.dataList[i].getData() in NODETYPES:
					n =	self.generateNode(i, self.dataList[i].getData())
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateModule() (ast line {}), not valid dataType for body".format(pos))
			elif (self.dataList[i].getIndentationLevel() <= self.dataList[pos].getIndentationLevel()):
				break
		return node


	def generateClassDef(self, pos: int):
		node = PythonNode()
		node.setNodeType("ClassDef")
		node.setName(self.findName(self.dataList[pos + 1].getData()))
		if (self.dataList[pos + 2].getData() != "bases=[],"): # The class has inheritance
			inheritance = []
			for i in range(pos + 3, len(self.dataList), 1):
				if "keywords=[" in self.dataList[i].getData():
					break
				else:
					inheritance.append(self.findName(self.dataList[i].getData()))
			node.setArgs(inheritance)

		bodyPos = self.findBodyPos(pos)
		for i in range(bodyPos + 1, len(self.dataList), 1):
			if (self.dataList[i].getIndentationLevel() == (self.dataList[bodyPos].getIndentationLevel() + 1)):
				if self.dataList[i].getData() in NODETYPES:
					n =	self.generateNode(i, self.dataList[i].getData())
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateClassDef() (ast line {}), not valid dataType for body".format(pos))
			elif (self.dataList[i].getIndentationLevel() <= self.dataList[bodyPos].getIndentationLevel()):
				break

		return node


	def generateImport(self, pos: int):
		imports = []
		for i in range(pos + 2, len(self.dataList), 1):
			if "alias(name='" in self.dataList[i].getData():
				node = PythonNode()
				node.setNodeType("Import")
				node.setName(self.findName(self.dataList[i].getData()))
				imports.append(node)
				if ("])," in self.dataList[i].getData()):
					break
			else:
				raise Exception("Error in PyAST.generateImport() (ast line {}), not import name found".format(pos))
		return imports


	def generateImportFrom(self, pos: int):
		node = PythonNode()
		node.setNodeType("ImportFrom")
		imports = []
		l = self.dataList[pos + 1].getData().split("'")
		#TRY NAMES
		node.setName(l[1]) # Will always be the second format:"  module='XXXXX',"
		for i in range(pos + 3, len(self.dataList), 1):
			if "alias(name='" in self.dataList[i].getData():
				imports.append(self.findName(self.dataList[i].getData()))
				if (")]," in self.dataList[i].getData()):
					break
			else:
				raise Exception("Error in PyAST.generateImport() (ast line {}), not import name found".format(pos))
		node.setValue(imports)
		return node


	def generateAssign(self, pos: int):
		assigns = []
		i = pos + 1
		expectedIndent = self.dataList[i].getIndentationLevel()
		while (i < len(self.dataList)):
			if (self.dataList[i].getIndentationLevel() < expectedIndent):
				raise Exception("Error in PyAST.generateAssign() (ast line {}), not assign found".format(pos))
			if self.dataList[i].getData() == "Attribute(":
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.generateAttribute(i))
				assigns.append(node)
				tmpIndent = self.dataList[i].getIndentationLevel()
				i += 1
				while self.dataList[i].getIndentationLevel() > tmpIndent:
					i += 1
				i -= 1
			if "Name(id='" in self.dataList[i].getData(): 
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.findName(self.dataList[i].getData()))
				assigns.append(node)
			if self.dataList[i].getData() == "elts=[": 
				i += 1
				while True:
					node = PythonNode()
					node.setNodeType("Assign")
					if ("Name(id='" in self.dataList[i].getData()):		
						node.setName(self.findName(self.dataList[i].getData()))
					elif ("Attribute(" == self.dataList[i].getData()):
						node.setName(self.generateAttribute(i))
						tmpIndent = self.dataList[i].getIndentationLevel()
						i += 1
						while self.dataList[i].getIndentationLevel() > tmpIndent:
							i += 1
						i -= 1
					elif "ctx=Store()" in self.dataList[i].getData():
						i += 1
						break
					else:
						raise Exception("Error in PyAST.generateAssignTuple() (ast line {}), not valid var in tuple".format(pos))
					i += 1
					assigns.append(node)
			if ("value=Call(" == self.dataList[i].getData()): # No elif, already incremented
				tmp = self.generateFunctionCall(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=Constant" in self.dataList[i].getData()):
				tmp = self.findValue(self.dataList[i].getData())
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=List(" in self.dataList[i].getData()): # For de moment is not storing the list values, just an empty list
				for j in assigns:
					j.setValue("[]")
				break
			if ("value=Name(" in self.dataList[i].getData()): 
				tmp = self.findName(self.dataList[i].getData())
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=BinOp(" in self.dataList[i].getData()):
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
			func=self.findName(self.dataList[i].getData()) + "("
		if self.dataList[i + 1].getData() == "args=[":
			i += 2
			while True:
				if "Name(id='" in self.dataList[i].getData():
					func += self.findName(self.dataList[i].getData()) + ", "
				else: 
					break
				i += 1
			func = func[0:(len(func) - 2)]
		if f:
			func += ")"
		return func



	def generateAttribute(self, pos: int) -> str: # Generates class attributes ["self", "tree", "data"] = self.tree.data
		attrib = ""		
		if ("value=Name(" in self.dataList[pos + 1].getData()):
			attrib = self.findName(self.dataList[pos + 1].getData())
		elif ("func=Attribute(" == self.dataList[pos].getData()):
			attrib = self.generateAttribute(pos + 1)
		elif self.dataList[pos].getData() == "value=Subscript(":
			return self.generateAttribute(pos + 1)
		elif ("value=Attribute(" == self.dataList[pos + 1].getData()):
			attrib = self.generateAttribute(pos + 1)
		elif (self.dataList[pos].getData() == "value=Call("):
			attrib = self.generateFunctionCall(pos)
			return attrib

		expectedIndent = self.dataList[pos].getIndentationLevel() + 1
		i = pos + 1
		while True:
			if (self.dataList[i].getIndentationLevel() < expectedIndent):
				raise Exception("Error in PyAST.generateAttribute(), not attr found.")
			elif (self.dataList[i].getIndentationLevel() == expectedIndent) and ("attr='" in self.dataList[i].getData()):
				attrib += "." + (self.findName(self.dataList[i].getData()))
				break
			i += 1
		return attrib





	def generateAnnAssign(self, pos: int):
		node = PythonNode()
		node.setNodeType("AnnAssign")
		if "Name(id='" in self.dataList[pos + 1].getData():
			node.setName(self.findName(self.dataList[pos + 1].getData()))
		else:
			raise Exception("Error in PyAST.generateAnnAssign() (ast line {}), not name found.".format(pos))

		if "annotation=Name" in self.dataList[pos + 2].getData():
			node.setValue(self.findName(self.dataList[pos + 2].getData()))
		elif "annotation=Call" in self.dataList[pos + 2].getData():
			node.setValue(self.findName(self.dataList[pos + 3].getData()))

		elif ("annotation=BoolOp(" in self.dataList[pos + 2].getData()):
			l = self.getBoolOp(pos + 4)
			node.setValue(l)
		else:
			raise Exception("Error in PyAST.generateAnnAssign() (ast line {}), not value found.".format(pos))
		return node


	def generateAsyncFunctionDef(self, pos: int): # To do
		node = PythonNode()
		node.setNodeType("AsyncFunctionDef")


	def generateFunctionDef(self, pos: int):
		node = PythonNode()
		node.setNodeType("FunctionDef")
		node.setName(self.findName(self.dataList[pos + 1].getData()))
		if ("arg(" in self.dataList[pos + 5].getData()):
			args = []
			i = pos + 5
			while (i < len(self.dataList)):
				if "kwonlyargs=[" in self.dataList[i].getData():
					break
				else:
					if "arg(arg=" in self.dataList[i].getData(): # Non typed param
						args.append(self.findName(self.dataList[i].getData()))
					else: # Typed param -> Generate param name with format "Name: type"
						param = ""
						if ("annotation=Name(" in self.dataList[i + 2].getData()):
							param = str(self.findName(self.dataList[i + 1].getData())) + ": " + str(self.findName(self.dataList[i + 2].getData()))
						elif ("annotation=BoolOp(" in self.dataList[i + 2].getData()):
							print("entra")
							param = str(self.getBoolOp(i + 2))
						else:
							raise Exception("Error in PyAST.generateFunctionDef() (ast line {}), not valid args type".format(i))	

						args.append(param)
						i = self.findNextIndentPos(i)
						if (i == -1):
							break
				i += 1
			node.setArgs(args)

		bodyPos = self.findBodyPos(pos)
		for i in range(bodyPos + 1, len(self.dataList), 1):
			if (self.dataList[i].getIndentationLevel() == (self.dataList[bodyPos].getIndentationLevel() + 1)):
				if self.dataList[i].getData() in NODETYPES:
					n =	self.generateNode(i, self.dataList[i].getData())
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							if (j.getName() != j.getValue()):
								node.addBody(j)
					else:
						raise Exception("Error in PyAST.generateFunctionDef() (ast line {}), not valid dataType for body".format(pos))
			elif (self.dataList[i].getIndentationLevel() <= self.dataList[bodyPos].getIndentationLevel()):
				break

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


	def findName (self, line: str) -> str:
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


	def findValue (self, line: str) -> str or int: # For AnnAssing and Assign nodes
		value = ""
		isString = False
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
		for i in range(pos + 1, len(self.dataList), 1):
			if (self.dataList[i].getIndentationLevel() <= self.dataList[pos].getIndentationLevel()):
				break
			elif (self.dataList[i].getIndentationLevel() == (self.dataList[pos].getIndentationLevel() + 1)):
				if self.dataList[i].getData() == "body=[":
					return i
				elif self.dataList[i].getData() == "body=[],":
					return 0 # Empty body
		raise Exception("Error in PyAST.findBodyPos() (ast line {}), not body".format(pos))


	def findNextIndentPos (self, pos: int) -> int:
		ind = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			if (ind == self.dataList[i].getIndentationLevel()):
				return i
			elif ind < self.dataList[i].getIndentationLevel():
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
				if ("Name" in self.dataList[i].getData()):
					l.append(self.findName(self.dataList[i].getData()))
				elif ("Constant" in self.dataList[i].getData()):
					l.append(self.findValue(self.dataList[i].getData()))
			i += 1
		return l

	def print (self):
		print(self.tree.toString())




# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pythonNode.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-14 21:07:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-11-18 21:39:12
#   @Description:        ...



NODETYPES = [
	"Module",
	"ClassDef",
	"Import",
	"ImportFrom",
	"Assign",
	"AnnAssign",
	"AsyncFunctionDef",
	"FunctionDef",
	"Return"
]

class PythonNode:

	nodeType: str 
	name: str or None
	value: str or int or list or None #returns for functions
	args: list or None # inheritance for classes
	body: list or None

	def __init__(self):
		self.nodeType = ""
		self.name = None
		self.value = None
		self.args = []
		self.body = []


		  	 
	def getNodeType(self) -> str:
		return self.nodeType


	def getName(self) -> str or None:
		return self.name


	def getValue(self) -> str or int or list or None:
		return self.value


	def getArgs(self) -> list or None:
		return self.args

	
	def getBody(self) -> list or None:
		return self.body


	def setNodeType(self, newNodeType: str):
		self.nodeType = newNodeType


	def setName(self, newName: str):
		self.name = newName


	def setValue(self, newValue: str or int):
		self.value = newValue


	def setArgs(self, newArgs: list):
		self.args = newArgs


	def setBody(self, newBody: list):
		self.body = newBody


	def addArg(self, node):
		self.args.append(node)


	def addBody(self, node):
		self.body.append(node)


	def toString(self, indent = 1) -> str:
		output = "\n"
		tab = str(indent * "\t")
		output += tab + self.nodeType
		if(self.name):
			output += "\n" + tab + "    Name: " + self.name
		if(self.value):
			output += "\n" + tab + "    Value: " + str(self.value)
		if(self.args):
			output += "\n" + tab + "    Args: ["
			for i in self.args:
				if (isinstance(i, PythonNode)):
					output += "\n" + i.toString(indent + 1)
				else:
					output += "\n" + str((indent + 1) * "\t") + i
			output += "\n" + tab + "    ]"
		if(self.body):
			output += "\n" + tab + "    Body: ["
			for i in self.body:
				if (isinstance(i, PythonNode)):
					output += "\n" + i.toString(indent + 1)
				else:
					output += "\n" + str((indent + 1) * "\t")
			output += "\n" + tab + "    ]"

		return output


