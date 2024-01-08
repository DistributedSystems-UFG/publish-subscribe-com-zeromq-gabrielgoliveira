import zmq, time
import random
import uuid
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)                     # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT                      # how and where to communicate
s.bind(p)                                       # bind socket to the address

static_message = "Hello, Friend !!"
count_msg = 0
while True:
	time.sleep(5)                                  # wait every 5 seconds
	random_value = random.randint(1, 100)

	# Data/Hora atual
	msg = str.encode("TIME " + time.asctime())

	# Obter um número aleatório
	msg2 = str.encode("RANDOM_VALUE " + str(random_value))
	
	# Obter um valor estático
	msg3 = str.encode("STATIC_VALUE " + static_message)

	# Um contador de quantas mensagens o publisher enviou
	count_msg = count_msg + 1
	msg4 = str.encode("COUNTER_MESSAGE " + str(count_msg))
	
	# Obter uuid
	msg5 = str.encode("GET_UUID " + str(uuid.uuid4()))

	s.send(msg) # publish the TIME
	s.send(msg2) # publish the RANDOM_VALUE
	s.send(msg3) # publish the STATIC_VALUE
	s.send(msg4) # publish the COUNTER_MESSAGE
	s.send(msg5) # publish the GET_UUID
