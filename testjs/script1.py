import cv2
import easyocr
from easyocr import Reader
import os
import json
reader = easyocr.Reader(['en'], gpu=True)

data = {}
os.chdir('C:/Users/User/Desktop/ST Internship/annotatortool/Images')

a = len(os.listdir())
image = cv2.cv2.imread(os.listdir()[a-1])
gray_image = cv2.cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)
a = ''
b = ''
c = ''
result = reader.readtext(gray_image, detail=0)
resulter = reader.readtext(gray_image)
for i in range(len(result), 0, -1):
    a = a+result[i-1]
for i in range(0, len(result)):
    b = b + result[i]
if not a[0].isalpha():
    c = b
else:
    c = a

data['car'] = []
data['car'].append({
    'leftbottom': resulter[0][0][0],
    'rightbottom': resulter[0][0][1],
    'righttop': resulter[0][0][2],
    'lefttop': resulter[0][0][3],
    'Plate': c,
    'confidence' : resulter[0][2]
})
print(data['car'])
a = " "
os.chdir('C:/Users/User/Desktop/ST Internship/annotatortool')

file1 = open("testjs/a.txt","w")
file1.write(a)
file1.close()

with open('testjs/a.txt') as json_data:
    for entry in json_data:
        print(entry, "<br>")
