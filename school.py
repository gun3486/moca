import xml.etree.ElementTree as ET
tree = ET.parse('C:\Users\user\Documents\Github\moca\급식식단정보')
root = tree.getroot()
print(root.tag)
for i in root:
    print(i.tag, i.text)
    