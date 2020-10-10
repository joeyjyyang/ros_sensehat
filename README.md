# ros_sensehat
**A ROS package containing a hardware driver for the Raspberry Pi Sense HAT and multiple ROS node wrappers that expose the sensor driver to the ROS ecosystem.**

## Overview
The Sense HAT is an affordable and easy-to-use add-on board for the Raspberry Pi. It is equipped with a multitude of useful sensors including a 9-DoF IMU and various environmental sensors, which makes it an ideal asset for personal robotic projects. This ROS package provides a ROS-agnostic hardware driver intreface to access the functionalities of the Sense HAT add-on board, and includes a set of ROS nodes that wrap around the driver and connects the sensor data to ROS topics.

## Prerequisites
### Software
- Ubiquity Robotics Raspberry Pi Image: https://downloads.ubiquityrobotics.com/pi.html
	- Ubuntu 16.04 (Xenial)
	- ROS Kinetic
### Hardware
- Raspberry Pi 4 Model B
- Raspberry Pi Sense HAT

## Installation
### Install from Git Repository
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone --single-branch --branch kinetic-devel https://github.com/joeyjyyang/ros_sensehat.git
cd .. 
sudo apt-get install -y
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
catkin_make # catkin build ros_sensehat (if using catkin_tools)
source devel/setup.bash
rospack profile
```

## Setup
### Calibration
- Sense HAT installation and calibration instructions: https://www.raspberrypi.org/documentation/hardware/sense-hat/

## Nodes 
- `sensehat_imu_publisher_node`
	- Publishes orientation (in euler angles and quaternions) data from 9-DoF IMU sensors. 
- `sensehat_environment_publisher_node`
	- Publishes data from environmental sensors, including temperature, relative humidity, pressure, and magnetic field vectors.
- `sensehat_compass_display_node`
	- Displays current compass direction on LED grid based on heading/yaw readings.

## Topics
- `/air_pressure`
- `/magnetic_field`
- `/imu_orientation_euler`
- `/imu_orientation_quaternion`
- `/relative_humidity`
- `/temperature_celsius`

## Messages
- `sensor_msgs/FluidPressure`
- `sensor_msgs/MagneticField`
- `sensor_msgs/Imu`
- `sensehat_driver/IMUOrientationEuler`
- `sensor_msgs/RelativeHumidity`
- `sensor_msgs/Temperature`

## Usage
### Example
- `roslaunch ros_sensehat sensehat_imu.launch`

## Contact
- Author and Maintainer: Joey Yang
- Email: joeyyang.ai@gmail.com
- GitHub: https://github.com/joeyjyyang
- LinkedIn: https://www.linkedin.com/in/joey-yang

