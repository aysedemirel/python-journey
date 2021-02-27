import re

# find() and re.search() 
text = "From: Ayse, Loves"
if re.search('From:',text):
    print('It is true')
else:
    print('It is false')
if text.find('Ayse') >= 0:
    print('Ayse')
    
# startswith and re.search(^)
text = "From: Ayse, Loves"
if re.search('^From:',text):
    print('It is true')
else:
    print('It is false')  
if text.startswith('From:'):
    print('Startswith')
    
x = 'My favorite numbers are 4 and 7'
y = re.findall('[0-9]+',x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
y = re.findall('^F.+?:',x)
print(y)
x = 'aysedemirel@gmail.com'
y = re.findall('\S+@\S+',x)
print(y)
x = 'From: ayse@gmail.com'
y = re.findall('From: (\S+@\S+)',x)
print(y)

text = 'From aysedemirel@gmail.com Sat Jan 5 03:23:34 2008'
words = text.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)

text = 'From aysedemirel@gmail.com Sat Jan 5 03:23:34 2008'
y = re.findall('@([^ ]*)', text)
print(y)

    