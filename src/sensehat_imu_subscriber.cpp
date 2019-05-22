#include "sensehat_driver/sensehat_imu_subscriber.h"

sensehat_imu::SenseHatIMUSubscriber::SenseHatIMUSubscriber(const ros::NodeHandle& nh) : nh_(nh) 
{
	sensehat_imu_subscriber_ = nh_.subscribe("imu_orientation_quaternion", 5, &SenseHatIMUSubscriber::IMUCallback, this);
}

void sensehat_imu::SenseHatIMUSubscriber::IMUCallback(const sensor_msgs::Imu::ConstPtr& imu_msg) 
{

	ROS_INFO("Quaternions: x=[%f], y=[%f], z=[%f], w=[%f]", imu_msg->orientation.x, imu_msg->orientation.y, imu_msg->orientation.z, imu_msg->orientation.w);
	/*
		Do something with data (i.e. get yaw/heading vs. time stamp and output warning if turning too fast)
	*/
}

sensehat_imu::SenseHatIMUSubscriber::~SenseHatIMUSubscriber() 
{

} 


