names = ['Ayse', 'Mustafa']
for name in names:
    print('name : ', name)
print("end of for")

for i in [2,3,4]:
   print(i)
print("end of for")

largest = -1
print('Before: ', largest)
for num in [9,41,12,3,74,15]:
    if num > largest :
        largest = num
    print(largest, num)
print('After : ', largest)

index = 0
print('Before:',index)
for thing in [9,41,12,3,74,15]:
    index = index + 1
    print(index, thing)
print('After:',index)

count = 0
sum = 0
for num in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + num
    print(count, sum, num)
print('After: ', count, sum, 'Average: ', sum/count)

for num in [9,41,12,3,74,15]:
    if num > 20:
        print("num: ", num)
print("end of for")

isFound = False
for num in [9,41,12,3,74,15]:
    if num == 3:
        isFound = True
    print(isFound, num)
print("After: ", isFound)
    
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(" total: ", tot,"\n number lenghts: ",num, "\n average:",tot/num)

banana = 'banana'
for letter in banana:
    print(letter)
print("Lenght: " , len(banana))

fruit = 'strawberry'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    
banana = 'banana'
count = 0
for letter in banana:
    if letter == 'a':
        count = count + 1 
print("number of a : ",count)
