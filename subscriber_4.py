import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "RANDOM_VALUE")  # subscribe to TIME messages
s.setsockopt_string(zmq.SUBSCRIBE, "COUNTER_MESSAGE")  # subscribe to TIME messages

while True:
	time = s.recv()   # receive a message
	print (bytes.decode(time))
