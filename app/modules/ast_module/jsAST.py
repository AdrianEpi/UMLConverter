# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               jsAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:19:59
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-06 14:43:23
#   @Description:        This file describes a javaScript ast class 

from app.modules.ast_module.pythonNode import PythonNode
from app.modules.ast_module.AST import AST
from app.modules.utils import JSNODETYPES
 
import esprima



class JsAST(AST):
	"""
	This class describes a javascript ast.
	"""

	def generateTree(self, l: list) -> bool:
		"""
		Generates the tree

		:param      l:    list of js nodes
		:type       l:    list

		:returns:   True if tree generated correctly, false otherwise
		:rtype:     bool
		"""
		# must receive the program.body
		self.dataList = l
		self.tree = self._AST__generateModule()
		return True


	def _AST__generateModule(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a javascript module

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node
		:type       node:  javascript node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("Module")
		for i in self.dataList:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					n.addBody(tmp)
		return n


	def _AST__generateClassDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a javascript class

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node
		:type       node:  javascript node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("ClassDef")
		n.setName(node.id.name)
		# Inheritance
		if node.superClass != None:
			args = [node.superClass.name]
			n.setArgs(args)

		for i in node.body.body:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					n.addBody(tmp)

		attributes = self.__findClassAttributes(node.body)
		if len(attributes) > 0:
			for i in attributes:
				n.addBody(self._AST__generateAnnAssign(node = i))

		return n


	def _AST__generateImport(self, pos = None, node = None) -> list or PythonNode:
		"""
		Generates a javascript import

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node
		:type       node:  javascript node

		:returns:   list of strings or pythonnodes or single pythonde 
		:rtype:     list or PythonNode
		"""
		n = PythonNode()
		n.setNodeType("Import")
		n.setName(node.expression.arguments.name)
		return n


	def _AST__generateImportFrom(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a javascript importFrom

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node
		:type       node:  javascript node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("ImportFrom")
		n.setName(node.declarations[0].init.arguments.value)
		if node.id.type == "Identifier":
			n.setValue(node.declarations[0].init.arguments.value)

		elif node.id.type == "ObjectPattern":
			imports = []
			n.setName(node.declarations[0].arguments.value)
			for i in node.declarations[0].id.properties:
				imports.append(i.key.name)
			n.setValue(imports)
		return n


	def _AST__generateAssign(self, pos = None, node = None) -> list:
		pass # Not necesary for Class Diagram in JavaScript


	def _AST__generateAnnAssign(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a javascript annAssign 

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node name in string format
		:type       node:  string

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("AnnAssign")
		n.setName(node)
		n.setValue(None)
		return n



	def _AST__generateAsyncFunctionDef(self, pos = None, node = None):
		pass # Not implemented yet


	def _AST__generateFunctionDef(self, pos = None, node = None) -> PythonNode:
		"""
		Generates a javascript Function 

		:param      pos:   Unnecessary for jsAST
		:param      node:  The node
		:type       node:  javascript node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("FunctionDef")
		n.setName(node.id.name)
		if node.params != None:
			params = []
			for i in node.params:
				params.append(i.name)
			n.setArgs(params)
		body = []
		for i in node.body.body:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					body.append(tmp)
		if len(body) > 0:
			n.setBody(body)
		return n


	def __findClassAttributes(self, node = None) -> list:
		"""
		Finds class attributes.

		:param      node:  The node
		:type       node:  javascript node

		:returns:   list with javascript nodes
		:rtype:     list
		"""
		attrs = []
		if node.type == "ClassBody":
			for i in node.body:
				tmp = self.__findClassAttributes(i)
				for j in tmp:
					if j not in attrs:
						attrs.append(j)
		elif node.type == "MethodDefinition":
			for i in node.value.body.body:
				if i.type == "ExpressionStatement":
					if i.expression.type == "AssignmentExpression":
						if i.expression.left.object != None:
							if i.expression.left.object.type == "ThisExpression":
								attrs.append(i.expression.left.property.name)
		return attrs					


	def __generateMethodDef(self, node = None) -> PythonNode:
		"""
		Generates a javascript method

		:param      node:  The node
		:type       node:  javascript node

		:returns:   The python node.
		:rtype:     PythonNode
		"""
		n = PythonNode()
		n.setNodeType("FunctionDef")
		n.setName(node.key.name)
		params = []
		for i in node.value.params:
			params.append(i.name)
		if len(params) > 0:
			n.setArgs(params)
		body = []
		for i in node.value.body.body:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					body.append(tmp)
		if len(body) > 0:
			n.setBody(body)
		return n


	def _AST__generateNode(self, pos = None, ntype = None, node = None) -> PythonNode or list:
		"""
		Calls the _AST__generateNode corresponded to the node type
		
		:param      pos:        The position
		:type       pos:        int
		:param      ntype:      The ntype
		:type       ntype:      str
		:param      node:       The node
		:type       node:       Node
		
		:returns:   PythonNode or list
		:rtype:     PythonNode or list
		
		:raises     TypeError:  Error if not valid node type
		"""
		if ntype == "Program":
			return self._AST__generateModule(node = node)
		elif ntype == "ClassDeclaration":
			return self._AST__generateClassDef(node = node)
		elif ntype == "ExpressionStatement":
			if node.expression.callee == "require":
				return self._AST__generateImport(node = node)
			elif node.expression.right != None:
				if node.expression.right.type == "ClassExpresssion":
					return self._AST__generateClassDef(node = node.expression.right)
				elif node.expression.right.type == "FunctionExpresssion":
					return self._AST__generateFunctionDef(node = node.expression.right)
		elif ntype == "VariableDeclaration":
			if node.declarations[0].init.callee == "require":
				return self._AST__generateImportFrom(node = node)
			elif node.declarations[0].init.type == "ClassExpresssion":
				return self._AST__generateClassDef(node = node.declarations[0].init)
			elif node.declarations[0].init.type == "FunctionExpresssion":
				return self._AST__generateFunctionDef(node = node.declarations[0].init)
		elif ntype == "FunctionDeclaration":
			return self._AST__generateFunctionDef(node = node)
		elif ntype == "MethodDefinition":
			return self.__generateMethodDef(node = node)
		else:
			return None # In case non necessary node


# class JsAST2Test(JsAST):
# 	def __init__(self):
# 		pass

# 	