import rospy
from std_msgs.msg import String #why?


class GenericSubscriber:
    def __init__(self, topic_name, data_type, callback):
        self.subscriber = rospy.Subscriber(topic_name, data_type, callback)
    
    def subscribe (self): #Why? subscription is already done by Subscriber constructor
        self.subscriber.subscribe()

