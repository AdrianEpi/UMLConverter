class NewClass():
	
	var1: str
	var2: int

	def __init__(self, v1, v2):
		self.setVar1(v1)
		self.setVar2(v2)


	def getVar1(self) -> str:
		return self.var1


	def getVar2(self) -> int:
		return self.var2 

	def setVar1(self, v1):
		self.var1 = v1

	def setVar2(self, v2):
		self.var2 = v2

