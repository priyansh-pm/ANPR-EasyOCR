import os
os.chdir('C:/Users/User/Desktop/ST Internship/annotatortool/Images')
a = os.listdir()
for i in range(0,len(a)):
    os.remove(a[i])