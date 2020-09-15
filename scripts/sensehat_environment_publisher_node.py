'''
  Author: Joey Yang
  Email: joeyyang.ai@gmail.com
  Description: 
    ROS node that begins publishing environment sensor data.
'''
#!/usr/bin/env python

import rospy
from sensehat_driver import sensehat_environment_publisher

if __name__ == '__main__':
    
    rospy.init_node("sensehat_environment_publisher_node")
    sensehat_environment_pub = sensehat_environment_publisher.SenseHatEnvironmentPublisher()
    spin_rate_param = rospy.get_param('~spin_rate')

    try:
        rate = rospy.Rate(spin_rate_param)    

        while not rospy.is_shutdown():
            sensehat_environment_pub.publish_environment_data()
            rate.sleep()         
    except rospy.ROSInterruptException:
        pass
