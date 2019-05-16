#!/usr/bin/env python

import rospy
from sensehat_imu import SenseHatIMU
from sensehat_driver.msg import IMUOrientationEuler 
from sensor_msgs.msg import Imu, MagneticField, Temperature, FluidPressure, RelativeHumidity

class SenseHatIMUPublisher:

    def __init__(self):
        self.sensehat_imu = SenseHatIMU()
        
        #initialize messages
        self.imu_orientation_euler_msg = IMUOrientationEuler()
        self.imu_orientation_quaternion_msg = Imu()
        self.magnetic_field_msg = MagneticField()
        self.temperature_celsius_msg = Temperature()
        self.air_pressure_msg = FluidPressure()
        self.relative_humidity_msg = RelativeHumidity()
        
        #initialize publishers
        self.imu_orientation_euler_pub = rospy.Publisher("imu_orientation_euler", IMUOrientationEuler, queue_size=5)
        self.imu_orientation_quaternion_pub = rospy.Publisher("imu_orientation_quaternion", Imu, queue_size=5)
        self.magnetic_field_pub = rospy.Publisher("magnetic_field", MagneticField, queue_size=5)
        self.temperature_celsius_pub = rospy.Publisher("temperature_celsius", Temperature, queue_size=5)
        self.air_pressure_pub = rospy.Publisher("air_pressure", FluidPressure, queue_size=5)
        self.relative_humidity_pub = rospy.Publisher("relative_humidity", RelativeHumidity, queue_size=5)
    
    def pub_imu_data(self):
        #retrieve sensehat data
        self.orientation_euler = self.sensehat_imu.get_orientation_degrees()
        self.orientation_quaternion = self.sensehat_imu.get_orientation_quaternion()
        self.angular_velocity = self.sensehat_imu.get_angular_velocity()
        self.linear_acceleration = self.sensehat_imu.get_linear_acceleration()
        self.magnetic_field = self.sensehat_imu.get_magnetic_field()
        self.temperature_celsius = self.sensehat_imu.get_temperature_celsius()
        self.air_pressure = self.sensehat_imu.get_air_pressure()
        self.relative_humidity = self.sensehat_imu.get_relative_humidity()

        #populate messages
        self.imu_orientation_euler_msg.pitch = self.orientation_euler["pitch"]
        self.imu_orientation_euler_msg.roll = self.orientation_euler["roll"]
        self.imu_orientation_euler_msg.yaw = self.orientation_euler["yaw"]
 
        self.imu_orientation_quaternion_msg.orientation.x = self.orientation_quaternion.quaternion_x
        self.imu_orientation_quaternion_msg.orientation.y = self.orientation_quaternion.quaternion_y
        self.imu_orientation_quaternion_msg.orientation.z = self.orientation_quaternion.quaternion_z
        self.imu_orientation_quaternion_msg.orientation.w = self.orientation_quaternion.quaternion_w
        self.imu_orientation_quaternion_msg.angular_velocity.x = self.angular_velocity["x"]
        self.imu_orientation_quaternion_msg.angular_velocity.y = self.angular_velocity["y"]
        self.imu_orientation_quaternion_msg.angular_velocity.z = self.angular_velocity["z"]
        self.imu_orientation_quaternion_msg.linear_acceleration.x = self.linear_acceleration["x"]
        self.imu_orientation_quaternion_msg.linear_acceleration.y = self.linear_acceleration["y"]
        self.imu_orientation_quaternion_msg.linear_acceleration.z = self.linear_acceleration["z"]

        self.magnetic_field_msg.magnetic_field.x = self.magnetic_field["x"]
        self.magnetic_field_msg.magnetic_field.y = self.magnetic_field["y"]
        self.magnetic_field_msg.magnetic_field.z = self.magnetic_field["z"]

        self.temperature_celsius_msg.temperature = self.temperature_celsius

        self.air_pressure_msg.fluid_pressure = self.air_pressure

        self.relative_humidity_msg.relative_humidity = self.relative_humidity

        #publish messages
        self.imu_orientation_euler_pub.publish(self.imu_orientation_euler_msg)
        self.imu_orientation_quaternion_pub.publish(self.imu_orientation_quaternion_msg)
        self.magnetic_field_pub.publish(self.magnetic_field_msg)
        self.temperature_celsius_pub.publish(self.temperature_celsius_msg)
        self.air_pressure_pub.publish(self.air_pressure_msg)
        self.relative_humidity_pub.publish(self.relative_humidity_msg)
       
