######################################################################
#
# Datei: node.py
# Autor: Johannes4Linux
# Datum: 22.11.2019
#
# Klassen & Funktionen, um den Namespace eines OPC UA Servers
# zu erforschen und alle Nodes zu finden
# 
######################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function
from opcua import ua

class Node:
    """Klasse macht eine OPC UA Node les- und nutzbar"""
    def __init__(self, node, parent, hierarchie=[0]):
        """Konstruktor initialisiert grundlegende Werte"""
        self.node=node
        self.parent=parent
        self.children=self.node.get_children()
        if parent==None:
            self.hierarchie=[0]
        else:
            self.hierarchie=hierarchie
        try:
            self.node_name=str(self.node.get_browse_name()).strip("QualifiedName(").strip(')')
        except:
            self.node_name=""
        try:
            self.node_value=self.node.get_value()
        except:
            self.node_value=None
        try:
            self.node_data_type=self.node.get_data_type()
        except:
            self.node_data_type=None

    def get_node_value(self):
        """Aktualisiere Node Value, falls vorhanden, und gib ihn zurueck"""
        try:
            self.node_value=self.node.get_value()
        except:
            self.node_value=None
        return self.node_value

    def write_value_only(self, value, type=None):
        """Schreibe den Wert einer Node ohne Timestamp"""
        datavalue=ua.DataValue(ua.Variant(value, type))
        self.node.set_attribute(ua.AttributeIds.Value, datavalue)


    def get_child_nr(self, nr):
        """Gebe ein Kind, falls vorhanden  der Node zurueck"""
        if nr < len(self.children):
            tmp=self.hierarchie[:]
            tmp.append(nr)
            return Node(self.children[nr], self, tmp)
        else:
            return None

node_list=[]
ebene=0
def get_tree(node):
    """suche alle Aeste des Baums ab der uebergebenen Node ab; node ist Objekt der Klasse Node"""
    node_list.append(node)
    if len(node.children) > 0:
        for i in range(len(node.children)):
            get_tree(node.get_child_nr(i))

class ServerNodes:
    """Klasse zum Erstellen und Anzeigen des Nodebaums"""
    def __init__(self):
        """Konstruktor erzeugt leere Node Liste"""
        self.node_list=[]

    def build_list(self, rootnode):
        """suche alle Aeste des Baumes ab der uebergebenen Node ab"""
        self.node_list.append(rootnode)
        if len(rootnode.children)>0:
            for i in range(len(rootnode.children)):
                self.build_list(rootnode.get_child_nr(i))

    def show_hierarchie(self):
        """Zeigt Hierarchie als Baum an"""
        element=0
        for i in self.node_list:
            print(str(element) + "\t\t" + "|"*(len(i.hierarchie)-2), end="")
            if len(i.hierarchie) != 1:
                print("+"+"--"*(len(i.hierarchie)-1), end="")
            print(i.node_name[i.node_name.find(":")+1:])
            element +=1
    def show_values():
        for i in self.node_list:
            tmp=i.get_node_value()
            if tmp != None:
                print(str(i.hierarchie)+"\t"+i.node_name+":\t"+str(tmp))


