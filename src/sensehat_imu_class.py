#!/usr/bin/env python

#import rospy
import math
#from sensehat_driver.msg import IMUOrientation 
from sense_hat import SenseHat
#from sensor_msgs.msg import Imu

class SenseHatIMU(SenseHat): 

    def __init__(self):
        SenseHat.__init__(self)

    def euler_to_quaternion(self):
        self.set_imu_config(True, True, True) #enable all (3) IMU sensors
        
        orientation_rad = self.get_orientation_radians()
        pitch_rad = orientation_rad["pitch"]
        roll_rad = orientation_rad["roll"]
        yaw_rad = orientation_rad["yaw"]

        cos_pitch = math.cos(pitch_rad * 0.5)
        sin_pitch = math.sin(pitch_rad * 0.5)
        cos_roll = math.cos(roll_rad * 0.5)
        sin_roll = math.sin(roll_rad * 0.5)
        cos_yaw = math.cos(yaw_rad * 0.5)
        sin_yaw = math.sin(yaw_rad * 0.5)

        quaternion_w = cos_pitch * cos_roll * cos_yaw + sin_pitch * sin_roll * sin_yaw
        quaternion_x = cos_pitch * sin_roll * cos_yaw - sin_pitch * cos_roll * sin_yaw
        quaternion_y = cos_pitch * sin_roll * sin_yaw + sin_pitch * cos_roll * cos_yaw
        quaternion_z = cos_pitch * cos_roll * sin_yaw - sin_pitch * sin_roll * cos_yaw

        quaternion = {"w" : quaternion_w, "x" : quaternion_x, "y" : quaternion_y, "z" : quaternion_z}
        return quaternion

if __name__ == "__main__":
    imu = SenseHatIMU()
    quaternion = imu.euler_to_quaternion()
    print(quaternion) 
    
