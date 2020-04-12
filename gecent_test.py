import gevent

def foo(a,b):
	print("a = %d,b = %d"%(a,b))
	gevent.sleep(2)
	print("Runing foo again")

def bar():
	print("Runing int bar")
	gevent.sleep(3)
	print("Runing bar again")

#生成协程对象
ge1 = gevent.spawn(foo,1,2)
ge2 = gevent.spawn(bar)
gevent.joinall([ge1,ge2])
print("---------------")