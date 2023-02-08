# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               utils.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-01-31 13:15:46
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-07 10:38:02
#   @Description:        ...

# Program Languages
LANGUAGES = [
	'Python',
	'JavaScript'
]

# Program Comments
COMMENTS = {
	'Python': {
		'single': '#',
		'multiStart': '"""',
		'multiEnd': '"""'
	},
	'JavaScript': {
		'single': '//',
		'multiStart': '/*',
		'multiEnd': '*/'
	}
}

# Python node types
NODETYPES = [
	'Module(',
	'ClassDef(',
	'Import(',
	'ImportFrom(',
	'Assign(',
	'AnnAssign(',
	'AsyncFunctionDef(',
	'FunctionDef('
]

# JavaScript node types
JSNODETYPES = [
	'ClassDeclaration',
	'ExpressionStatement',
	'VariableDeclaration',
	'FunctionDeclaration',
	'MethodDefinition'
]

# Searcher excluded paths
EXCLUDEPATHS = [
	# Python
	'__pycache__',
	'__pypackages__',
	'.env',
	'env',
	'ENV',
	'env.back',
	'venv.back',
	'.venv',
	'venv',
	'docs',
	'samples',
	'examples',
	'tests',
	'test',
	'site',
	'.mypy_cache',
	'target',
	'htmlcov',
	'.tox',
	'.nox',
	'coverage',
	'.hypothesis',
	'.pytest_cache',

	# JavaScript
	'node_modules',
	'jspm_packages',
	'.nyc_output',
	'dist',
	'tmp',
	'out-tsc',
	'pids',
	'lib-cov',
	'coverage',
	'bower_components',
	'.npm',
	'bin'
]

UMLTHEMES = [
	'_none_',
	'carbon-gray',
	'crt-amber',
	'hacker',
	'reddress-lightblue',
	'cerulean-outline',
	'crt-green',
	'lightgray',
	'plain',
	'spacelab-white',
	'cloudscape-design',
	'cyborg-outline',
	'metal',
	'reddress-darkblue',
	'superhero-outline'
]