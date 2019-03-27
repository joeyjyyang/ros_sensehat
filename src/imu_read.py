#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sense_hat import SenseHat

def pub_orientation():
    pub = rospy.Publisher("imu_orientation", String, queue_size=10)
    rospy.init_node("imu_read", anonymous=True)
    rate = rospy.Rate(30)
    
    while not rospy.is_shutdown():
        orientation = sense.get_orientation()
        direction = orientation["yaw"]
        imu_reading = "%s" % direction
        rospy.loginfo(imu_reading)
        pub.publish(imu_reading)
        rate.sleep()

if __name__ == '__main__':
    sense = SenseHat()
    sense.set_imu_config(True, True, True)
    try:
        pub_orientation()
    except rospy.ROSInterruptException:
        pass
