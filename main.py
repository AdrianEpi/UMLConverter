# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-09 08:30:09
#   @Description:        ...


from app.modules.uml_module.UMLConverter import UMLConverter

a = UMLConverter()
a.run()




# from app.modules.file_module.file import File
# from app.modules.ast_module.jsAST import JsAST
# import esprima


# f = File('E:\\TFG\\UMLConverter\\samples\\JavaScript_Samples\\School\\Teacher.js')
# f.read()
# #print(f.getData())
# tree = JsAST()
# fileAST = esprima.parseScript(f.getData())
# print(fileAST)
# tree.generateTree(fileAST.body)
# tree.printTree()
