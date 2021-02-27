sample_text = open('.\sample.txt','r')
all_file = sample_text.read()
print(len(all_file))
print(sample_text)


count = 0
sample_text = open('.\sample.txt','r')
for text in sample_text:
    print(text)
    count = count + 1
print("Counting lines: " , count)


try:
    sample_text = open('.\sample.txt','r')
except:
    print("File cannot be found: ", sample_text)
    quit()

for line in sample_text:
    line  = line.rstrip()
    if not 'ipsum' in line:
        print('no ipsum: ',line )
        print('\n')
    if not line.startswith('Lorem'):
        continue
    print("Line with lorem: ",line)
    print('\n')