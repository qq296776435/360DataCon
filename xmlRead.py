import xml.etree.cElementTree as ET


class StandardObj:
    def __init__(self):
        self.attributes = {}
        self.apiArg_list = []
        self.exInfo_list = []


standardObj = StandardObj()
standardObjList = []
tree = ET.parse('000ad090d3a78850f0ecd2c2ab9ca83626d155ebf958e63c7bfb7b5528caddf8.xml')
root = tree.getroot()
element = root[0][0][0][1]

for element in root[0][0][0][1]:
    standardObj.attributes = element.attrib
    apiArgObj = element[0]
    apirArgCount = apiArgObj.__len__()
    if apirArgCount > 0:
        for i in range(0, apirArgCount):
            standardObj.apiArg_list.append(apiArgObj[i].attrib['value'])
    exInfoObj = element[1]
    exInfoCount = exInfoObj.__len__()
    if exInfoCount > 0:
        for i in range(0, exInfoCount):
            standardObj.exInfo_list.append(exInfoObj[i].attrib['value'])
    standardObjList.append(standardObj)





