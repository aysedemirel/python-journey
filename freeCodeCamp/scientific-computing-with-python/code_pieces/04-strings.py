hello = "Hello"
world = "World"
hello_world = hello + " " + world
print(hello_world)

num = '123'
num = int(num) + 1 
print(num)

text = "Sample Text For Python"
print(text[0:6])
print(text[7:11])
print(text[12:15])
print(text[16:22])

fruit = "banana"
print('n' in fruit)
print('m' in fruit)

print("Hello Wolrd".lower())
print("Hello Wolrd".upper())
print("hello world".capitalize())
hello = "Hello World"
print(type(hello))
dir(hello)


str = "Hello world"
isFound = str.find('wo') 
print(isFound)


str = "Hello Ayse"
print(str)
replace_str = str.replace("Ayse","Mustafa")
print(replace_str)


str = "     Hello World       "
print(str.lstrip())
print(str.rstrip())
print(str.strip())


str = "Please have a nice day"
print(str.startswith('Please'))
print(str.startswith('please'))


data = "hello there,i'm Ayse"
comma = data.find(',')
empty = data.find(' ',comma)
text = data[comma+1: empty] 
print(comma)
print(empty)
print(text)