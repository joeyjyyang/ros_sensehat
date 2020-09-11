#!/usr/bin/env python

import math
from sense_hat import SenseHat

class SenseHatDriver(SenseHat): 

    GRAVITY = 9.80665

    def __init__(self):
        super(SenseHatDriver, self).__init__()

    def get_orientation_quaternion(self):
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
       
        self.orientation_quaternion = dict()

        self.orientation_quaternion["x"] = cos_yaw * cos_pitch * sin_roll - sin_yaw * sin_pitch * cos_roll
        self.orientation_quaternion["y"] = sin_yaw * cos_pitch * sin_roll + cos_yaw * sin_pitch * cos_roll 
        self.orientation_quaternion["z"] = sin_yaw * cos_pitch * cos_roll - cos_yaw * sin_pitch * sin_roll 
        self.orientation_quaternion["w"] = cos_yaw * cos_pitch * cos_roll + sin_yaw * sin_pitch * sin_roll

        return self.orientation_quaternion

    def get_angular_velocity(self):
        #dict of angular velocities in rad/sec
        self.angular_velocity = self.get_gyroscope_raw()

        return self.angular_velocity

    def get_linear_acceleration(self):
        #dict of linear accelerations in g
        self.linear_acceleration_g = self.get_accelerometer_raw()
        #dict of linear accelerations in m/s^2
        self.linear_acceleration = dict()

        for axis, lin_accel_g in self.linear_acceleration_g.items():
            self.linear_acceleration[axis] = lin_accel_g * SenseHatDriver.GRAVITY
        
        return self.linear_acceleration

    def get_relative_humidity(self):
        self.relative_humidity = self.get_humidity() 

        return self.relative_humidity

    def get_temperature_celsius(self):
        self.temperature_celsius = self.get_temperature_from_humidity() #self.get_temperature_from_pressure()
        
        return self.temperature

    def get_magnetic_field(self):
        #dict of magnetic field vectors in microteslas
        self.magnetic_field = self.get_compass_raw() 

        return self.magnetic_field

    def get_air_pressure(self):
        self.air_pressure = self.get_pressure() #millibars

        return self.air_pressure

