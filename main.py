# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-02 08:56:55
#   @Description:        ...


from app.modules.uml_module.UMLConverter import UMLConverter

a = UMLConverter()
a.run()


# import esprima
# from app.modules.ast_module.jsAST import JsAST
# aaa = '''

# console.log(materials.map(material => material.length));

# '''

# b = '''
# class Teacher extends Person {
#   constructor(first, last, age, gender, interests, subject, grade) {
#     this.name = {
#       first,
#       last
#     };

#   this.age = age;
#   this.gender = gender;
#   this.interests = interests;
#   // subject and grade are specific to Teacher
#   this.subject = subject;
#   this.grade = grade;
#   }
# }
# '''

# c = '''
# require('esprima')
# var fs = require('fs');
# const { specialForms } = require("../interpreter/registry.js");
# var { egg2js, deleteEnd } = require("../jsTranslator/egg2js.js");
# var asdf = Hello()
# '''

# d = '''
# var a = class Point {
# 	constructor(x, y) {

# 	}
# }
# d = function a() { }

# '''

# e = '''
# class Point {

#   constructor(coordinateX_, coordinateY_) {
#     this.coordinateX = coordinateX_;
#     this.coordinateY = coordinateY_;
#   }

#   aa() {
#   }
# }

# '''
# #print(esprima.parseScript(aaa))
# l = esprima.parseScript(e)

# print(l)
# i = JsAST()
# i.generateTree(l.body)
# i.printTree()



# # for i in l.body:
# # 	print(i)
