#/usr/bin/python3.5
'''d = {}
li = [1, 2, 3]
v = 'abc'
print (d.fromkeys(li,v))
e = d.fromkeys(li,v)
e.pop(1)'''

#pop(k): We should pass a key as a parametre. Remove and return a value
#popitem(): this is a default no parametre. It removes and returns a parametre at the end.
'''x = {}
x = {2:'x'}
#x = {3:'f'}'''
# update()
#It is used to add a dictionary to an existing dictionary.existing

#setdefault(k,v): set default key...

'''dl = {1: 'a', 2: 'b'}
dl.setdefault(3,'c')
print (dl)
adds new values to a dictionary!'''
'''d = [1, 2]
d = {}'''
#e = {1:'a', 2:'b', 3:'c'}
# indexing and slicing cannot be applied for dictionaries.
#set: It is a data structure with a collection of heterogeneos elements.
# Imutable (frozen set)
#mutable (set)
# no duplicates 
#insertion not order not preserved.
#insertion order not preserved
# dynamic
#no indexing

#creatinf set
# -----------
#s = {1, 2, 3, 1, 2, 3, 'a' ,10.5}
#print (s)
'''set()
create a new set
also used to create data structures into sets!
'''
'''files
--->methods of sets
add()
remove()
discard()
copy()
pop()
update()
'''
#discard('a', s)
#something like this.
'''s = set()
s.add(12)
s.add(53)
s.add(45)
s.add(474)
print (s)

s.remove(12)
print(s)
#s2 = s.copy()
s.pop()
print(s)
s.update([1, 2, 3, 4, 5])
print (s)'''

'''mathamatical operations on sets
-union(|)
-intersection(&)
-difference(-)
-symetric_difference()'''
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print (s1.union(s2))
s1.difference_update(s2)
print (s1)
#output = {1, 2}
print (s1.symmetric_difference_update(s2))
#all the elements should exist in the other element
print (s1.issuperset(s2))
# output = true, so it is a boolean!
print (s1.isdisjoint(s2))
# this is also a boolean
fs = frozenset({1, 2, 3, 4})
for i in fs:
	print (i)
bts = {1, 2, 3, 4, 5}
# display all prime no.
print (bts)
#just a string for incase
print (len(bts))
print (bts not in fs)
print (bts in fs)
#s1.remove(None)
# the code above is not possible as None is a key error
s = {1, 2, 3, 4, 5}
#if(None in s):
	#print(s)
for i in s:
	x = i
	a = 1 
	f = 0
	while(a<=x):
		if(x%a==0):
			f = f + 1
		a = a + 1
	if (f == 2):
	       print (x)
# break
# continue
# pass
#s = [1, 2, 3, 4, 5]
#key ---->3
#flag = false
#break the exicution and then com out
s = [1, 2, 3, 4, 5]
key = int(input('enter key'))
flag = False
x = 1
for i in s:
	if(x<=3):
		x = x + 1
		continue
	print(i)	
	
'''if(flag):
	print('element found')
else:
	print('element not found')'''

x = 5
y = 10
if(x>y):
	pass
else:
	print('hey y is big')


