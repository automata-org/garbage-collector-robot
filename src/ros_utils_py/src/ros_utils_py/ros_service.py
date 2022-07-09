import rospy


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

class GenericServiceServer:

    def __init__ (self, topic_name, data_type, callback):
        self.serviceserver = rospy.Service(topic_name, data_type, callback)
