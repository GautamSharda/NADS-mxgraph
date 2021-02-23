from flask import Flask, render_template, url_for, jsonify
import json, jsons, jsonpickle
from lxml import etree
import numpy as np
from array import array

#parsing the XML file
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse('hardware.xml', parser=parser)

#Creating a root
root = tree.getroot()
#Defining key elements
miniSim = root[0]
hardwareInterface = miniSim[0]
devices = hardwareInterface[0]

app = Flask(__name__)

@app.route('/')
def home():
    myList = []
    for x in devices:
        myList.append(x.get("name"))
    return render_template("index.html")
    return jsonify(myList)



@app.route('/devices<int:index>')
def device(index):
    device = devices[index]
    
    return render_template("template.html", deviceName=deviceName)


if __name__== "__main__":
    app.run()

