#!/usr/bin/env python

import rospy
from sensehat_imu import SenseHatIMU
from sensehat_driver.msg import IMUOrientation 
from sensor_msgs.msg import Imu

class SenseHatIMUPublisher:

    def __init__(self):
        self.sensehat_imu = SenseHatIMU()
        
        self.imu_data_msg = Imu()
        self.imu_euler_msg = IMUOrientation() 
        
        self.imu_data_publisher = rospy.Publisher("imu_data", Imu, queue_size=1)
        self.imu_euler_publisher = rospy.Publisher("imu_euler", IMUOrientation, queue_size=1)

    def pub_imu_data(self):
         self.orientation_quaternion = self.sensehat_imu.euler_to_quaternion()
         self.orientation_euler = self.sensehat_imu.get_orientation_degrees()
         self.angular_velocity = self.sensehat_imu.angular_velocity()
         self.linear_acceleration = self.sensehat_imu.linear_acceleration()

         self.imu_data_msg.orientation.x = self.orientation_quaternion.quaternion_x
         self.imu_data_msg.orientation.y = self.orientation_quaternion.quaternion_y
         self.imu_data_msg.orientation.z = self.orientation_quaternion.quaternion_z
         self.imu_data_msg.orientation.w = self.orientation_quaternion.quaternion_w
        
         self.imu_euler_msg.pitch = self.orientation_euler["pitch"]
         self.imu_euler_msg.roll = self.orientation_euler["roll"]
         self.imu_euler_msg.yaw = self.orientation_euler["yaw"]

         self.imu_data_msg.angular_velocity.x = self.angular_velocity["x"]
         self.imu_data_msg.angular_velocity.y = self.angular_velocity["y"]
         self.imu_data_msg.angular_velocity.z = self.angular_velocity["z"]

         self.imu_data_msg.linear_acceleration.x = self.linear_acceleration["x"]
         self.imu_data_msg.linear_acceleration.y = self.linear_acceleration["y"]
         self.imu_data_msg.linear_acceleration.z = self.linear_acceleration["z"]

         self.imu_data_publisher.publish(self.imu_data_msg)
         self.imu_euler_publisher.publish(self.imu_euler_msg)
