#!/usr/bin/env python

import math
#from sensehat_quaternion import Quaternion
from sense_hat import SenseHat

class SenseHatIMU(SenseHat): 

    GRAVITY = 9.80665

    def __init__(self):
        super(SenseHatIMU, self).__init__()

    def euler_to_quaternion(self):
        #enable all (3) IMU sensors 
        self.set_imu_config(True, True, True)

        #dict of euler angles in radians
        self.orientation_euler = self.get_orientation_radians()
 
        #heading z-axis
        yaw = self.orientation_euler["yaw"]
        #attitude y-axis
        pitch = self.orientation_euler["pitch"]
        #bank x-axis
        roll = self.orientation_euler["roll"]
        
        cos_yaw = math.cos(yaw * 0.5)
        sin_yaw = math.sin(yaw * 0.5)
        cos_pitch = math.cos(pitch * 0.5)
        sin_pitch = math.sin(pitch * 0.5)
        cos_roll = math.cos(roll * 0.5)
        sin_roll = math.sin(roll * 0.5)
        
        quaternion_x = cos_yaw * cos_pitch * sin_roll - sin_yaw * sin_pitch * cos_roll
        quaternion_y = sin_yaw * cos_pitch * sin_roll + cos_yaw * sin_pitch * cos_roll 
        quaternion_z = sin_yaw * cos_pitch * cos_roll - cos_yaw * sin_pitch * sin_roll 
        quaternion_w = cos_yaw * cos_pitch * cos_roll + sin_yaw * sin_pitch * sin_roll

        #self.orientation_quaternion = Quaternion(quaternion_x, quaternion_y, quaternion_z, quaternion_w)
        
        self.orientation_quaternion = dict()

        self.orientation_quaternion["x"] = quaternion_x
        self.orientation_quaternion["y"] = quaternion_y
        self.orientation_quaternion["z"] = quaternion_z
        self.orientation_quaternion["w"] = quaternion_w

        return self.orientation_quaternion

    def angular_velocity(self):
        #dict of angular velocities in rad/sec
        self.angular_velocity_rad_sec = self.get_gyroscope_raw()
       
        return self.angular_velocity_rad_sec

    def linear_acceleration(self):
        #dict of linear accelerations in g
        self.linear_acceleration_g = self.get_accelerometer_raw()
        #dict of linear accelerations in m/s^2
        self.linear_acceleration_m_s2 = dict()

        for axis, lin_accel_g in self.linear_acceleration_g.items():
            self.linear_acceleration_m_s2[axis] = lin_accel_g * SenseHatIMU.GRAVITY
        
        return self.linear_acceleration_m_s2

   




