import requests
import json
from PIL import Image
from io import BytesIO
import random
import tempfile
import os
import  hashlib
headers = {
    'Authorization': 'Bearer KEY',
    'Content-Type': 'application/json',
}

data = '{"path":""}'

response = requests.post('https://api.dropboxapi.com/2/files/list_folder', headers=headers, data=data)
content = response.json()

l = []
for i in content["entries"]:
	l.append(i["name"])
index = random.randrange(1,len(l),1)
headers = {
    'Authorization': 'Bearer KEY',
    'Dropbox-API-Arg': '{"path":"/'+l[index]+'"}',
}

response = requests.post('https://content.dropboxapi.com/2/files/download', headers=headers)

file = open(l[index], "wb")
file.write(response.content)
file.close()
'''
#img = Image.open(BytesIO(response.content))

#img.show()
tempfile.tempdir = os.getcwd()
temp = tempfile.TemporaryFile(mode='wb') #2

try:
	print("Name of the file is:", temp.name) #4
	temp.write(response.content)
	temp.seek(0)
finally:
	Image.open(temp.name).show()
	#temp.close()
'''
