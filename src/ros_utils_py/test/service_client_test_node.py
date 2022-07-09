import ros_utils_py.ros_service as ServiceClient
import sys
import rospy
from std_srvs.srv import Trigger


def main():
    rospy.init_node("service_client_test_node")
    client = ServiceClient.GenericServiceClient("talk_service", Trigger)
    res1 = client.request()
    print("Service Talker ->", res1.message)   


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
