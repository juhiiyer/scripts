import re
text = 'Google Chapter 22 - The Production Environment at 456 Apple'
result = re.findall(r'C\W+',text)
print (result)