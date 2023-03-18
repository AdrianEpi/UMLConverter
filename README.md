# UMLConverter
Repository for Thesis code

## TABLE OF CONTENTS
1. [Requirements](#REQUIREMENTS)
2. [Setting up (local enviroment)](#SETTING-UP-LOCAL-ENVIROMENT)


## REQUIREMENTS
- Python3.10 
- Python3.10-venv `sudo apt install python3.10-venv`


## SETTING UP LOCAL ENVIROMENT

In order to run the project for the first time:

1) Make sure you have all the [REQUIREMENTS](#REQUIREMENTS)
2) Clone this repository and make sure you have ssh key generated locally and added to your github account
```sh
	git clone git@github.com:AdrianEpi/UMLConverter.git
```
3) Go to the root directory of the project:
```sh
	cd UMLConverter/
```
4) Install virtual enviroment if don't have it yet
```sh
	sudo apt install python3.10-venv
```
5) Generate the virtual enviroment for the repository
```sh
	python3 -m venv .venv
```
6) Activate the virtual enviroment
```sh
	source .venv/bin/activate
```
7) Install all the packages
```sh
	pip install -r requirements.txt
```
8) Install tkinter for interface display
```sh
	sudo apt-get install python3-tk
```

## Exceute

1) Activate the virtual enviroment
```sh
	source .venv/bin/activate
```
2) Run program
```sh
	python UMLConverter/main.py
```


## TEST AND COVERAGE

1) Test the code
```sh
	cd UMLConverter/
	coverage run -m pytest
```

2) Print report of coverage
```sh
	coverage report
```

2) Generate html version of coverage in `htmlcov/`
```sh
	coverage html
```

## Test log

```py
===================================================== test session starts =====================================================
platform linux -- Python 3.10.6, pytest-7.2.0, pluggy-1.0.0 -- /mnt/e/TFG/UMLConverter/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /mnt/e/TFG/UMLConverter
collected 74 items

tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/AbstractMethods/main.py-samples/Simple_Samples/AbstractMethods/main.uml] PASSED [  1%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/AccessModifiers/Private/main.py-samples/Simple_Samples/AccessModifiers/Private/main.uml] PASSED [  2%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/AccessModifiers/Protected/main.py-samples/Simple_Samples/AccessModifiers/Protected/main.uml] PASSED [  4%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/AccessModifiers/Public/main.py-samples/Simple_Samples/AccessModifiers/Public/main.uml] PASSED [  5%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/Attributes/main.py-samples/Simple_Samples/Attributes/main.uml] PASSED [  6%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/MethodReturnType/main.py-samples/Simple_Samples/MethodReturnType/main.uml] PASSED [  8%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/MethodsWithoutParameters/main.py-samples/Simple_Samples/MethodsWithoutParameters/main.uml] PASSED [  9%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/MethodsWithParameters/main.py-samples/Simple_Samples/MethodsWithParameters/main.uml] PASSED [ 10%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/StaticMethods/main.py-samples/Simple_Samples/StaticMethods/main.uml] PASSED [ 12%]
tests/test_UMLConverter.py::test_AST[samples/Simple_Samples/Types/main.py-samples/Simple_Samples/Types/main.uml] PASSED [ 13%]
tests/test_UMLConverter.py::test_AST[samples/testAST/ClassDef/complexClass.py-samples/testAST/ClassDef/complexClass.uml] PASSED [ 14%]
tests/test_UMLConverter.py::test_AST[samples/testAST/ClassDef/inheritedClass.py-samples/testAST/ClassDef/inheritedClass.uml] PASSED [ 16%]
tests/test_UMLConverter.py::test_AST[samples/testAST/ClassDef/simpleClass.py-samples/testAST/ClassDef/simpleClass.uml] PASSED [ 17%]
tests/test_UMLConverter.py::test_AST[samples/testAST/Module/module.py-samples/testAST/Module/module.uml] PASSED         [ 18%]
tests/test_UMLConverter.py::test_getSetFileList PASSED                                                                  [ 20%]
tests/test_UMLConverter.py::test_getCode PASSED                                                                         [ 21%]
tests/test_UMLConverter.py::test_getSetOutput PASSED                                                                    [ 22%]
tests/test_UMLConverter.py::test_getSetLanguage PASSED                                                                  [ 24%]
tests/test_UMLConverter.py::test_getSetExtension PASSED                                                                 [ 25%]
tests/test_UMLConverter.py::test_getSetClassList PASSED                                                                 [ 27%]
tests/test_UMLConverter.py::test_getSetImports PASSED                                                                   [ 28%]
tests/test_file.py::test_getSetFileName PASSED                                                                          [ 29%]
tests/test_file.py::test_getSetData PASSED                                                                              [ 31%]
tests/test_file.py::test_readFileNotFoundError PASSED                                                                   [ 32%]
tests/test_file.py::test_readAndAnalyze PASSED                                                                          [ 33%]
tests/test_file.py::test_write PASSED                                                                                   [ 35%]
tests/test_jsAST.py::test_AST[samples/JavaScript_Samples/Animal/Animal.js-samples/JavaScript_Samples/Animal/Animal.txt] PASSED [ 36%]
tests/test_jsAST.py::test_AST[samples/JavaScript_Samples/Animal/Cat.js-samples/JavaScript_Samples/Animal/Cat.txt] PASSED [ 37%]
tests/test_jsAST.py::test_AST[samples/JavaScript_Samples/School/Person.js-samples/JavaScript_Samples/School/Person.txt] PASSED [ 39%]
tests/test_jsAST.py::test_AST[samples/JavaScript_Samples/School/Student.js-samples/JavaScript_Samples/School/Student.txt] PASSED [ 40%]
tests/test_jsAST.py::test_AST[samples/JavaScript_Samples/School/Teacher.js-samples/JavaScript_Samples/School/Teacher.txt] PASSED [ 41%]
tests/test_jsAST.py::test_setGetTree PASSED                                                                             [ 43%]
tests/test_jsAST.py::test_setGetDataList PASSED                                                                         [ 44%]
tests/test_line.py::test_getIndentation PASSED                                                                          [ 45%]
tests/test_line.py::test_getData PASSED                                                                                 [ 47%]
tests/test_line.py::test_getRawData PASSED                                                                              [ 48%]
tests/test_line.py::test_getIndentationLevel PASSED                                                                     [ 50%]
tests/test_markdown.py::test_Markdown PASSED                                                                            [ 51%]
tests/test_pyAST.py::test_AST[samples/testAST/AnnAssign/arrayAnnAssign.py-samples/testAST/AnnAssign/arrayAnnAssign.txt] PASSED [ 52%]
tests/test_pyAST.py::test_AST[samples/testAST/AnnAssign/attribAnnAssign.py-samples/testAST/AnnAssign/attribAnnAssign.txt] PASSED [ 54%]
tests/test_pyAST.py::test_AST[samples/testAST/AnnAssign/complexAnnAssign.py-samples/testAST/AnnAssign/complexAnnAssign.txt] PASSED [ 55%]
tests/test_pyAST.py::test_AST[samples/testAST/AnnAssign/simpleAnnAssign.py-samples/testAST/AnnAssign/simpleAnnAssign.txt] PASSED [ 56%]
tests/test_pyAST.py::test_AST[samples/testAST/AnnAssign/typeAnnAssign.py-samples/testAST/AnnAssign/typeAnnAssign.txt] PASSED [ 58%]
tests/test_pyAST.py::test_AST[samples/testAST/Assign/mutipleAssign1.py-samples/testAST/Assign/mutipleAssign1.txt] PASSED [ 59%]
tests/test_pyAST.py::test_AST[samples/testAST/Assign/mutipleAssign2.py-samples/testAST/Assign/mutipleAssign2.txt] PASSED [ 60%]
tests/test_pyAST.py::test_AST[samples/testAST/Assign/simpleAssign.py-samples/testAST/Assign/simpleAssign.txt] PASSED    [ 62%]
tests/test_pyAST.py::test_AST[samples/testAST/ClassDef/complexClass.py-samples/testAST/ClassDef/complexClass.txt] PASSED [ 63%]
tests/test_pyAST.py::test_AST[samples/testAST/ClassDef/inheritedClass.py-samples/testAST/ClassDef/inheritedClass.txt] PASSED [ 64%]
tests/test_pyAST.py::test_AST[samples/testAST/ClassDef/simpleClass.py-samples/testAST/ClassDef/simpleClass.txt] PASSED  [ 66%]
tests/test_pyAST.py::test_AST[samples/testAST/FunctionDef/argsFun.py-samples/testAST/FunctionDef/argsFun.txt] PASSED    [ 67%]
tests/test_pyAST.py::test_AST[samples/testAST/FunctionDef/complexFun.py-samples/testAST/FunctionDef/complexFun.txt] PASSED [ 68%]
tests/test_pyAST.py::test_AST[samples/testAST/FunctionDef/nestedFunctions.py-samples/testAST/FunctionDef/nestedFunctions.txt] PASSED [ 70%]
tests/test_pyAST.py::test_AST[samples/testAST/FunctionDef/returnFun.py-samples/testAST/FunctionDef/returnFun.txt] PASSED [ 71%]
tests/test_pyAST.py::test_AST[samples/testAST/FunctionDef/simpleFun.py-samples/testAST/FunctionDef/simpleFun.txt] PASSED [ 72%]
tests/test_pyAST.py::test_AST[samples/testAST/Import/multipleImport.py-samples/testAST/Import/multipleImport.txt] PASSED [ 74%]
tests/test_pyAST.py::test_AST[samples/testAST/Import/simpleImport.py-samples/testAST/Import/simpleImport.txt] PASSED    [ 75%]
tests/test_pyAST.py::test_AST[samples/testAST/ImportFrom/complexImportFrom.py-samples/testAST/ImportFrom/complexImportFrom.txt]
 PASSED [ 77%]
tests/test_pyAST.py::test_AST[samples/testAST/ImportFrom/importFrom.py-samples/testAST/ImportFrom/importFrom.txt] PASSED [ 78%]
tests/test_pyAST.py::test_AST[samples/testAST/ImportFrom/longImport.py-samples/testAST/ImportFrom/longImport.txt] PASSED [ 79%]
tests/test_pyAST.py::test_AST[samples/testAST/Module/module.py-samples/testAST/Module/module.txt] PASSED                [ 81%]
tests/test_pyAST.py::test_setGetTree PASSED                                                                             [ 82%]
tests/test_pyAST.py::test_setGetDataList PASSED                                                                         [ 83%]
tests/test_pythonNode.py::test_setgetNodeType PASSED                                                                    [ 85%]
tests/test_pythonNode.py::test_setgetName PASSED                                                                        [ 86%]
tests/test_pythonNode.py::test_setgetValue PASSED                                                                       [ 87%]
tests/test_pythonNode.py::test_setgetArgs PASSED                                                                        [ 89%]
tests/test_pythonNode.py::test_setgetBody PASSED                                                                        [ 90%]
tests/test_pythonNode.py::test_addArg PASSED                                                                            [ 91%]
tests/test_pythonNode.py::test_addBody PASSED                                                                           [ 93%]
tests/test_pythonNode.py::test_toString PASSED                                                                          [ 94%]
tests/test_pythonNode.py::test_toStringBodyException PASSED                                                             [ 95%]
tests/test_searcher.py::test_lookForFiles PASSED                                                                        [ 97%]
tests/test_searcher.py::test_getFileList PASSED                                                                         [ 98%]
tests/test_searcher.py::test_fetDirList PASSED                                                                          [100%]

===================================================== 74 passed in 7.69s ======================================================
```


## Coverage report

```py
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
app/__init__.py                                  0      0   100%
app/modules/ast_module/AST.py                   48     11    77%
app/modules/ast_module/__init__.py               0      0   100%
app/modules/ast_module/jsAST.py                152     26    83%
app/modules/ast_module/line.py                  29      0   100%
app/modules/ast_module/pyAST.py                384     39    90%
app/modules/ast_module/pythonNode.py            59      0   100%
app/modules/file_module/__init__.py              0      0   100%
app/modules/file_module/file.py                102     22    78%
app/modules/file_module/markdown.py            104      3    97%
app/modules/file_module/searcher.py             26      0   100%
app/modules/interface_module/__init__.py         0      0   100%
app/modules/interface_module/interface.py      108     89    18%
app/modules/metric_module/__init__.py            0      0   100%
app/modules/metric_module/metric.py            122     90    26%
app/modules/metric_module/metricClass.py       123     52    58%
app/modules/metric_module/metricPackage.py      72     34    53%
app/modules/uml_module/UMLConverter.py         204     57    72%
app/modules/uml_module/__init__.py               0      0   100%
app/modules/uml_module/translator.py           131     26    80%
app/modules/utils.py                             6      0   100%
tests/__init__.py                                0      0   100%
tests/test_UMLConverter.py                      57      0   100%
tests/test_file.py                              41      2    95%
tests/test_jsAST.py                             18      0   100%
tests/test_line.py                              17      0   100%
tests/test_markdown.py                          28      2    93%
tests/test_pyAST.py                             19      0   100%
tests/test_pythonNode.py                        58      0   100%
tests/test_searcher.py                          15      0   100%
tests/utils.py                                  39      0   100%
----------------------------------------------------------------
TOTAL                                         1962    453    77%
```