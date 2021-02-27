number_list = [1,2,3,4]
string_text = ['a', 'b', 'c']

print(number_list)
print(string_text)

number_list[2] = 22
print(number_list)

mix_list = [1, 2, 'one', 'two']
print(mix_list)

print(range(4))

a = [1, 2]
b = [3, 4]
c = a + b
print(c)
print(c[1:])
print(c[:2])
print(c[:])

x  = list()
print(type(x))
x.append('a')
x.append('b')
x.append(2)
if 2 in x:
    print(x)
if 3 not in x:
    print('3 is not in x')
    
name = ['Mustafa', 'Ahmet', 'Ayşe']
name.sort()
print(name)
print(name[2])

nums = [90,1,2,3,4,5,6,10,7]
print('min: ' , min(nums))
print('max: ' , max(nums))
print('sum: ', sum(nums))
print('average: ' , sum(nums) / len(nums))

word = 'With three words'
split_word = word.split()
print(split_word)