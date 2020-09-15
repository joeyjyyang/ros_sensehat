'''
  Author: Joey Yang
  Email: joeyyang.ai@gmail.com
  Description: 
    ROS node that begins publishing IMU data. 
'''

#!/usr/bin/env python

import rospy
from sensehat_driver import sensehat_imu_publisher

if __name__ == '__main__':
    
    rospy.init_node("sensehat_imu_publisher_node")
    sensehat_imu_pub = sensehat_imu_publisher.SenseHatIMUPublisher()
    spin_rate_param = rospy.get_param("~spin_rate")

    try:
        rate = rospy.Rate(spin_rate_param)    

        while not rospy.is_shutdown():
            sensehat_imu_pub.publish_imu_data()
            rate.sleep()         
    except rospy.ROSInterruptException:
        pass
