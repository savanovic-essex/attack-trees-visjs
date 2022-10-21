# coding=utf-8
import ast
import json
import os
import sys
import webbrowser

from pyvis.network import Network

attack_tree_net = Network(height="100%", width="50%", bgcolor="#222222", font_color="white", layout=True)

# JSON file
with open('attack_tree.json', 'r') as file:
    attack_tree = json.load(file)
    attack_tree = ast.literal_eval(json.dumps(attack_tree))

nodes = attack_tree['nodes']
at_nodes = []

for a in nodes:
    name = a['name']
    ID = str(a['id'])
    at_nodes.append(str(ID) + ':' + name)

attack_tree_net.barnes_hut()

for n in nodes:
    idNumber = n["id"]
    label = n["name"]
    attack_tree_net.add_node(str(idNumber), str(label), shape="box", title=label)

edges = attack_tree['edges']

for e in edges:
    toID = e['to']
    fromID = e['from']
    attack_tree_net.add_edge(str(fromID), str(toID), value=1)

attack_tree_net.hrepulsion(node_distance=160)
attack_tree_net.show_buttons(filter_=['edges'])

fileName = raw_input("Enter file name:")
print(fileName)
attack_tree_net.show(fileName + ".html")

url = os.path.join(sys.path[0], fileName + ".html")
print(url)
webbrowser.open("file://" + url, new=2)
