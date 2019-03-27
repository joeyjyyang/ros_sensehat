#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sense_hat import SenseHat

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)

def display_callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    direction = float(data.data)
    
    if (45 <= direction < 135):
        sense.show_letter("E")
    elif (135 <= direction < 225):
        sense.show_letter("S")
    elif (225 <= direction < 315):
        sense.show_letter("W")
    else:
        sense.show_letter("N")

def sub_orientation():
    rospy.init_node("display_orientation", anonymous=True)
    rospy.Subscriber("imu_orientation", String, display_callback)
    rospy.spin()

if __name__ == '__main__':
    sense = SenseHat()
    sense.clear()
    sub_orientation()
    

