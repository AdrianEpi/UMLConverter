# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_pythonNode.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-09 08:58:52
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-12 08:54:18
#   @Description:        Tests for app/ast_module/pythonNode.py

from app.modules.ast_module.pythonNode import PythonNode
import pytest

node = PythonNode()
node1 = PythonNode()
node2 = PythonNode()

def test_setgetNodeType():
	nodeType = "ClassDef"
	node.setNodeType(nodeType)
	assert(node.getNodeType() == nodeType)


def test_setgetName():
	name = "newName"
	node.setName(name)
	assert(node.getName() == name)

def test_setgetValue():
	value = ["str", "len", "append"]
	node.setValue(value)
	assert(node.getValue() == value)

def test_setgetArgs():
	args = ["str", "len", "append"]
	node.setArgs(args)
	assert(node.getArgs() == args)

def test_setgetBody():
	body = [node, node, node]
	node.setBody(body)
	assert(node.getBody() == body)

def test_addArg():
	args = ["str", "len", "append"]
	node.setArgs(args)
	node.addArg("newArg")
	result = ["str", "len", "append", "newArg"]
	assert(node.getArgs() == result)

def test_addBody():
	body = [node, node, node]
	node.setBody(body)
	node.addBody(node)
	result = [node, node, node, node]
	assert(node.getBody() == result)

def test_toString():
	node = PythonNode()
	node.setNodeType("ClassDef")
	node1.setNodeType("FunctionDef")
	node2.setNodeType("Assign")
	node.setName("Class1")
	node1.setName("Func1")
	node2.setName("var1")
	node1.setValue("str")
	node2.setValue(10)
	node1.setArgs(["arg1", "arg2", "arg3", node2])
	node.addBody(node1)
	node1.addBody(node2)
	result = "\n\tClassDef\n\t    Name: Class1\n\t    Body: [\n\n\t\tFunctionDef\n\t\t    Name: Func1\n\t\t    Value: str\n\t\t    Args: [\n\t\t\targ1\n\t\t\targ2\n\t\t\targ3\n\n\t\t\tAssign\n\t\t\t    Name: var1\n\t\t\t    Value: 10\n\t\t    ]\n\t\t    Body: [\n\n\t\t\tAssign\n\t\t\t    Name: var1\n\t\t\t    Value: 10\n\t\t    ]\n\t    ]"
	assert(node.toString() == result)


def test_toStringBodyException():
	node = PythonNode()
	node.addBody("AA")
	with pytest.raises(Exception) as exception_info:
		node.toString()
	assert str(exception_info.value) == 'Error PythonNode.toString(), body must be a node.'
