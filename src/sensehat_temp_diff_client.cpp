#include "ros/ros.h"
#include "sensehat_driver/TemperatureDifference.h"
#include <cstdlib>

int main(int argc, char* argv[]) {
	ros::init(argc, argv, "calc_temp_diff_client");

	if (argc != 2) {
		ROS_INFO("Usage: rosrun sensehat_driver calc_temp_diff_client input_temp ");
		return 1;
	};

	ros::NodeHandle n;
	ros::ServiceClient client = n.serviceClient<sensehat_driver::TemperatureDifference>("calc_temp_diff");

	sensehat_driver::TemperatureDifference service;
	//get input temperature from command line arg
	service.request.input_temp = atof(argv[1]);
	
	//call service
	if (client.call(service)) {
		ROS_INFO("Temperature difference: %f", (float)service.response.temp_diff);
	}
	else {
		ROS_ERROR("Failed to call service calc_temp_diff");
		return 1;
	}

	return 0;
}



