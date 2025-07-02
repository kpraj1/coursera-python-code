import json
# single data item
# data='''{
# "name":"chuck",
# "phone":{
# "type":"intl",
# "number":"+91 9090989778"
# },
# "email":{
# "hide":"yes"
# }
# }'''
#
# info = json.loads(data)
#
# print('Name:',info['name'])
# print('Hide:',info['email']['hide'])
# print('type:',info['phone']['type'])
# print('number:',info['phone']['number'])

#multiple data item
input_data = '''{
"comments": [
{
"id" :"001",
"x":"2",
"name":"chuck"
},
{
"id" :"007",
"x":"1",
"name":"bond"
},
{
"id" :"045",
"name":"hitman",
"x":"264"
}
]
}'''

info = json.loads(input_data)
print('user count: ',len(info["comments"]))
print("-"*30)
# print(info[0]["name"])
# print("-"*30)
# print(info[-1]["name"])


for item in info["comments"]:
    print("Name",item['name'])
    print("ID",item['id'])
    print("x: ",int(item['x'])+2)
    print("-" * 60)
