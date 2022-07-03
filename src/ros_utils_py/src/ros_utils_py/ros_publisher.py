import rospy

class GenericPublisher:
    def __init__(self, topic_name, data_type):
        self.publisher = rospy.Publisher(topic_name, data_type, queue_size=1)
    
    def publish(self, msg):
        self.publisher.publish(msg)