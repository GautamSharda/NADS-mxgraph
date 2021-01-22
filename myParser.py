#imports
from lxml import etree

#parsing the XML file
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse('hardware.xml', parser=parser)

#Creating a root
root = tree.getroot()

#Defining key elements
miniSim = root[0]
HardwareInterface = miniSim[0]
Devices = HardwareInterface[0]

#Getting the device info
device1 = Devices[0]
device1Name = device1.get("name")
device1Ports = device1[2]

#for sink in device1Ports.iter(device1Ports[0].tag, device1Ports[11].tag):
    #print(sink.get("name"))  



#for element in port.iter("Source")-- This is very powerful
#can add elements using tostring -- This is very useful
# https://lxml.de/tutorial.html





