#!/usr/bin/env python

#import rospy
#from sensehat_driver.msg import IMUOrientation 
from sense_hat import SenseHat
#from sensor_msgs.msg import Imu

class SenseHatIMU(SenseHat): 

    def __init__(self):
        SenseHat.__init__(self)

if __name__ == "__main__":
    imu = SenseHatIMU()
    print(imu.temp)
    #sensehat
