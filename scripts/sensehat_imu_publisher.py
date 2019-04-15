#!/usr/bin/env python

import rospy
import sys
sys.path.insert(0, "../src")
from sensehat_imu import SenseHatIMU
from sensehat_driver.msg import IMUOrientation 
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, Vector3

class IMUPublisherNode:

    def __init__(self):
        pass

    def pub_imu_data(self):
        pub = rospy.Publisher("imu_data", IMUOrientation, queue_size=10)
        rate = rospy.Rate(30)
        imu_orientation = IMUOrientation()
        
        while not rospy.is_shutdown():
            orientation = sense.get_orientation()
            imu_orientation.pitch = orientation["pitch"]
            imu_orientation.roll = orientation["roll"]
            imu_orientation.yaw = orientation["yaw"]
            #rospy.loginfo(imu_orientation)
            pub.publish(imu_orientation)
            rate.sleep()

if __name__ == '__main__':
    sensehat_imu = SenseHatIMU()
    linear_accelerations = sensehat_imu.linear_accelerations()
    print(linear_accelerations["x"])
    #rospy.init_node("sensehat_imu_publisher", anonymous=True)
    try:
        pass     
        #pub_imu_data()
    except rospy.ROSInterruptException:
        pass
