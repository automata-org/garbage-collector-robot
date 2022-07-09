import ros_utils_py.ros_service as ServiceClient
import sys
import rospy
from std_srvs.srv import Trigger


def main():
    #ROS nodes must be initialized rospy.init_node....
    client = ServiceClient.GenericServiceClient("talk_service", Trigger)
    res1 = client.request()
    print("Service Talker ->", res1.message)   


if __name__ == "__main__":
    main()
