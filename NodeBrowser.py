######################################################################
#
# Filename: NodeBrowser.py
# Author: Johannes4Linux
# Date: 04.04.2020
#
# A simple command line tool to browse through all the nodes 
# in an OPC UA Server
#
######################################################################

from node import *
from opcua import Client
import sys

hostname = input("Enter OPC UA Server's address [default: localhost]: ")
if hostname == "":
    hostname = "localhost"
port = input("Enter OPC UA Server's port number [default 8080]: ")
if port == "":
    port = 8080
else:
    try:
        port = int(port);
    except:
        print("Invalid Port Number!")
        sys.exit(-1)

start = input("Select start point: 1: Objects Node, 2: Root Node [default: 1]: ")
if start == "":
    start = 1
else:
    try:
        start = int(start)
        if start not in [1,2]:
            raise ValueError
    except:
        print("Invalid Option!")
        sys.exit(-1)
        
try:
    client = Client("opc.tcp://"+hostname+":"+str(port))
    client.connect()
except:
    print("Client couldn't connect to Server at " + "opc.tcp://"+hostname+":"+str(port))
    sys.exit(-1)


starting_points={1:client.get_objects_node, 2:client.get_root_node}
print("Connected to OPC UA server!")
base = Node(starting_points[start](), None)
struct = ServerNodes()
print("Start browsing server's namespace. This will take some time...")
struct.build_list(base)
print("Finished browsing for nodes")
struct.show_hierarchie()

client.close_session()
