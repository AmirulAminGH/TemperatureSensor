
import serial
import datetime
from time import sleep
import time
import datetime
import re

def getdate():
    now = datetime.datetime.now()
    date_string = now.strftime("%d%m%Y")
    return date_string

def gettime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H%M%S")
    return current_time


def extract_substring(input_string, start_index, end_index):
    # Extract the substring from the input string using slicing
    substring = input_string[start_index:end_index]

    # Return the extracted substring
    return substring

port = serial.Serial(
    port='COM9',
    baudrate=9600,
    timeout=5,
    #parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)
port.open

#w, h = 12, 1
#DataMatrix = [[0 for x in range(w)] for y in range(h)]
DataMatrix=['','','','','','','','','','','','']

today=getdate()
DataString="Date,Time,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10\n"

filename="C:/Temp/TempData"+str(getdate())+"_"+str(gettime())+".csv"
while True:
    data = port.readline().decode('utf-8')
    print(data)
    currentTime=gettime()
    #while currentTime==gettime():
    if "TS" in data :
        pattern = r'TS(.*?):'
        Id=re.findall(pattern,data)
        tempId=int(Id[0])

        pattern2 = r':(.*?),'
        Temp = re.findall(pattern2, data)
        tempData = Temp[0]

        DataMatrix[0]=today
        DataMatrix[1]=currentTime
        DataMatrix[tempId+1]=tempData
    for idx in range(len(DataMatrix)):
        DataString+=str(DataMatrix[idx])+","
    DataString+="\n"


    with open(filename, "w") as f:
        f.write(DataString)




