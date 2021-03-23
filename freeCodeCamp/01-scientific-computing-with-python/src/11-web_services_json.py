import json

################ JSON EXAMPLE #########################

data = '''{
        "name" : "Ayse",
        "phone" : {
            "type" : "intl",
            "number" : "123456789"
            },
        "email" : {
            "hide" : "yes"
            }            
        }'''

info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])

################ JSON SECOND EXAMPLE ########################

data_input = '''[
        {
            "id"   : "001",
            "x"    : "2",
            "name" : "Ayse"
        },
        {
            "id"   : "002",
            "x"    : "5",
            "name" : "Mustafa"
        }           
    ]'''

info = json.loads(data_input)
print("User count: ",len(info))
print("First name: ", info[0]["name"])
for item in info:
    print("Name: ",item["name"])
    print("Id: ",item["id"])
    print("Attribute: ",item["x"])