# Collections: List and Dictionary
# List -> A linear collection of values that stay in order
# Dictionary -> A bag of values, each with its own label

# DICTIONARIES
# Dictionaries are Python's most powerful data collection
# Dictionaries allow us to do fast database-like operations in Python
# Dictionaries in Python is like "Properties or Map or Hashmap - Java"


purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

ages_dict = {}
print(ages_dict)
ages_dict = {'ayse' : 1, 'mustafa' : 2}
print(ages_dict)

counts = dict()
names = ['ayse', 'mustafa', 'ahmet']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

x = counts.get('ayse', 1)
print(x)

counts = dict()
print('Enter lines of text: ')
line = input('')
words = line.split()
print('Words: ',words)
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts: ', counts)

name_age = {'ayse' : 1, 'mustafa' : 2}
print(list(name_age))
print(name_age.keys())
print(name_age.values())
print(name_age.items()) # key and value

name_age = {'ayse' : 1, 'mustafa' : 2}
for name,age in name_age.items():
    print(name, age)

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
        
        thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
# get(keyname,value)
# keyname -> Required. The keyname of the item you want to return the value from
# value -> Optional. A value to return if the specified key does not exist. Default value None
print(thisdict.get('colors'))
 
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
thisdict.pop("electric")
print(thisdict)
thisdict.clear()
print(thisdict)      

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]) 
        

