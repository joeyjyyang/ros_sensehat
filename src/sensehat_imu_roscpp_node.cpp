#include "sensehat_imu_subscriber.h"

int main(int argc, char *argv[]) {
	
	ros::init(argc. argv, "sensehat_imu_roscpp_node", ros::init_options::AnonymouseName);
	ros::NodeHandle nh;

	SenseHatIMUSubscriber sensehat_imu_subscriber();

	return 0;
}
