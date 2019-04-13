#!/usr/bin/env python

#import rospy
import math
#from sensehat_driver.msg import IMUOrientation 
#import sensehat_quaternion
from sensehat_quaternion import Quaternion
from sense_hat import SenseHat
#from sensor_msgs.msg import Imu

class SenseHatIMU(SenseHat): 

    def __init__(self):
        SenseHat.__init__(self)

        #enable all (3) IMU sensors
        self.set_imu_config(True, True, True)

    def euler_to_quaternion(self):
        #euler angles in radians
        self.orientation_euler = self.get_orientation_radians()
        pitch = self.orientation_euler["pitch"]
        roll = self.orientation_euler["roll"]
        yaw = self.orientation_euler["yaw"]

        cos_pitch = math.cos(pitch * 0.5)
        sin_pitch = math.sin(pitch * 0.5)
        cos_roll = math.cos(roll * 0.5)
        sin_roll = math.sin(roll * 0.5)
        cos_yaw = math.cos(yaw * 0.5)
        sin_yaw = math.sin(yaw * 0.5)

        quaternion_w = cos_pitch * cos_roll * cos_yaw + sin_pitch * sin_roll * sin_yaw
        quaternion_x = cos_pitch * sin_roll * cos_yaw - sin_pitch * cos_roll * sin_yaw
        quaternion_y = cos_pitch * sin_roll * sin_yaw + sin_pitch * cos_roll * cos_yaw
        quaternion_z = cos_pitch * cos_roll * sin_yaw - sin_pitch * sin_roll * cos_yaw

        self.orientation_quaternion = Quaternion(quaternion_w, quaternion_x, quaternion_y, quaternion_z)
        
        return self.orientation_quaternion

if __name__ == "__main__":
    imu = SenseHatIMU()
    orientation_quaternion = imu.euler_to_quaternion()
    orientation_quaternion.log_orientation()
