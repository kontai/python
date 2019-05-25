import xml.etree.ElementTree as ET
tree=ET.parse("xml_lesson")
root=tree.getroot()
#print(root.tag)

for i in root:
    print(i.attrib)
