#include "sensehat_driver/sensehat_imu_subscriber.h"

sensehat_imu::SenseHatIMUSubscriber::SenseHatIMUSubscriber(const ros::NodeHandle& nh) : nh_(nh) 
{
	sensehat_imu_subscriber_ = nh_.subscribe("imu_data", 5, &SenseHatIMUSubscriber::IMUCallback, this);
}

void sensehat_imu::SenseHatIMUSubscriber::IMUCallback(const sensor_msgs::Imu::ConstPtr& imu_msg) 
{

	ROS_INFO("Quaternions: x=[%f], y=[%f], z=[%f], w=[%f]", imu_msg->orientation.x, imu_msg->orientation.y, imu_msg->orientation.z, imu_msg->orientation.w);
}

sensehat_imu::SenseHatIMUSubscriber::~SenseHatIMUSubscriber() 
{

} 


