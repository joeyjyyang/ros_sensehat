#include "sensehat_driver/sensehat_imu_subscriber.h"

int main(int argc, char *argv[]) {
	
	ros::init(argc, argv, "sensehat_imu_subscriber_node");
	ros::NodeHandle nh;
	sensehat_imu::SenseHatIMUSubscriber sensehat_imu_subscriber(nh);
	ros::spin();

	return 0;
}
