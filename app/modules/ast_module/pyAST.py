# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               pyAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-17 13:08:56
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-31 13:18:04
#   @Description:        This file describes a python ast class

from app.modules.ast_module.pythonNode import PythonNode
from app.modules.ast_module.AST import AST
from app.modules.utils import NODETYPES

class PyAST(AST):


	def generateTree(self, l: list) -> bool:
		"""
		Generates the python tree
		
		:param      l:    list of lines readed form ast python module
		:type       l:    list
		
		:returns:   True if tree can be generated, false otherwhise
		:rtype:     bool
		"""
		self.dataList = l
		if "Module(" == self.dataList[0].getData():
			self.tree = self._AST__generateModule(0)
			return True
		else:
			return False


	def _AST__generateModule(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a Module PythonNode
		Module:
			nodeType: "Module" 
			name: str (Name of the module)
			value: None
			args: None
			body: list of PyhonNode (List with nodes in module's body)
		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node

		:returns:   The python node.
		:rtype:     PythonNode
		
		:raises     TypeError:  Error if not PythonNode type
		"""
		node = PythonNode()
		node.setNodeType("Module")
		indent = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 2, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (indent + 2)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self._AST__generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise TypeError("Error in PyAST._AST__generateModule() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= indent):
				break
		return node


	def _AST__generateClassDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a ClassDef PythonNode
		ClassDef:
			nodeType: "ClassDef" 
			name: str (Name of the class)
			value: None
			args: str (Class Inheritance)
			body: list of PyhonNode (List with nodes in class's body)

		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   The python node.
		:rtype:     PythonNode
		
		:raises     TypeError:  Error if not valid types
		"""
		node = PythonNode()
		node.setNodeType("ClassDef")
		node.setName(self.__findName(pos + 1))
		if (self.dataList[pos + 2].getData() != "bases=[],"): # The class has inheritance
			inheritance = []
			for i in range(pos + 3, len(self.dataList), 1):
				if "keywords=[" in self.dataList[i].getData():
					break
				else:
					inheritance.append(self.__findName(i))
			node.setArgs(inheritance)

		bodyPos = self.__findBodyPos(pos)
		bodyIndent = self.dataList[bodyPos].getIndentationLevel()
		for i in range(bodyPos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (bodyIndent + 1)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self._AST__generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							node.addBody(j)
					else:
						raise TypeError("Error in PyAST._AST__generateClassDef() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= bodyIndent):
				break

		return node


	def _AST__generateImport(self, pos = None, node = None) -> list or PythonNode:
		"""
		Generates an Import PythonNode
		Import:
			nodeType: "Import" 
			name: str (Name of the imported module)
			value: None
			args: None
			body: None

		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   List of PythonNode
		:rtype:     list

		:raises     Exception:  Not found import
		"""
		imports = []
		for i in range(pos + 2, len(self.dataList), 1):
			data = self.dataList[i].getData()
			if "alias(name='" in data:
				node = PythonNode()
				node.setNodeType("Import")
				node.setName(self.__findName(i))
				imports.append(node)
				if ("])," in data or ")]," in data):
					break
			else:
				raise Exception("Error in PyAST._AST__generateImport() (ast line {}), not import name found".format(pos))
		return imports


	def _AST__generateImportFrom(self, pos = None, node = None) -> PythonNode:
		"""
		Generates an ImportFrom PythonNode
		ImportFrom:
			nodeType: "ImportFrom" 
			name: str (Name of the imported Module)
			value: list of str (List of imported functionalities)
			args: None
			body: None

		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   The python node.
		:rtype:     PythonNode

		:raises     Exception:  Not found imports from
		"""
		node = PythonNode()
		node.setNodeType("ImportFrom")
		imports = []
		l = self.dataList[pos + 1].getData().split("'")
		node.setName(l[1]) # Will always be the second format:"  module='XXXXX',"
		for i in range(pos + 3, len(self.dataList), 1):
			data = self.dataList[i].getData()
			if "alias(name='" in data:
				imports.append(self.__findName(i))
				if (")]," in data):
					break
			else:
				raise Exception("Error in PyAST._AST__generateImportFrom() (ast line {}), not import name found".format(pos))
		node.setValue(imports)
		return node


	def _AST__generateAssign(self, pos = None, node = None) -> list:
		"""
		Generates an Assign PythonNode
		Assign:
			nodeType: "Assign" 
			name: str (Name of the assign)
			value: str or int or list or bool or Object (Assign value)
			args: None
			body: None

		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   list of PythonNode, strings, integers or empty list
		:rtype:     list

		:raises     Exception:  Error findind assing or generating tuples
		"""
		assigns = []
		i = pos + 1
		expectedIndent = self.dataList[i].getIndentationLevel()
		while (i < len(self.dataList)):
			actualIndent = self.dataList[i].getIndentationLevel()
			data = self.dataList[i].getData()
			if (actualIndent < expectedIndent):
				raise Exception("Error in PyAST._AST__generateAssign() (ast line {}), not assign found".format(pos))
			if data == "Attribute(":
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.__generateAttribute(i))
				assigns.append(node)
				tmpIndent = actualIndent
				i = self.__findNextIndentPos(i + 1) # Find the next indent afther the parent
			if "Name(id='" in data: 
				node = PythonNode()
				node.setNodeType("Assign")
				node.setName(self.__findName(i))
				assigns.append(node)

			if data == "elts=[": 

				i += 1
				while True:
					data = self.dataList[i].getData()
					node = PythonNode()
					node.setNodeType("Assign")
					if ("Name(id='" in data):		
						node.setName(self.__findName(i))
					elif ("Attribute(" == data):
						node.setName(self.__generateAttribute(i))
						tmpIndent = actualIndent
						i += 1
						while actualIndent > tmpIndent:
							i += 1
						i -= 1
					elif "ctx=Store()" in data:
						i += 1
						break
					else:
						raise Exception("Error in PyAST._AST__generateAssignTuple() (ast line {}), not valid var in tuple".format(pos))

					i += 1
					assigns.append(node)
				data = self.dataList[i].getData()

			if ("value=Call(" == data): # No elif, already incremented
				tmp = self.__generateFunctionCall(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=Constant" in data):
				tmp = self.__findValue(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=List(" in data): # For de moment is not storing the list values, just an empty list
				for j in assigns:
					j.setValue("[]")
				break
			if ("value=Name(" in data): 
				tmp = self.__findName(i)
				for j in assigns:
					j.setValue(tmp)
				break
			if ("value=BinOp(" in data):
				for j in assigns:
					j.setValue("BinaryOperation")
				break
			if ("value=Dict(" in data):
				for j in assigns:
					j.setValue("Dict")
				break
			i += 1
		return assigns

			
	def __generateFunctionCall(self, pos: int) -> str:
		"""
	 	Generate a function call "var.func()"  in str format of the ast
	 
	 	:param      pos:        The position
	 	:type       pos:        int
	 
	 	:returns:   str representation of the function call
	 	:rtype:     str
	  	""" 
		i = pos + 1
		expectedIndent = self.dataList[i].getIndentationLevel()
		func = ""
		f = False
		if "func=Attribute(" in self.dataList[i].getData():
			func = self.__generateAttribute(i)
		else:
			f = True
			func = self.__findName(i) + "("
		if self.dataList[i + 1].getData() == "args=[":
			i += 2
			while True:
				data = self.dataList[i].getData()
				if "Name(id='" in data:
					func += self.__findName(i) + ", "
				elif "BinOp(" in data:
					func += "BinaryOperation, "
					i = self.__findNextIndentPos(i)
					i -= 1
				else: 
					break
				i += 1
			func = func[0:(len(func) - 2)]
		if f:
			func += ")"
		return func


	def __generateAttribute(self, pos: int) -> str:
		"""
	 	Generates class attributes ["self", "tree", "data"] = self.tree.data
	 
	 	:param      pos:        The position
	 	:type       pos:        int
	 
	 	:returns:   String representation of the atributes
	 	:rtype:     str
	 
	 	:raises     Exception:  Error if not attribute found
	 	""" 
		attrib = ""		
		data = self.dataList[pos].getData()
		data1 = self.dataList[pos + 1].getData()
		if "value=Name(" in data1:
			attrib = self.__findName(pos + 1)

		elif "func=Attribute(" == data:
			attrib = self.__generateAttribute(pos + 1)
		
		elif data == "value=Subscript(":
			return self.__generateAttribute(pos + 1)
		
		elif "value=Attribute(" == data1:
			attrib = self.__generateAttribute(pos + 1)
		
		elif data == "value=Call(":
			attrib = self.__generateFunctionCall(pos)
			return attrib

		expectedIndent = self.dataList[pos].getIndentationLevel() + 1
		i = pos + 1
		while True:
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent < expectedIndent):
				raise Exception("Error in PyAST.__generateAttribute(), not attr found.")
			elif (actualIndent == expectedIndent) and ("attr='" in self.dataList[i].getData()):
				attrib += "." + (self.__findName(i))
				break
			i += 1
		return attrib


	def _AST__generateAnnAssign(self, pos = None, node = None) -> PythonNode:
		"""
		Generates an AnnAssign PythonNode
		AnnAssign:
			nodeType: "AnnAssign" 
			name: str (Name of the var)
			value: str or int or list or bool or Object (Assign value)
			args: None
			body: None

		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   The python node.
		:rtype:     PythonNode

		:raises     Exception:  Error if not name or value found
		"""
		node = PythonNode()
		node.setNodeType("AnnAssign")
		data1 = self.dataList[pos + 1].getData()
		if "Name(id='" in data1:
			node.setName(self.__findName(pos + 1))
		elif "target=Subscript(" in data1:
			node.setName(self.__findName(pos + 2) + "[...]")
		elif "target=Attribute(" in data1:
			node.setName(self.__generateAttribute(pos + 1))
		else:
			raise Exception("Error in PyAST._AST__generateAnnAssign() (ast line {}), not name found.".format(pos))

		posVal = self.__findNextIndentPos(pos + 1)
		data2 = self.dataList[posVal].getData()
		if "annotation=Name" in data2:
			node.setValue(self.__findName(posVal))
		elif "annotation=Constant" in data2:
			node.setValue(self.__findValue(posVal))
		elif "annotation=Call" in data2:
			node.setValue(self.__findName(posVal + 1))
		elif ("annotation=BoolOp(" in data2):
			l = self.__getBoolOp(posVal + 2)
			node.setValue(l)
		else:
			raise Exception("Error in PyAST._AST__generateAnnAssign() (ast line {}), not value found.".format(pos))
		return node


	# FUNCTION NOT IMPLEMENTED YET
	def _AST__generateAsyncFunctionDef(self, pos = None, node = None):
		node = PythonNode()
		node.setNodeType("AsyncFunctionDef")


	def _AST__generateFunctionDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a FunctionDef PythonNode. 
		FunctionDef:
			nodeType: "FunctionDef" 
			name: str (Name of the function)
			value: str or int or list or bool or Object (Return type)
			args: str, Object, list, bool or int (Function arguments)
			body: list of PyhonNode (List with nodes in function's body)
		
		:param      pos:        The position
		:type       pos:        int
		:param      node:       The node
		:type       node:       Node
		
		:returns:   The python node.
		:rtype:     PythonNode
		
		:raises     TypeError:  Error if not valid types for args or body
		"""
		node = PythonNode()
		node.setNodeType("FunctionDef")
		node.setName(self.__findName(pos + 1))
		if ("arg(" in self.dataList[pos + 5].getData()):
			args = []
			i = pos + 5
			while (i < len(self.dataList)):
				data = self.dataList[i].getData()
				if "kwonlyargs=[" in data:
					break
				else:
					if "arg(arg=" in data: # Non typed param
						args.append(self.__findName(i))
					else: # Typed param -> Generate param name with format "Name: type"
						param = ""
						data2 = self.dataList[i + 2].getData()
						if ("annotation=Name(" in data2):
							param = str(self.__findName(i + 1)) + ": " + str(self.__findName(i + 2))
						elif ("annotation=BoolOp(" in data2):
							param = str(self.__getBoolOp(i + 2))

						else:
							raise TypeError("Error in PyAST._AST__generateFunctionDef() (ast line {}), not valid args type".format(i))	

						args.append(param)
						i = self.__findNextIndentPos(i)
						if (i == -1):
							break
						i -= 1
				i += 1
			node.setArgs(args)

		bodyPos = self.__findBodyPos(pos)
		bodyIndent = self.dataList[bodyPos].getIndentationLevel()
		for i in range(bodyPos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent == (bodyIndent + 1)):
				data = self.dataList[i].getData()
				if data in NODETYPES:
					n =	self._AST__generateNode(i, data)
					if isinstance(n, PythonNode):
						node.addBody(n)
					elif isinstance(n, list):
						for j in n:
							if (j.getName() != j.getValue()):
								node.addBody(j)
					else:
						raise TypeError("Error in PyAST._AST__generateFunctionDef() (ast line {}), not valid dataType for body".format(pos))
			elif (actualIndent <= bodyIndent):
				break

		r = self.__findReturn(pos)
		if r:
			node.setValue(r)
		return node


	def _AST__generateNode(self, pos = None, ntype = None, node = None) -> PythonNode or list:
		"""
		Calls the _AST__generateNode corresponded to the node type

		:param      pos:        The position
		:type       pos:        int
		:param      ntype:      The ntype
		:type       ntype:      str

		:returns:   PythonNode or list
		:rtype:     PythonNode or list

		:raises     TypeError:  Error if not valid node type
		"""
		if ntype == "Module(":
			return self._AST__generateModule(pos = pos)
		elif ntype == "ClassDef(":
			return self._AST__generateClassDef(pos = pos)
		elif ntype == "Import(":
			return self._AST__generateImport(pos = pos)
		elif ntype == "ImportFrom(":
			return self._AST__generateImportFrom(pos = pos)
		elif ntype == "Assign(":
			return self._AST__generateAssign(pos = pos)
		elif ntype == "AnnAssign(":
			return self._AST__generateAnnAssign(pos = pos)
		elif ntype == "AsyncFunctionDef(":
			return self._AST__generateAsyncFunctionDef(pos = pos)
		elif ntype == "FunctionDef(":
			return self._AST__generateFunctionDef(pos = pos)
		else:
			raise TypeError("Error in PyAST._AST__generateNode() (ast line {}), not valid node type.".format(pos))


	def __findName (self, pos: int) -> str:
		"""
		Finds a name in a given Line from an AST.

		:param      pos:        The position
		:type       pos:        int

		:returns:   name if found
		:rtype:     str

		:raises     Exception:  Error if not name found
		"""
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
			raise Exception("Error in PyAST.__findName(), no name found")
		return name


	def __findValue (self, pos: int) -> str or int:
		"""
		Finds a value in a given Line from an AST. For AnnAssign and Assign nodes

		:param      pos:        The position
		:type       pos:        int

		:returns:   value if found
		:rtype:     str

		:raises     Exception:  Error if not value found
		"""
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
			raise Exception("Error in PyAST.__findValue(), no value found")
		return value[::-1] # [::-1] reverses python string


	def __findBodyPos (self, pos: int) -> int:
		"""
		Finds a body position.

		:param      pos:        The position
		:type       pos:        int

		:returns:   Position where the boddy starts
		:rtype:     int

		:raises     Exception:	Error if not body found
		"""

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
		raise Exception("Error in PyAST.__findBodyPos() (ast line {}), not body".format(pos))

	def __findReturn (self, pos: int) -> str or list:
		expectedIndent = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (actualIndent <= expectedIndent):
				return None
			elif (actualIndent == (expectedIndent + 1)):
				data = self.dataList[i].getData()
				if "returns=Name(" in data:
					return self.__findName(i)
				elif "returns=BoolOp(" in data:
					return self.__getBoolOp(i)

		raise Exception("Error in PyAST.__findReturn() (ast line {}), no return found".format(pos))


	def __findNextIndentPos (self, pos: int) -> int:
		"""
		Finds the next indent level position (finds the next line with the same indent level)

		:param      pos:        The position
		:type       pos:        int

		:returns:   Position where the next indent level starts
		:rtype:     int

		:raises     Exception:  Error if not lower indent level found
		"""
		ind = self.dataList[pos].getIndentationLevel()
		for i in range(pos + 1, len(self.dataList), 1):
			actualIndent = self.dataList[i].getIndentationLevel()
			if (ind == actualIndent):
				return i
			elif ind > actualIndent:
				return -1
		raise Exception("Error in PyAST.__findNextIndentPos() (ast line {}), not lower indent found".format(pos))


	def __getBoolOp(self, pos: int) -> list:
		"""
		Gets the bool operation.

		:param      pos:  The position
		:type       pos:  int

		:returns:   The bool operation params in a list.
		:rtype:     list
		"""
		l = []
		expectedIndent = self.dataList[pos].getIndentationLevel() + 1
		i = pos + 1
		while True:
			if (self.dataList[i].getIndentationLevel() < expectedIndent):
				break
			else:
				data = self.dataList[i].getData()
				if ("Name" in data):
					l.append(self.__findName(i))
				elif ("Constant" in data):
					l.append(self.__findValue(i))
			i += 1
		return l

