number = 5
text = "sample text"

print(type(number),type(text))

input_text = input("Please enter a number : ")
number = int(input_text)
print("number: ",number)

# In python 3, all strings are unicode
# We don't have to add 'u' before string
str = u'你好 Ayşe'
print(str)