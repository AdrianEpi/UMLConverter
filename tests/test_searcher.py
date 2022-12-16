# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_searcher.py
#   @Author:             Adrian Epifanio
#   @Date:               2022-12-12 08:38:26
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2022-12-12 11:02:03
#   @Description:        Tests for app/file_module/searcher.py


from app.modules.file_module.searcher import Searcher
import pytest

path = "app/modules/file_module"

s = Searcher()
filesExpected = ['app/modules/file_module/file.py', 'app/modules/file_module/searcher.py', 'app/modules/file_module/__init__.py']
dirExpected = ['tests', 'tests/testFiles']


def test_lookForFiles():
	assert(s.lookForFiles(path, ".py").sort() == filesExpected.sort())


def test_getFileList():
	assert(s.getFileList().sort() == filesExpected.sort())


def test_fetDirList():
	s2 = Searcher()
	path = "tests"
	s2.lookForFiles(path, ".py")
	assert(s2.getDirList().sort() == dirExpected.sort())
