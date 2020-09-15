'''
  Author: Joey Yang
  Email: joeyyang.ai@gmail.com
  Description: 
    Interface between the Sense HAT's environment sensors and the ROS ecosystem.
'''

#!/usr/bin/env python

import rospy
from sensehat_driver import SenseHatDriver
from sensor_msgs.msg import MagneticField, Temperature, FluidPressure, RelativeHumidity

class SenseHatEnvironmentPublisher:

    def __init__(self):
        self.sensehat_driver = SenseHatDriver()
        
        #initialize messages
        self.magnetic_field_msg = MagneticField()
        self.temperature_celsius_msg = Temperature()
        self.air_pressure_msg = FluidPressure()
        self.relative_humidity_msg = RelativeHumidity()
        
        #initialize publishers
        self.magnetic_field_pub = rospy.Publisher("magnetic_field", MagneticField, queue_size=1)
        self.temperature_celsius_pub = rospy.Publisher("temperature_celsius", Temperature, queue_size=1)
        self.air_pressure_pub = rospy.Publisher("air_pressure", FluidPressure, queue_size=1)
        self.relative_humidity_pub = rospy.Publisher("relative_humidity", RelativeHumidity, queue_size=1)
    
    def publish_environment_data(self):
        #retrieve sensehat data
        self.magnetic_field = self.sensehat_driver.get_magnetic_field()
        self.temperature_celsius = self.sensehat_driver.get_temperature_celsius()
        self.air_pressure = self.sensehat_driver.get_air_pressure()
        self.relative_humidity = self.sensehat_driver.get_relative_humidity()

        #populate messages
        self.magnetic_field_msg.magnetic_field.x = self.magnetic_field["x"]
        self.magnetic_field_msg.magnetic_field.y = self.magnetic_field["y"]
        self.magnetic_field_msg.magnetic_field.z = self.magnetic_field["z"]

        self.temperature_celsius_msg.temperature = self.temperature_celsius

        self.air_pressure_msg.fluid_pressure = self.air_pressure

        self.relative_humidity_msg.relative_humidity = self.relative_humidity

        #publish messages
        self.magnetic_field_pub.publish(self.magnetic_field_msg)
        self.temperature_celsius_pub.publish(self.temperature_celsius_msg)
        self.air_pressure_pub.publish(self.air_pressure_msg)
        self.relative_humidity_pub.publish(self.relative_humidity_msg)
       
