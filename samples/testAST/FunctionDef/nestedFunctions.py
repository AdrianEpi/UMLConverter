def fun(var1: int) -> int:
	num2 = 2
	def fun2(var2: int):
		num3 = 3
		def fun3(var3: int):
			return var1 + var2 + var3
		return fun3(num3)

	return fun2(num2)

fun(1) # 1 + 2 + 3 = 6