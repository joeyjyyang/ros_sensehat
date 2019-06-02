# sensehat_driver
**A ROS driver for the Raspberry Pi Sense HAT**
## Overview
## Sense HAT Setup 
- The Sense HAT installation and calibration instructions can be found [here](https://www.raspberrypi.org/documentation/hardware/sense-hat/).
## Installation
## Usage
### Topics
- /air_pressure
- /magnetic_field
- /imu_orientation_euler
- /imu_orientation_quaternion
- /relative_humidity
- /temperature_celsius
- /temperature_fahrenheit
#### Messages
- sensor_msgs/FluidPressure
- sensor_msgs/MagneticField
- sensor_msgs/Imu
- sensehat_driver/IMUOrientationEuler
- sensor_msgs/RelativeHumidity
- sensor_msgs/Temperature
### Nodes
#### Publishers
- Generic 9-DoF IMU data
- Readings from environmental sensors 
#### Subscribers
- Generic 9-DoF IMU data
- Compass display based on heading/yaw
### Launch Files
- Compass display and log IMU data 
- Log environmental data
## References
- The Sense HAT API Reference can be found [here](https://pythonhosted.org/sense-hat/api/).
- The sensor_msgs Msg/Srv Documentation can be found [here](http://docs.ros.org/kinetic/api/sensor_msgs/html/index-msg.html).
