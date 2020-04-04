# OPCUA_NodeBrowser

This is a simple command line tool, to browse the Nodes of a OPC UA Server.

## Installation

To use this script, make sure you have installed the python module *opcua* on your computer. You can install it with the following command:

~~~bash
sudo pip install opcua
~~~

## Usage

This repository contains two python files:
- node.py: Some usefull classes for handling OPC UA Nodes. You can use it for our own python scripts
- NodeBrowser.py: A simple command line tool, to browse and display the Nodes of a OPC UA Server.

Both scripts are using Python 3. 

To start the NodeBrowser, just type the following command:

~~~bash
python NodeBrowser.py
~~~

After that the script asks you for the Ip and port of the OPC UA Server. You can take default values by pressing Enter. After connecting to it, the script will browse through the namespaces of the Server and then will display the server' structure. 
