class base1():
	pass

class base2():
	pass

class meta():
	pass 
	
class Foo(base1, base2, metaclass=meta):
    pass