from basehat import IMUSensor
from basehat import Button
import sys
import time
from math import sqrt

IMU = IMUSensor()
feele = open("magDist.csv","w")

button = Button(22)

gap=int(input("Enter the distance between steps in cm: "))
steps=int(input("Enter the number of steps: "))
          
tFLAG=0
edgeNew=0
edgeOld=0

feele.write("Distance,")
feele.write("X axis,")
feele.write("Y axis,")
feele.write("Z axis,")
feele.write("Magnitude,")
feele.write("Time,\n")

time.sleep(0.1)

t0=time.time()
t_init=t0
try:
    for a in range(0,steps):

        print("\nMove the sensor to be "+str((a+1)*gap)+" cm away from the magnet")
        print("Press the button when you are ready to measure.")
        
        while not tFLAG:
            edgeNew = button.value
            if edgeOld==1 and edgeNew==0:
                tFLAG=1
            edgeOld=edgeNew
        tFLAG=0
 from basehat import IMUSensor
from basehat import Button
import sys
import time
from math import sqrt

IMU = IMUSensor()
feele = open("magDist.csv","w")

button = Button(22)

gap=int(input("Enter the distance between steps in cm: "))
steps=int(input("Enter the number of steps: "))
          
tFLAG=0
edgeNew=0
edgeOld=0

feele.write("Distance,")
feele.write("X axis,")
feele.write("Y axis,")
feele.write("Z axis,")
feele.write("Magnitude,")
feele.write("Time,\n")

time.sleep(0.1)

t0=time.time()
t_init=t0
try:
    for a in range(0,steps):

        print("\nMove the sensor to be "+str((a+1)*gap)+" cm away from the magnet")
        print("Press the button when you are ready to measure.")
        
        while not tFLAG:
            edgeNew = button.value
            if edgeOld==1 and edgeNew==0:
                tFLAG=1
            edgeOld=edgeNew
        tFLAG=0
        x,y,z = IMU.getMag()
        print("X axis: " + str(x) + "\tY axis: " +str(y) + "\tZ axis: " + str(z) + "\tTime: " +str(time.time()-t_init))
        time.sleep(0.1)
        if(x != 0 or y != 0 or z != 0):
            feele.write(str((a+1)*gap))
            feele.write(" cm,")
            feele.write(str(x))
            feele.write (",")
            feele.write(str(y))
            feele.write (",")
            feele.write(str(z))
            feele.write(",")
            feele.write(str(sqrt(x*x+y*y+z*z)))
            feele.write(",")

            t=time.time()
            delt=t-t0
            feele.write(str(delt))
            feele.write(",\n")
            
    feele.close()
    print("Data Collection Complete.")
    
except KeyboardInterrupt:
    feele.close()
    sys.exit()
    
       x,y,z = IMU.getMag()
        print("X axis: " + str(x) + "\tY axis: " +str(y) + "\tZ axis: " + str(z) + "\tTime: " +str(time.time()-t_init))
        time.sleep(0.1)
        if(x != 0 or y != 0 or z != 0):
            feele.write(str((a+1)*gap))
            feele.write(" cm,")
            feele.write(str(x))
            feele.write (",")
            feele.write(str(y))
            feele.write (",")
            feele.write(str(z))
            feele.write(",")
            feele.write(str(sqrt(x*x+y*y+z*z)))
            feele.write(",")

            t=time.time()
            delt=t-t0
            feele.write(str(delt))
            feele.write(",\n")
            
    feele.close()
    print("Data Collection Complete.")
    
except KeyboardInterrupt:
    feele.close()
    sys.exit()
    
