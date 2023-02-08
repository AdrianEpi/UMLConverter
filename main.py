# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               main.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-11-13 16:25:53
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-08 20:58:44
#   @Description:        ...


from app.modules.uml_module.UMLConverter import UMLConverter

a = UMLConverter()
a.run()


# from os import system

# system('mdpdf -o ' + './outputs/projectUML.pdf '+ './outputs/projectUML.md')