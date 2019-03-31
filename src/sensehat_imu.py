#!/usr/bin/env python

import rospy
from sensehat_driver.msg import IMUOrientation 
from sense_hat import SenseHat

def init_imu():
    compass_enabled = rospy.get_param("~compass_enabled")
    gyro_enabled = rospy.get_param("~gyro_enabled")
    accel_enabled = rospy.get_param("~accel_enabled")
    sense.set_imu_config(compass_enabled, gyro_enabled, accel_enabled)

def pub_imu_data():
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
    rospy.init_node("sensehat_imu", anonymous=True)
    sense = SenseHat()
    init_imu()

    try:
        pub_imu_data()
    except rospy.ROSInterruptException:
        pass
