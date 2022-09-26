#webscraping --
#finding and filtering data from website using website tree {tags tree using beautiful soup}
# Beautiful Soup is a Python library for pulling data out of HTML and XML files, we will focus on HTML files. 
# This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML.
#  We can navigate the HTML as a tree and/or filter out what we are looking for.


import csv
from bs4 import BeautifulSoup as bsp
import requests
# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# soup=bsp(html,"html.parser")
# print(ob.prettify()) to get pretty object
# tag_obj=soup.h3
# # print(tag_obj.string) lebron james prints the string in the tag
# # print(tag_child['id'])
# tag_child=tag_obj.parent


# print(tag_child.attrs) #printing
# tag_sibling=tag_obj.next_sibling
# print(tag_sibling.next_sibling)

###############################################################################################################################################################

#Filters General
table_html="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = bsp(table_html, "html.parser")

####find_all fxn --- find_all(name, attrs, recursive, string, limit, **kwargs)//filter 1
res=(table_bs.find_all('tr'))
# for i in res:
#     print(i.td)

# for i,row in enumerate(res):
#     print("row",i)
#     cells=row.find_all('td')
#     for j,cell in enumerate(cells):
#         print('colunm',j,"cell",cell.string)

# list_input=table_bs.find_all(name=["tr", "td"])
# print(list_input)

z=(table_bs.find_all(id="flight"))
#We can find all the elements that have links to the Florida Wikipedia page
#list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")



#We can also use the `read_html` function to directly get DataFrames from a `url`.
dataframe_list = pd.read_html(url, flavor='bs4')//using readhtml to get df_list
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]#match to find matching table from dataframe

   # #reading different file formats 
   
   # 1.csv
   # using pd.read_csv("File") #to add headers use df.columns["SNO","Name","another column heading"...] ####the Read_csv methods converts the data directly to df
    df.loc[[0,1,2], "First Name" ]
    df.iloc[[0,1,2], 0] //purely index based

    #Python’s Transform function returns a self-produced dataframe with transformed values after applying the function specified in its parameter.
    df = df.transform(func = lambda x : x + 10) #func to add own customised function for data filtering and other usefull processes


   # 2.JSON 
   # #using json.load
   # with open("filename",'rw') as file
   # json_obj=json.load(file)
    import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
#writing data to json file 
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)
# Serializing dictionaries or file pointer to json //converting data structures into a readible format is called serialization 
json_object = json.dumps(person, indent = 4) //indent is defines the number of units for indentation

deserialization : reading json to a file converts the special format to usable object

#   3.XLSX
#     filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())

# await download(filename, "file_example_XLSX_10.xlsx")

# df = pd.read_excel("file_example_XLSX_10.xlsx")

   # 4.XML
   # import xml.etree.ElementTree ass etree
   # column = ["SNO","Name","another column heading"...]
   # df=pd.DataFrame(columns=column)
    # for node in root:
    #     sno=node.find("SNO").text
    #     name=node.fEind("name").text
    #     another=node.find("another column heading").text
    # df=df.append(pd.Series[sno,name,another],index=columns,ignore_index=true)


#writing files 
# import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

#reading files 
import xml.etree.ElementTree as etree

tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root: 

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)
 or 

 df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 

 ###############################################################################################################################################################

 BINARY FILES READING :like jpegs,pngs,mp3 all are binary files

 1.Image files
 img = Image.open('dog.jpg') 
  
# Output Images 
display(img)

