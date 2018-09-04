#MODULES
#Q.1
import datetime
Current_Date = datetime.datetime.today()
print ('Current Date: ' + str(Current_Date))
#Q-1.
import datetime as dt
print(dt.date.today())

#Q-2.
import webbrowser
x=input("search video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%x)

#Q-3.
import os
path = '/F:/New folder (2)/directory'
files = os.listdir(path)
i = 1

for file in files:
    a=input("name of file")
    os.rename(os.path.join(path, file), os.path.join(path, a+'.jpg'))
    i = i+1
