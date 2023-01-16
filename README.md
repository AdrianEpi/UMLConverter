# UMLConverter
Repository for TFG code

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