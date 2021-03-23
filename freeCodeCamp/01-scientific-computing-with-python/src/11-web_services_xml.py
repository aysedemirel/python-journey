import xml.etree.ElementTree as ET

################ XML EXAMPLE #########################

data = '''<person>
        <name>Ayse</name>
        <phone type="intl">1234567 </phone>
        <email hide="yes"/>
        </person>'''
        
tree=ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))

################ XML SECOND EXAMPLE #########################

input='''<stuff>
             <users>
             <user x="2">
                 <id>001</id>
                 <name>Ayse</name>
             </user>
             <user x="7">
                 <id>009</id>
                 <name>Mustafa</name>
             </user>
             </users>
          </stuff>'''
          
stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count: ',len(lst))
for item in lst:
    print('Name: ',item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attribute: ', item.get('x'))
