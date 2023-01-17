# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               jsAST.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-16 12:19:59
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-01-17 13:09:55
#   @Description:        This file describes a javaScript ast class 

from app.modules.ast_module.pythonNode import PythonNode
from app.modules.ast_module.AST import AST

import esprima

JSNODETYPES = [
	"ClassDeclaration",
	"ExpressionStatement",
	"VariableDeclaration",
	"FunctionDeclaration",
	"MethodDefinition"
]

class JsAST(AST):

	def generateTree(self, l: list) -> bool:
		# must receive the program.body
		self.dataList = l
		self.tree = self._AST__generateModule()


	def _AST__generateModule(self, pos = None, node = None) -> PythonNode:
		n = PythonNode()
		n.setNodeType("Module")
		for i in self.dataList:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					n.addBody(tmp)
		return n


	def _AST__generateClassDef(self, pos = None, node = None) -> PythonNode:
		n = PythonNode()
		n.setNodeType("ClassDef")
		n.setName(node.id.name)
		# Inheritance
		if node.superClass != None:
			args = [n.superClass.name]
			n.setArgs(args)

		for i in node.body.body:
			if i.type in JSNODETYPES:
				tmp = self._AST__generateNode(ntype = i.type, node = i)
				if tmp != None:
					n.addBody(tmp)

		attributes = self.__findClassAttributes(node.body)
		if len(attributes) > 0:
			for i in attributes:
				assign = PythonNode()
				assign.setNodeType("AnnAssign")
				assign.setName(i)
				assign.setValue(None)
				n.addBody(assign)

		return n


	def _AST__generateImport(self, pos = None, node = None) -> list or PythonNode:
		n = PythonNode()
		n.setNodeType("Import")
		n.setName(node.expression.arguments.name)
		return n


	def _AST__generateImportFrom(self, pos = None, node = None) -> PythonNode:
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
		pass # Doesn't exist in JavaScript


	def _AST__generateAsyncFunctionDef(self, pos = None, node = None):
		pass # Not implemented yet


	def _AST__generateFunctionDef(self, pos = None, node = None) -> PythonNode:
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
