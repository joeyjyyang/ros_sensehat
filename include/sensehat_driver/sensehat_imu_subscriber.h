#ifndef SENSEHAT_IMU_SUBSCRIBER_H
#define SENSEHAT_IMU_SUBSCRIBER_H

#include <iostream>
#include <string>

#include "ros/ros.h"
#include "sensor_msgs/Imu.h"

class SenseHatIMUSubscriber {
	public:
		SenseHatIMUSubscriber(const ros::NodeHandle &p_nh);
		
		void IMUCallback(const sensor_msgs::Imu::ConstPtr &imu_msg);

		~SenseHatIMUSubscriber();

	private:
		ros::Subscriber m_sensehat_imu_subscriber;
		ros::NodeHandle m_nh;
};

#endif // SENSEHAT_IMU_SUBSCRIBE_H
