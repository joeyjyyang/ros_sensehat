'''
  Author: Joey Yang
  Email: joeyyang.ai@gmail.com
  Description: 
    ROS node that displays a letter (N, E, S, or W) representing the cardinal direction in whi    ch the Sense HAT is pointing towards, based on the Euler angle value of the yaw/heading.
'''

#!/usr/bin/env python

import rospy
from sensehat_driver.msg import IMUOrientationEuler
from sense_hat import SenseHat
from sensor_msgs.msg import Imu

def display_compass(data, compass_angles):
    if (compass_angles[0] <= data.yaw < compass_angles[1]):
        sense.show_letter("E")
    elif (compass_angles[1] <= data.yaw < compass_angles[2]):
        sense.show_letter("S")
    elif (compass_angles[2] <= data.yaw < compass_angles[3]):
        sense.show_letter("W")
    else:
        sense.show_letter("N")

if __name__ == '__main__':
    sense = SenseHat()
    sense.clear()

    rospy.init_node("sensehat_compass_display_node") 
    
    NE_angle_param = rospy.get_param("~NE_angle")
    SE_angle_param = rospy.get_param("~SE_angle")
    SW_angle_param = rospy.get_param("~SW_angle")
    NW_angle_param = rospy.get_param("~NW_angle")
    
    rospy.Subscriber("imu_orientation_euler", IMUOrientationEuler, display_compass, (NE_angle_param, SE_angle_param, SW_angle_param, NW_angle_param))
    rospy.spin()


