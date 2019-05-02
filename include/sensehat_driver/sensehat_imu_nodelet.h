#ifndef SENSEHAT_IMU_NODELET_H
#define SENSEHAT_IMU_NODELET_H

#include "ros/ros.h"
#include "nodelet/nodelet.h"

namespace sensehat_imu 
{
class SenseHatIMUNodelet : public nodelet::Nodelet
{
public:
	SenseHatIMUNodelet();
	~SenseHatIMUNodelet();
};
}

#endif // SENSEHAT_IMU_SUBSCRIBE_H
