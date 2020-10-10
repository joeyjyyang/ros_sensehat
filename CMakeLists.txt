cmake_minimum_required(VERSION 2.8.3)
project(ros_sensehat)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  sensor_msgs
)

catkin_python_setup()

add_message_files(
  FILES
  IMUOrientationEuler.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime sensor_msgs
)

install(
   PROGRAMS scripts/sensehat_imu_publisher_node.py scripts/sensehat_compass_display_node.py scripts/sensehat_environment_publisher_node.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
