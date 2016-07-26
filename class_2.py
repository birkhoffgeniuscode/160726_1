#coding=utf-8
#使用super()调用父类__init__方法：
class Fruit(object):
	def __init__(self):
		print 'parent'

class Apple(Fruit):
	def __init__(self):
		super(Apple,self).__init__()  #在Apple类的__init__中调用super,self类的对象是Apple类的实例,super调用父类的__init__
		print 'child'

if __name__ == '__main__':
	Apple()


#单例模式
class singleton(object):
	__instance = None

	def __init__(self):
		pass
	def __new__(cls,*argu,**kwd):
		if singleton.__instance is None:
			singleton.__instance = object.__new__(cls,*argu,**kwd) # cls表示当前类的实例
		return singleton.__instance
#此时__instance还不存在，可以用 print singleton.__instance来测试，会显示无此特性
obj1=singleton()
obj2=singleton()
singleton.__instance = 'value1' #此时才有了singleton.__instance的值
print obj1.__instance , obj2.__instance
print obj1 is obj2  #判断这两个实例是不是相等


#8.4.1 继承
class Fruit_1:
	def __init__(self,color):
		self.color = color    #父类公有属性
		print  "fruit's color is : %s " %self.color 
	def grow(self):           #父类公有方法
		print "8.4.1 grow..."

class Apple_1(Fruit_1):					#如果父类定义了__init__方法，子类必须显式调用父类的__init__方法，如果子类需要扩展父类的行为，可以添加__init__方法
	def __init__(self,color):
		Fruit_1.__init__(self,color)		#显式调用父类的__init__方法
		print "8.4.1apple's color : %s " %self.color		#继承父类的属性color

class Banana_1(Fruit_1):
	def __init__(self,color):
		Fruit_1.__init__(self,color)
		print "8.4.1banana's color : %s" %self.color 
	def grow(self):							#定义了和父类同名的方法grow,并且覆盖了父类的grow
		print "8.4.1banana grow..."

if __name__ == '__main__':
	apple = Apple_1("red")				#由于Apple继承了Fruit,所以先输出父类的信息，再输出子类的信息
	apple.grow()
	banana=Banana_1("yellow")
	banana.grow()


#8.4.3 多态性
class Fruit_2:
	def __init__(self, color =None):
		self.color = color 
class Apple_2(Fruit_2):
	def __init__(self,color = "red"):
		Fruit_2.__init__(self,color)
class Banana_2(Fruit_2):
	def __init__(self,color="yellow"):
		Fruit_2.__init__(self,color)
class FruitShop:
	def sellFruit(self,fruit):			#参数fruit接收Apple_2,Banana_2类的实例
		if isinstance(fruit,Apple_2):	#判断fruit的类型
			print "sell apple"
		if isinstance(fruit,Banana_2):
			print "sell banana"
		if isinstance(fruit,Fruit_2):
			print "sell fruit"
if __name__ == '__main__':
	shop = FruitShop()
	apple = Apple_2("red")
	banana = Banana_2("yellow")
	shop.sellFruit(apple)				#参数的多态性，传递apple的对象
	shop.sellFruit(banana)				#传递banana的对象


#8.4.4 多重继承
   #新测试修改












