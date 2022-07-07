#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class GenericROSNode:
    def __init__(self, name):
        self.node=rospy.init_node(name, anonymous=True)
        self.publishers={}
        self.subscribers={}
    def main_task(self):
        pass
    def run(self,rate_hz):
        rate = rospy.Rate(rate_hz)
        while not rospy.is_shutdown():
            self.main_task()
            rate.sleep()
    def do_something(self):
        raise Exception("Not Implemented")
      
    def add_publisher(self,topic_name, data_type):
        self.publishers[topic_name]=rospy.Publisher(topic_name, data_type, queue_size=1)
    def add_subscriber(self, topic_name, data_type,callback):
        self.subscribers[topic_name]=rospy.Subscriber(topic_name, data_type, callback)
    def get_publisher(self,topic_name):
        try:
            pub=self.publishers[topic_name]
            return pub
        except:
            rospy.logerr("cannot find publisher for topic: ", topic_name)
            raise ValueError("publisher does not exist")
    def get_subscriber(self,topic_name):
        try:
            sub=self.subscribers[topic_name]
            return sub
        except:
            rospy.logerr("cannot find subscriber for topic: ", topic_name)
            raise ValueError("subscriber does not exist")
