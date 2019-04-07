#!/usr/bin/env python

import rospy

def goal_orientation_client(goal_yaw):
    rospy.wait_for_service("heading_correction")
    try:
        heading_correction = rospy.ServiceProxy("heading_correction", 

