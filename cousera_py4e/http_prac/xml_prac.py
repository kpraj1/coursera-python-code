import xml.etree.ElementTree as ET

#example 1 -- complex tag = series of simple tags in this case
# input_data = '''<stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <!-- multi argument user -->
#         <user x="7" y="9">
#             <id>009</id>
#             <name>Raj</name>
#         </user>
#         <user>
#             <id>007</id>
#             <name>Bond</name>
#         </user>
#     </users>
# </stuff>'''
#
# stuff = ET.fromstring(input_data)
# #this is giving list of user child tags under users parent tag
# lst = stuff.findall('users/user')
# print("user count: ",len(lst))
# print("-"*40)
# # for getting text content of child use find('childtagname').text
# # for getting respective attribute value use get("attribute")
# for item in lst:
#     print('Name:',item.find('name').text)#giving text content of name
#     print('Id:', item.find('id').text)#giving text content of id
#     print('Attribute:', item.get("x"))#getting attribute x of user
#     print("-" * 60)

#example 2 -- simple tag
# data = '''<person>
# <name>Chuck</name>
# <phone type="intl">
# +91 9989767898
# </phone>
# <email hide="yes"/>
# </person>
# '''
#
# tree = ET.fromstring(data)
# print('Name: ',tree.find('name').text)
# print('Attr: ',tree.find('email').get('hide'))



#deserialization example
xml_data = '''
<student>
  <name>Alice</name>
  <id>123</id>
  <marks>
    <mark>85</mark>
    <mark>90</mark>
    <mark>92</mark>
  </marks>
</student>
'''


root = ET.fromstring(xml_data)

name = root.find('name').text
id = int(root.find('id').text)
marks = [int(m.text) for m in root.find('marks').findall('mark')]

student_back = {
    "name": name,
    "id": id,
    "marks": marks
}

print(student_back)
