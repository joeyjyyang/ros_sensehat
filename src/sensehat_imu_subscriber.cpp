#include "sensehat_imu_subscriber.h"

SenseHatIMUSubscriber::SenseHatIMUSubscriber(const ros::NodeHandle &p_nh) : m_nh(p_nh) {
	//std::cout << "created object" << std::endl;
	m_sensehat_imu_subscriber = m_nh.subscribe("imu_data", 5, &SenseHatIMUSubscriber::IMUCallback, this);
}

void SenseHatIMUSubscriber::IMUCallback(const sensor_msgs::Imu::ConstPtr &imu_msg) {

	ROS_INFO("Heard quaternion w: [%s]", imu_msg->orientation.w.c_str());
}

SenseHatIMUSubscriber::~SenseHatImuSubscriber() {

}


