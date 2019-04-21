#!/usr/bin/env python

import rospy
from sensehat_driver.srv import *
from sense_hat import SenseHat

def handle_calc_temp_diff(request):
    sense_temp = sense.get_temperature() 
    #print "Returning [%s - %s = %s]" % (sense_temp, req.input_temp, (sense_temp - req.input_temp))
    return TemperatureDifferenceResponse(sense_temp - request.input_temp)

def calc_temp_diff_server():
    rospy.init_node("calc_temp_diff_server")
    service = rospy.Service("calc_temp_diff", TemperatureDifference, handle_calc_temp_diff)
    #print("Ready to calculate temperature difference.")
    rospy.spin()

if __name__ == "__main__":
    sense = SenseHat()
    calc_temp_diff_server()
