#!/usr/bin/env python

import rospy
from sensehat_api import SenseHatAPI
from sensor_msgs.msg import MagneticField, Temperature, FluidPressure, RelativeHumidity
from sensehat_driver.msg import TemperatureFahrenheit

class SenseHatEnvironmentPublisher:

    def __init__(self):
        self.sensehat_api = SenseHatAPI()
        
        #initialize messages
        self.magnetic_field_msg = MagneticField()
        self.temperature_celsius_msg = Temperature()
        self.temperature_fahrenheit_msg = TemperatureFahrenheit()
        self.air_pressure_msg = FluidPressure()
        self.relative_humidity_msg = RelativeHumidity()
        
        #initialize publishers
        self.magnetic_field_pub = rospy.Publisher("magnetic_field", MagneticField, queue_size=5)
        self.temperature_celsius_pub = rospy.Publisher("temperature_celsius", Temperature, queue_size=5)
        self.temperature_fahrenheit_pub = rospy.Publisher("temperature_fahrenheit", TemperatureFahrenheit, queue_size=5)
        self.air_pressure_pub = rospy.Publisher("air_pressure", FluidPressure, queue_size=5)
        self.relative_humidity_pub = rospy.Publisher("relative_humidity", RelativeHumidity, queue_size=5)
    
    def publish_environment_data(self):
        #retrieve sensehat data
        self.magnetic_field = self.sensehat_api.get_magnetic_field()
        self.temperature_celsius = self.sensehat_api.get_temperature_celsius()
        self.temperature_fahrenheit = self.sensehat_api.get_temperature_fahrenheit()
        self.air_pressure = self.sensehat_api.get_air_pressure()
        self.relative_humidity = self.sensehat_api.get_relative_humidity()

        #populate messages
        self.magnetic_field_msg.magnetic_field.x = self.magnetic_field["x"]
        self.magnetic_field_msg.magnetic_field.y = self.magnetic_field["y"]
        self.magnetic_field_msg.magnetic_field.z = self.magnetic_field["z"]

        self.temperature_celsius_msg.temperature = self.temperature_celsius
        self.temperature_fahrenheit_msg.temperature = self.temperature_fahrenheit

        self.air_pressure_msg.fluid_pressure = self.air_pressure

        self.relative_humidity_msg.relative_humidity = self.relative_humidity

        #publish messages
        self.magnetic_field_pub.publish(self.magnetic_field_msg)
        self.temperature_celsius_pub.publish(self.temperature_celsius_msg)
        self.temperature_fahrenheit_pub.publish(self.temperature_fahrenheit_msg)
        self.air_pressure_pub.publish(self.air_pressure_msg)
        self.relative_humidity_pub.publish(self.relative_humidity_msg)
       
