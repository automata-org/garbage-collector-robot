from __future__ import print_function

import ros_utils_py.ros_service as GenericServiceClient
import sys
import rospy
from std_srvs.srv import Trigger


def main():
    client = GenericServiceClient("talk_service", Trigger)
    res1 = client.request()
    print("Service Talker ->", res1.message)   


if __name__ == "__main__":
    main()
