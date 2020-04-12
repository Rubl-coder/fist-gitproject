from socket import *
import os,sys
from threading import *
import traceback

HOST = ''
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handler(connfd):
	print("Connect from",connfd.getpeername())
	while True:
		data = connfd.recv(1024)
		if not data:
			break
		print(data.decode())
		connfd.send(b'Recive your message')
	connfd.close()
#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#等待客户端请求
while True:
	try:
		#connfd是全局变量，如果不传参，表示服务端连接的永远是最新的客户端，以前的被覆盖了
		connfd,addr = s.accept()
	except KeyboardInterrupt:
		s.close()
		print("服务端退出")
		break
	except Exception:
		traceback.print_exc()
		continue

	t = Thread(target=handler,args=(connfd,))

	t.setDaemon(True)
	t.start()
	#t.join()是阻塞函数，用到这里会一直阻塞，不能连接第二个客户端
	#所以用setDaemon

