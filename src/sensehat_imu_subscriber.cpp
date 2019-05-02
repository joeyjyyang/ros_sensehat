#include "sensehat_driver/sensehat_imu_subscriber.h"

sensehat_imu::SenseHatIMUSubscriber::SenseHatIMUSubscriber(const ros::NodeHandle &p_nh) : m_nh(p_nh) 
{
	m_sensehat_imu_subscriber = m_nh.subscribe("imu_data", 5, &SenseHatIMUSubscriber::IMUCallback, this);
}

void sensehat_imu::SenseHatIMUSubscriber::IMUCallback(const sensor_msgs::Imu::ConstPtr &imu_msg) 
{

	ROS_INFO("Heard quaternion w: [%f]", imu_msg->orientation.w);
}

sensehat_imu::SenseHatIMUSubscriber::~SenseHatIMUSubscriber() 
{

} 


