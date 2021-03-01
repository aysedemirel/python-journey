x = ['Ayse', 'Mustafa', 'Ahmet']
print(x)
x.sort()
print(x)
x.append('Deniz')
print(x)
x.reverse()
print(x)

(x,y) = (4, 'Ayse')
print(y)

d = dict()
d['ayse'] = 1
d['mustafa'] = 2
for (k,v) in d.items():
    print(k,v)
    
# First item is smaller than oter tuple's first item, it is true. After the second element, third element.
if((0,1,2)<(5,1,2)):
    print(True)
else:
    print(False)

d = {'c':1,'b':2}
print(d.items())
print(sorted(d.items()))
print(sorted(d))
print(sorted(d, reverse=True))


c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))

counts = { 'chuck' : 53 , 'annie' : 42, 'jan': 100}
lst = []
for key, val in counts.items():
    newtup = (val, key)
    print(newtup)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

