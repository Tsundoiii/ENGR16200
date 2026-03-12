#field_map.py
from basehat import IMUSensor
from basehat import Button
import time
import math

IMU = IMUSensor()

button = Button(22)

tFLAG=0
edgeNew=0
edgeOld=0
fid = open("FieldMagData.csv","w")
fid2 = open("FieldVecData.csv","w")
fid.write("Points,")
fid2.write("Points,")

xwidth=int(input("Enter the total number of x steps: "))
ywidth=int(input("Enter the total number of y steps: "))

for q in range(0,xwidth+1):
    fid.write(str(q))
    fid.write(",")
    fid2.write(str(q))
    fid2.write(",")
    fid2.write(",")
    fid2.write(",")
    
fid.write("\n")
fid2.write("\n")

time.sleep(0.1)

try:
    for a in range(0,xwidth):
        fid.write(str(a))
        fid.write(",")
        fid2.write(str(a))
        fid2.write(",")
        for b in range(0,ywidth):
            print("Move to location ("+str(a)+" , "+str(b)+") and press the button")
            while not tFLAG:
                edgeNew = button.value
                if edgeOld==1 and edgeNew==0:
                    tFLAG=1
                edgeOld=edgeNew
            try:
                x,y,z = IMU.getMag()
                total_mag=math.sqrt(x*x+y*y+z*z)
                fid.write(str(total_mag))
                fid.write(",")
                fid2.write(str(x))
                fid2.write(",")
                fid2.write(str(y))
                fid2.write(",")
                fid2.write(str(z))
                fid2.write(",")
            except IOError:
                print ("IO Error")
            tFLAG=0
        fid.write("\n")
        fid2.write("\n")
    fid.close()
    fid2.close()
    print("Data Collection Completed.\n")


except KeyboardInterrupt:
    fid.close()
    fid2.close()
