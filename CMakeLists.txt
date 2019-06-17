cmake_minimum_required(VERSION 2.8.3)
project(sensehat_driver)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  sensor_msgs
)

catkin_python_setup()

add_message_files(
  FILES
  IMUOrientationEuler.msg
  TemperatureFahrenheit.msg
)

add_service_files(
   FILES
   TemperatureDifference.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime sensor_msgs
)

include_directories(
  include 
  ${catkin_INCLUDE_DIRS}
)

add_library(${PROJECT_NAME}
	src/sensehat_imu_subscriber.cpp
)

add_executable(sensehat_temp_diff_client src/sensehat_temp_diff_client.cpp)
target_link_libraries(sensehat_temp_diff_client ${catkin_LIBRARIES})
add_dependencies(sensehat_temp_diff_client sensehat_driver_gencpp)

add_executable(sensehat_imu_subscriber_node src/sensehat_imu_subscriber_node.cpp src/sensehat_imu_subscriber.cpp)
target_link_libraries(sensehat_imu_subscriber_node ${catkin_LIBRARIES})

install(PROGRAMS
   scripts/sensehat_imu_publisher_node
   scripts/sensehat_compass_display
   scripts/sensehat_temp_diff_server
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(TARGETS ${PROJECT_NAME} 
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.h"
   PATTERN ".svn" EXCLUDE
)

