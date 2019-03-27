#!/usr/bin/env python

import rospy
#from std_msgs.msg import String
from sensehat_driver.msg import IMUOrientation #include custom IMU orientation messge 
from sense_hat import SenseHat

def pub_orientation():
    pub = rospy.Publisher("imu_orientation", IMUOrientation, queue_size=10)
    rospy.init_node("imu_read", anonymous=True)
    rate = rospy.Rate(30)
    imu_orientation = IMUOrientation()

    while not rospy.is_shutdown():
        orientation = sense.get_orientation()
        imu_orientation.pitch = orientation["pitch"]
        imu_orientation.roll = orientation["roll"]
        imu_orientation.yaw = orientation["yaw"]
        rospy.loginfo(imu_orientation)
        pub.publish(imu_orientation)
        rate.sleep()

if __name__ == '__main__':
    sense = SenseHat()
    sense.set_imu_config(True, True, True)
    
    try:
        pub_orientation()
    except rospy.ROSInterruptException:
        pass
