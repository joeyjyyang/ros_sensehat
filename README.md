# sensehat_driver
**A ROS driver for the Raspberry Pi Sense HAT.**

## Overview
The Sense HAT is an affordable and easy-to-use add-on board for the Raspberry Pi. It is equipped with a multitude of useful sensors including a 9-DoF IMU and various environmental sensors, which makes it an ideal asset for personal robotic projects. This ROS package provides an interface to access the functionalities of the Sense HAT add-on board, and includes a set of ROS nodes and launch files to immediately start extracting sensor data.

## Prerequisites
### Software
- Ubiquity Robotics Raspberry Pi Image: https://downloads.ubiquityrobotics.com/pi.html
	- Ubuntu 16.04 (Xenial)
	- ROS Kinetic
### Hardware
- Raspberry Pi 4 Model B
- Raspberry Pi Sense HAT
### Sense HAT Setup 
- The Sense HAT installation and calibration instructions can be found [here](https://www.raspberrypi.org/documentation/hardware/sense-hat/).

## Installation
### Install from Git Repository
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone --single-branch --branch kinetic-devel https://github.com/joeyjyyang/sensehat_driver.git
cd .. 
sudo apt-get install -y
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
catkin_make # catkin build sensehat_driver (if using catkin_tools)
source devel/setup.bash
rospack profile
```

## Nodes 
- `sensehat_imu_publisher_node(.py)`
	- Publishes orientation (in euler angles and quaternions) data from 9-DoF IMU sensors. 
- `sensehat_environment_publisher_node(.py)`
	- Publishes data from environmental sensors, including temperature, relative humidity, pressure, and magnetic field vectors.
- `sensehat_compass_display(.py)`
	- Displays current compass direction on LED grid based on heading/yaw readings.
- `sensehat_temp_diff_server(.py)`
	- Server to the calc_temp_diff service.
- `sensehat_imu_subscriber_node(.cpp)`
	- Generic/template subscriber to orientation data from 9-DoF IMU data sensors.
- `sensehat_temp_diff_client(.cpp)`
	- Client of the calc_temp_diff service.

## Services
- `calc_temp_diff`
	- Calculates (and outputs) the temperature difference (in celsius) between the user-input temperature and the current measured temperature.

## Topics
- `/air_pressure`
- `/magnetic_field`
- `/imu_orientation_euler`
- `/imu_orientation_quaternion`
- `/relative_humidity`
- `/temperature_celsius`
- `/temperature_fahrenheit`

## Messages
- `sensor_msgs/FluidPressure`
- `sensor_msgs/MagneticField`
- `sensor_msgs/Imu`
- `sensehat_driver/IMUOrientationEuler`
- `sensor_msgs/RelativeHumidity`
- `sensor_msgs/Temperature`
- `sensehat_driver/TemperatureFahrenheit`

## Usage
### Example
- `roslaunch sensehat_driver sensehat_compass_display.launch`

## References
- The Sense HAT API Reference can be found [here](https://pythonhosted.org/sense-hat/api/).
- The sensor_msgs Msg/Srv Documentation can be found [here](http://docs.ros.org/kinetic/api/sensor_msgs/html/index-msg.html).

## Contact
- Author and Maintainer: Joey Yang
- Email: joeyyang.ai@gmail.com
- GitHub: https://github.com/joeyjyyang
- LinkedIn: https://www.linkedin.com/in/joey-yang

