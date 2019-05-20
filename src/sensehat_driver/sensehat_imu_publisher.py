#!/usr/bin/env python

import rospy
from sensehat_api import SenseHatAPI
from sensehat_driver.msg import IMUOrientationEuler 
from sensor_msgs.msg import Imu

class SenseHatIMUPublisher:

    def __init__(self):
        self.sensehat_api = SenseHatAPI()
        
        #initialize messages
        self.imu_orientation_euler_msg = IMUOrientationEuler()
        self.imu_orientation_quaternion_msg = Imu()
        
        #initialize publishers
        self.imu_orientation_euler_pub = rospy.Publisher("imu_orientation_euler", IMUOrientationEuler, queue_size=5)
        self.imu_orientation_quaternion_pub = rospy.Publisher("imu_orientation_quaternion", Imu, queue_size=5)
    
    def publish_imu_data(self):
        #retrieve sensehat data
        self.orientation_euler = self.sensehat_api.get_orientation_degrees()
        self.orientation_quaternion = self.sensehat_api.get_orientation_quaternion()
        self.angular_velocity = self.sensehat_api.get_angular_velocity()
        self.linear_acceleration = self.sensehat_api.get_linear_acceleration()

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

        #publish messages
        self.imu_orientation_euler_pub.publish(self.imu_orientation_euler_msg)
        self.imu_orientation_quaternion_pub.publish(self.imu_orientation_quaternion_msg)
       
