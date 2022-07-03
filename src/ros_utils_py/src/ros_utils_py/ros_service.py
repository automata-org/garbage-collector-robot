from __future__ import print_function

import sys
import rospy
from std_srvs.srv import Trigger

class GenericServiceClient:
    def __init__(self, service_name, data_type):
        rospy.wait_for_service(service_name)
        try:
            self.service = rospy.ServiceProxy(service_name, data_type)
        except rospy.ServiceException as e:
            rospy.logerr("Service creation failed: %s" %rospy.get_time()) 
    
    def request(self, *args):
        try:
            response = self.service(*args)
            return response
        except rospy.ServiceException as e:
             print("service call failed")
