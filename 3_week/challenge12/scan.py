import socket
import sys
import getopt

try:
	opts, args = getopt.getopt(sys.argv[1:],'',['host=', 'port='])
except:
	print('Parameter Error')
	sys.exit()



if not len(opts) - 1:
	print('Parameter Error')
	sys.exit()


for opt, value in opts:

	if opt == '--host':
		if not len(value.split('.')) - 4:
			HOST = value
		else:
			print('Parameter Error')
			sys.exit()

	elif opt == '--port':
		value = value.split('-')
		if not len(value)-1:
			port_min = port_max = int(value[0])
			
		else:
			port_max = int(value[1])
			port_min = int(value[0])
	

for PORT in range(port_min,port_max+1):
	TCPCLINK = socket.socket()
	TCPCLINK.settimeout(0.1)
	addr = HOST, PORT
	if not TCPCLINK.connect_ex(addr):
		print(addr[1], ' open')
	else:
		print(addr[1], ' closed')
		