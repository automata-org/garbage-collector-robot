import rospy
from std_msgs.msg import String


class GenericSubscriber:
    def __init__(self, topic_name, data_type, callback):
        self.subscriber = rospy.Subscriber(topic_name, data_type, callback)
    
    def subscribe (self):
        self.subscriber.subscribe()

