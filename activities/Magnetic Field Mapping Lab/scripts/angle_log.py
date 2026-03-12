from basehat import IMUSensor
from basehat import Button
import sys
import time
from math import sqrt

IMU = IMUSensor()
feele = open("magAngle.csv","w")

button = Button(22)

base=int(input("Enter the set distance to the magnet in cm: "))
gap=int(input("Enter the angular step in degrees (must multiply to 360): "))
steps=int(360/gap)
          
tFLAG=0
edgeNew=0
edgeOld=0

feele.write("Base Distance:,")
feele.write(str(base))
feele.write(" cm,\n\n")

feele.write("Angle,")
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

        print("\nRotate the sensor to "+str((a+1)*gap)+" degrees clockwise from the original heading")
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
            feele.write(" degrees,")
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
    print("Data Collection Completed.\n")
    
except KeyboardInterrupt:
    feele.close()
    sys.exit()
    
