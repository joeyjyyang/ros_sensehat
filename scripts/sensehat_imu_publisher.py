#!/usr/bin/env python

import rospy
import sys
sys.path.insert(0, "../src")
from sensehat_imu import SenseHatIMU
from sensehat_driver.msg import IMUOrientation 
from sensor_msgs.msg import Imu
#from geometry_msgs.msg import Quaternion, Vector3

class SenseHatIMUPublisherNode:

    def __init__(self):
        self.sensehat_imu = SenseHatIMU()
        
        self.imu_data_msg = Imu()
        self.imu_euler_msg = IMUOrientation() 
        
        self.pub_data = rospy.Publisher("imu_data", Imu, queue_size=1)
        self.pub_euler = rospy.Publisher("imu_euler", IMUOrientation, queue_size=1)

    def pub_imu_data(self):
        #self.orientation_quaternion = self.sensehat_imu


if __name__ == '__main__':
    rospy.loginfo("Publishing Sense Hat IMU data.")

    rospy.init_node("sensehat_imu_publisher", anonymous=True)
    

    sensehat_imu_publisher = SenseHatIMUPublisherNode()

    try:
        rate = rospy.Rate(30)    
        
        while not rospy.is_shutdown():
            sensehat_imu_publisher.pub_imu_data()
    except rospy.ROSInterruptException:
        pass
