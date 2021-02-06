from flask import Flask, render_template, url_for
from jinja2 import Markup
from myParser import device1Name, devices, tree, etree

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/devices<int:index>')
def device(index):
    device = devices[index]
    deviceName = device.get("name")
    deviceKind = device.get("kind")
    deviceID = device.get("ID")

    deviceSettings = device[0]
    deviceSettingsTag = deviceSettings.tag
    
    deviceSetting1 = deviceSettings[0]
    deviceSetting1Tag = deviceSetting1.tag
    deviceSetting1Name = deviceSetting1.get("name")
    deviceSetting1Type = deviceSetting1.get("type")#unsigned int?
    deviceSetting1Unit = deviceSetting1.get("unit")
    deviceSetting1Data = deviceSetting1.text
    
    devicePorts = device[1]
    devicePortsTag = devicePorts.tag
    
    devicePort1 = devicePorts[0]
    devicePort1Tag = devicePort1.tag
    devicePort1Name = devicePort1.get("name")
    devicePort1Type = devicePort1.get("type")
    devicePort1Unit = devicePort1.get("unit")
    
    devicePort2 = devicePorts[1]
    devicePort2Tag = devicePort2.tag
    devicePort2Name = devicePort2.get("name")
    devicePort2Type = devicePort2.get("type")
    devicePort2Unit = devicePort2.get("unit")

    devicePort3 = devicePorts[2]
    devicePort3Tag = devicePort3.tag
    devicePort3Name = devicePort3.get("name")
    devicePort3Type = devicePort3.get("type")
    devicePort3Unit = devicePort3.get("unit")

    devicePort4 = devicePorts[3]
    devicePort4Tag = devicePort4.tag
    devicePort4Name = devicePort4.get("name")
    devicePort4Type = devicePort4.get("type")
    devicePort4Unit = devicePort4.get("unit")

    return render_template("template.html", deviceName=deviceName, deviceKind=deviceKind, deviceID=deviceID, settings=deviceSettingsTag, setting1Name=deviceSetting1Name, setting1Type=deviceSetting1Type, setting1Unit=deviceSetting1Unit, setting1Data=deviceSetting1Data, port1Tag=devicePort1Tag, port1Name=devicePort1Name, port1Type=devicePort1Type, port1Unit=devicePort1Unit)


if __name__== "__main__":
    app.run()
