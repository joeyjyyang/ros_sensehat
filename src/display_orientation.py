#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sense_hat import SenseHat

sense = SenseHat()

def display_callback(data):
    rospy.loginfo(rospy.get
def get_orientation():
    pub = rospy.Publisher('imu_orientation', String, queue_size=10)
    rospy.init_node('imu_read', anonymous=True)
    rate = rospy.Rate(30) 
    while not rospy.is_shutdown():
        orientation = sense.get_orientation()
        yaw = orientation["yaw"]
        imu_reading = "orientation relative to North (in degrees): %s" % yaw
        rospy.loginfo(imu_reading)
        pub.publish(imu_reading)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_orientation()
    except rospy.ROSInterruptException:
        pass
