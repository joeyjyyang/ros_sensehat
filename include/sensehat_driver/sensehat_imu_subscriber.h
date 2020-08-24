#ifndef SENSEHAT_IMU_SUBSCRIBER_H
#define SENSEHAT_IMU_SUBSCRIBER_H

#include <iostream>
#include <string>

#include "ros/ros.h"
#include "sensor_msgs/Imu.h"

namespace sensehat_driver
{
class SenseHatIMUSubscriber 
{
public:
  explicit SenseHatIMUSubscriber(const ros::NodeHandle& nh);
  void IMUCallback(const sensor_msgs::Imu::ConstPtr& imu_msg);
  ~SenseHatIMUSubscriber();
private:
  ros::Subscriber sensehat_imu_subscriber_;
  ros::NodeHandle nh_;
};
} // namespace sensehat_driver

#endif // SENSEHAT_IMU_SUBSCRIBE_H
