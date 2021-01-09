from xml.dom import minidom as md 
my_doc = md.parse('/500gb1/juhiPython/scripts/python/icecream.xml')
print(my_doc.nodeName)
print(my_doc.firstChild.tagName)
items = my_doc.getElementsByTagName('item')
print(items[0].attributes['name'].value)

for ele in items:
	print(ele.attributes['name'].value)
print(items[0].firstChild.data)
print(items[2].childNodes[0].data)

print(items[1].childNodes[0].data)	
for it in items:
	print(it.firstchild.data)