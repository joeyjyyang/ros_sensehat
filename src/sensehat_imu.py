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
 
        #heading
        yaw = self.orientation_euler["yaw"]
        #attitude
        pitch = self.orientation_euler["pitch"]
        #bank
        roll = self.orientation_euler["roll"]
        
        cos_yaw = math.cos(yaw * 0.5)
        sin_yaw = math.sin(yaw * 0.5)
        cos_pitch = math.cos(pitch * 0.5)
        sin_pitch = math.sin(pitch * 0.5)
        cos_roll = math.cos(roll * 0.5)
        sin_roll = math.sin(roll * 0.5)
        
        quaternion_w = cos_yaw * cos_pitch * cos_roll + sin_yaw * sin_pitch * sin_roll
        quaternion_x = cos_yaw * cos_pitch * sin_roll - sin_yaw * sin_pitch * cos_roll
        quaternion_y = sin_yaw * cos_pitch * sin_roll + cos_yaw * sin_pitch * cos_roll 
        quaternion_z = sin_yaw * cos_pitch * cos_roll - cos_yaw * sin_pitch * sin_roll 

        self.orientation_quaternion = Quaternion(quaternion_w, quaternion_x, quaternion_y, quaternion_z)
        
        return self.orientation_quaternion

if __name__ == "__main__":
    imu = SenseHatIMU()
    orientation_quaternion = imu.euler_to_quaternion()
    orientation_quaternion.log_orientation()
    print(imu.orientation_radians)
